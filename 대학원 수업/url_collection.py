import requests
from bs4 import BeautifulSoup
import re
import csv
import time
save_file = open("C:/Users/DI_Lab/Desktop/20년도 대학원 수업/Naver_Movie_url.csv", "w",newline='')
write = csv.writer(save_file)
name = ["url"]
#name = ["movie_name", "date", "review_date", "type", "director", "actor", "nickname", "text", "rate"]
write.writerow(name)
def get_data(url):
    html = requests.get(url)
    html = BeautifulSoup(html.content, 'html.parser')
    html = str(html)
    html = html.split('감상평')[1]

    for i in range(1, 11):
        try:
            add = []
            Full_text = html.split('ac num')[i]
            Full_text = Full_text.split('title')[1]
            Full_text = Full_text.split('sword=')[1]
            Full_text = Full_text.split('&amp')[0]
            print(Full_text)
            url = "https://movie.naver.com/movie/point/af/list.nhn?st=mcode&sword=" + str(Full_text)+ "&target=after&page="
            add.append(url)
            write.writerow(add)
        except:
            pass

i = 1
while(i < 1000):
    try:
        test_url = 'https://movie.naver.com/movie/point/af/list.nhn?&page=' + str(i)
        print(i)
        i = i + 1
        get_data(test_url)
        if i/5 == 0:
            time.sleep(3)

    except:
        print(test_url)
save_file.close()