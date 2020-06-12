import pandas as pd
import re
j = 0
#data = pd.read_csv('C:/Users/DI_Lab/Desktop/20년도 대학원 수업/퍼지이론 cf/data(영화 이름, 닉네임, 평점).csv', encoding="euc-kr")
#data = pd.read_csv('C:/Users/DI_Lab/Desktop/20년도 대학원 수업/퍼지이론 cf/data(영화 종류, 닉네임, 평점).csv', encoding='utf-8-sig')
data = pd.read_csv('C:/Users/DI_Lab/Desktop/20년도 대학원 수업/퍼지이론 cf/원본.csv', encoding="utf-8-sig")

#name_list = ['nackname','공포', '범죄', '멜로/애정/로맨스', '액션', 'SF',             '스릴러', '드라마', '애니메이션', '코미디', '판타지',             '모험', '미스터리', '느와르', '전쟁', '가족',             '서스펜스', '무협', '뮤지컬', '다큐멘터리', '서부',             '실험', '블랙코미디', '서사']
def split(text):
    cleaned_text = re.sub('                   ', ',', text)
    cleaned_text = re.sub('                  ', ',', cleaned_text)
    cleaned_text = re.sub('                 ', ',', cleaned_text)
    cleaned_text = re.sub('                ', ',', cleaned_text)
    cleaned_text = re.sub('               ', ',', cleaned_text)
    cleaned_text = re.sub('              ', ',', cleaned_text)
    cleaned_text = re.sub('             ', ',', cleaned_text)
    cleaned_text = re.sub('            ', ',', cleaned_text)
    cleaned_text = re.sub('           ', ',', cleaned_text)
    cleaned_text = re.sub('          ', ',', cleaned_text)
    cleaned_text = re.sub('         ', ',', cleaned_text)
    cleaned_text = re.sub('        ', ',', cleaned_text)
    cleaned_text = re.sub('       ', ',', cleaned_text)
    cleaned_text = re.sub('      ', ',', cleaned_text)
    cleaned_text = re.sub('     ', ',', cleaned_text)
    cleaned_text = re.sub('    ', ',', cleaned_text)
    cleaned_text = re.sub('   ', ',', cleaned_text)
    cleaned_text = re.sub('  ', ',', cleaned_text)
    cleaned_text = re.sub(' ', ',', cleaned_text)
    cleaned_text = re.sub(',', '  ', cleaned_text)
    return cleaned_text
grouped = data.groupby('nickname')
count = grouped.count()

# 10 ~ 5000개 댓글만 추출. 5000개 넘는건 다른 사용자를 동일한 사용자로 인식해서 발생하는 문제로 생각
count_10 = count.loc[count.rate > 20]
count_10 = count_10.loc[count.rate < 500]

# column name을 nickname으로 변환하여 추출하기 위해
count_10 = count_10.T

# nickname추출
nickname = count_10.columns.values
nickname = nickname.T

a = pd.DataFrame(nickname, columns=['nickname'])
k = pd.merge(data, a)
print(k)

k.to_csv("C:/Users/DI_Lab/Desktop/20년도 대학원 수업/퍼지이론 cf/원본 - FULL.csv", mode='w', encoding='utf-8-sig')

