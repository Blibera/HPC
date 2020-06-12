from selenium import webdriver

driver = webdriver.Chrome('C:/chromedriver')

driver.implicitly_wait(3)

driver.get('https://comic.naver.com/webtoon/detail.nhn?titleId=20853&no=1193&weekday=tue')