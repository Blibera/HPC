import requests
from bs4 import BeautifulSoup
import re
import csv
import time
open_file = open("C:/Users/DI_Lab/Desktop/20년도 대학원 수업/Naver_Movie_url.csv", 'r')
save_file = open("C:/Users/DI_Lab/Desktop/20년도 대학원 수업/Naver_Movie.csv", "w",newline='', encoding='utf-8-sig')
write = csv.writer(save_file)
name = ["movie_name", "date", "review_date", "type", "director", "actor", "nickname", "text", "rate"]
write.writerow(name)
def get_data(url):
    url = url.strip()
    html_movie = requests.get(url)
    html_movie = BeautifulSoup(html_movie.content, 'html.parser')
    html_movie = str(html_movie)

    try:
        # Count
        count = html_movie.split('h5_right_txt')[1]
        count = count.split('fs_11">')[1]
        count = count.split('</strong>')[0]
        count = int(count.strip())
        count_num = count//10
        if count_num > 1000:
            count_num = 1000

        # 영화 이름
        movie_name = html_movie.split('choice_movie_info')[1]
        movie_name = movie_name.split('title="')[1]
        movie_name = movie_name.split('">')[0]

        # 개봉년도
        Date = html_movie.split('기본정보')[1]
        Date = Date.split('td>')[1]
        if "개봉" in Date:
            Date = Date.split('개봉')[1]
            Date = Date.split('">')[1]
            Date = Date.split('</a')[0]
        else:
            Date = "NULL"


        # 영화 종류
        html_movie_type = html_movie.split('기본정보')[1]
        html_movie_type = html_movie_type.split('td>')[1]
        html_movie_type = html_movie_type.split('|')[0]
        count = html_movie_type.count('</a>')
        if count == 0:
            movie_type = "NULL"
        else:
            stack = 0
            for i in range(1, count + 1):
                type_name = html_movie_type.split("\">")[i]
                type_name = type_name.split("</")[0]

                if stack == 0:
                    movie_type = type_name
                    stack = 1
                else:
                    movie_type = movie_type + str(',') + type_name
        print(movie_type)
        # 감독
        html_movie_director = html_movie.split('감독')[1]
        html_movie_director = html_movie_director.split('td>')[1]
        html_movie_director = html_movie_director.split('\">')[1]
        movie_director = html_movie_director.split('</a>')[0]


        # 배우
        html_movie_actor = html_movie.split('출연')[1]
        html_movie_actor = html_movie_actor.split('td>')[1]
        stack = 0
        count = html_movie_actor.count(',')
        for i in range(1, count + 2):
            actor_name = html_movie_actor.split("\">")[i]
            actor_name = actor_name.split("</a")[0]
            if stack == 0:
                movie_actor = actor_name
                stack = 1
            else:
                movie_actor = movie_actor + str(',') + actor_name
        # 리뷰 수집
        for j in range(1, count_num + 1):
            url_html = url + str(j)
            worng_url = url + str(j)
            url_html = requests.get(url_html)
            url_html = BeautifulSoup(url_html.content, 'html.parser')
            url_html = str(url_html)
            if j / 5 == 0:
                time.sleep(2)
            #try:
            for k in range(1,11):
                add = []
                k_html = url_html.split("ac num")[k]
                # 평점
                Rate = k_html.split('list_netizen_score')[1]
                Rate = Rate.split('em>')[1]
                Rate = Rate.split('</')[0]

                # 댓글 내용
                Text = k_html.split('title')[1]
                Text = Text.split('br/>')[1]
                Text = Text.split("<")[0]
                Text = Text.strip()

                # 리뷰 작성 날짜
                Date_review = k_html.split('author')[1]
                Date_review = Date_review.split('br/>')[1]
                Date_review = Date_review.split('</td')[0]

                # 아이디
                nickname = k_html.split('author')[1]
                nickname = nickname.split('after')[1]
                nickname = nickname.split('">')[1]
                nickname = nickname.split('</')[0]



                add.append(movie_name)
                add.append(Date)
                add.append(Date_review)
                add.append(movie_type)
                add.append(movie_director)
                add.append(movie_actor)
                add.append(nickname)
                add.append(Text)
                add.append(Rate)

                write.writerow(add)
    except:
        print(url)
    #print(movie_name)
    #print(Date)
    #print(movie_type)
    #print(movie_director)
    #print(movie_actor)

    # except:
    #    print(url)
    #    print(worng_url)
i = 1
tt = 1
while True:
    line = open_file.readline()
    if not line: break
    line_url = str(line)

    get_data(line_url)
    print(tt)

    tt = tt + 1

save_file.close()