def test_crawling():
    # import requests
    from time import sleep
    from random import randrange
    from selenium import webdriver
    from xml.etree.ElementTree import Element, dump
    from xml.etree.ElementTree import ElementTree
    from selenium.webdriver.chrome.options import Options
    from time import time
    import os
    import re
    # from selenium.webdriver.common.alert import Alert
    # from multiprocessing import Process


    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")
    browser = webdriver.Chrome('C:/Users/DI_Lab/Desktop/랩페어자료/chromedriver.exe', options=options)

    def indent(elem, level=0):
        i = "\n" + level * "  "
        if len(elem):
            if not elem.text or not elem.text.strip():
                elem.text = i + "  "
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
            for elem in elem:
                indent(elem, level + 1)
            if not elem.tail or not elem.tail.strip():
                elem.tail = i
        else:
            if level and (not elem.tail or not elem.tail.strip()):
                elem.tail = i

    files = os.listdir('C:/Users/DI_Lab/Desktop/10,11,12/')

    for file_name in files:
        f = open('C:/Users/DI_Lab/Desktop/10,11,12/' + file_name, 'r', encoding='euc-kr')

        urls = f.readlines()
        f.close()
        # meta-data convention eg
        # 1 topic(input word): 헬스케어
        # 2 number of total news: 2432
        # 3 number of news: 957
        # 4 start_date: 2018.01.01
        # 5 end_date: 2018.01.1
        meta_topic = file_name
        # urls[0].split(':')[1].strip()
        meta_start_data = '0'  # urls[3].split(':')[1].strip()
        meta_end_date = '1'  # urls[4].split(':')[1].strip()
        folder_name = '{0}_{1}~{2}'.format(meta_topic, meta_start_data, meta_end_date)
        os.mkdir('C:/Users/DI_Lab/Desktop/10,11,12/' + folder_name)

        # strip meta data
        urls = urls[5:len(urls) - 1]

        digit = len(str(len(urls)))
        start = time()
        for index, url in enumerate(urls):
            offset = '0' * (digit - len(str(index)))
            _id = offset + str(index + 1)
            browser.get(url)
            root_node = Element('xml')
            title_node = Element('title')
            date_node = Element('date')
            article_node = Element('article')

            if url.find('sports') == -1:
                # title
                try:
                    title = browser.find_element_by_id('articleTitle')
                    title_node.text = title.text
                    root_node.append(title_node)
                except Exception:
                    # Entertainment
                    continue

                # date
                try:
                    date = browser.find_element_by_class_name('t11').text
                    date_node.text = date
                    root_node.append(date_node)
                except Exception:
                    # Entertainment
                    continue

                # article
                try:
                    article_text = browser.execute_script("return $('#articleBodyContents')[0].outerText")
                    article_node.text = article_text
                except Exception:
                    # Entertainment
                    continue

            root_node.append(article_node)
            sleep(randrange(1, 3) * 0.1)
            indent(root_node)
            # write to xml
            ElementTree(root_node).write('C:/Users/DI_Lab/Desktop/10,11,12/' + folder_name + '/' + _id + '.xml', encoding='utf-8')
        end = time()
        print(end - start)
    browser.quit()


if __name__ == '__main__':
    test_crawling()