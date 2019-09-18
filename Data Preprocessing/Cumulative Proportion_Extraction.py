import csv
import re
import pandas as pd


f = open("C:/Users/Slayer/Desktop/연구실 자료/Kisti 관련/Performance Analysis/Perf Data/result_ep_80유지.csv", 'r', encoding='UTF8')
ff = open("C:/Users/Slayer/Desktop/연구실 자료/Kisti 관련/Performance Analysis/Perf Data/perf_pca_name_list.csv", "w", newline='')
write = csv.writer(ff)

# PC의 개수를 카운팅 할때 사용하는 변수
PC_Ceck_stack = 0
PC_num = 0

# 변수 선언
top = 0

# 배열 선언
add = []
column_name_list = []
column_name_list_copy = []

# sort할때 사용
sort_matrix = []

# column과 cp값이 있는 메트릭스
main_matrix = []

# 주요 column들을 모아서 저장할때 사용하는 매트릭스
save_matrix = []

# 해당 파일의 모든 정보를 하나의 메트릭스로 제작
list_full = []

while True:
    line = f.readline()
    if not line: break

    # PC의 개수를 카운팅함
    if PC_Ceck_stack == 0:
        PC_num = line.count(',')
        PC_Ceck_stack = 1

    # 카운팅이 끝나면 수행되는 부분분
    elif PC_Ceck_stack == 1:
        column_comma_count = line.count(',')
        for i in range(0, column_comma_count + 1):
            if i == 0:
                tol = line.split(',')[i]
                tol = re.sub('\n', '', tol)
                column_name_list.append(tol)
                i = 1
            else:
                tol = line.split(',')[i]
                tol = re.sub('\n', '', tol)
                add.append(tol)
        list_full.append(add)
        add = []

# 매트릭스 뒤집기
new_list = list(map(list, zip(*list_full)))

# column개수 구하기
list_count = len(new_list[0])

# column copy
column_name_list_copy = column_name_list

j = 0
for j in range(PC_num):
    # rupe마다 초기화 해줘야 하는 변수
    save_matrix = []
    sort_matrix = []
    main_matrix = []
    top = 0
    top_10 = 0

    line = str(new_list[j])
    line = re.sub('\[', '', line)
    line = re.sub('\]','',line)
    line = re.sub('\'','',line)

    for i in range(list_count):
        add = []
        tol = line.split(',')[i]
        tol = re.sub('\n', '', tol)
        tol = tol.strip()

        # float형 변환, R에서 오류가 안나게 하기 위함
        tol = float(tol)

        # 절대값
        tol = abs(tol)

        # column의 이름을 찾기 위함.
        add.append(column_name_list[i])
        add.append(tol)
        main_matrix.append(add)
    for i in range(list_count):
        tol = main_matrix[i][1]
        sort_matrix.append(tol)
    # Sort 수행
    sort_matrix.sort(reverse=True)

    # top값을 통해 상위 10% 값을 갖고있는 변수 추출
    top = sort_matrix[0]
    top_10 = top*0.9

    for i in range(list_count):
        if main_matrix[i][1] > top_10:
            tol = main_matrix[i][0]
            tol = tol.strip()
            tol = re.sub('\\n','',tol)
            save_matrix.append(tol)
        else:
            pass
    write.writerow(save_matrix)
f.close()
ff.close()

perf_pca_name_list = open("C:/Users/Slayer/Desktop/연구실 자료/Kisti 관련/Performance Analysis/Perf Data/perf_pca_name_list.csv", 'r')
perf_data = open("C:/Users/Slayer/Desktop/연구실 자료/Kisti 관련/Performance Analysis/Perf Data/perf.csv", 'r', encoding='UTF8')
perf_pca = open("C:/Users/Slayer/Desktop/연구실 자료/Kisti 관련/Performance Analysis/Perf Data/perf_pca.csv", "w", newline='')

# csv 파일읽기, 기존방법이 문제가 있어서 변경함.
lines = csv.reader(perf_pca_name_list)
lines_perf = csv.reader(perf_data)

# 중복제거를 위한 변수 저장 배열 생성
Deduplication = []

# 새로운 매트릭스 생성
matrix = []

for line in lines:

    column_count = len(line)
    for i in range(column_count):
        tol = line[i]
        tol = tol.strip()
        Deduplication.append(tol)

for line in lines_perf:
    matrix.append(line)

# 매트릭스 뒤집기
new_matrix = list(map(list, zip(*matrix)))

# column 중복제거
Deduplication_list = list(set(Deduplication))

# row 수만큼 루프 하기 위함
new_matrix_row = len(new_matrix)

# 범주형 변수 살리기 위한 check 변수
check = 0

# CP값의 범위에 맞는 값만을 사용하여 perf 매트릭스 정의
Perf_matrix = []
df = pd.DataFrame(new_matrix)
df.to_csv("C:/Users/Slayer/Desktop/연구실 자료/Kisti 관련/Performance Analysis/Perf Data/파일명t.csv", header=None, index=None)

test = []

for i in range(new_matrix_row):
    string = str(new_matrix[i][0])
    string = string.strip()
    string = re.sub(':','.',string)
    test.append(string)
    if check == 0:
        Perf_matrix.append(new_matrix[0])
        check = 1
    else:
        if string in Deduplication_list:
            Perf_matrix.append(new_matrix[i])
            print("a")
        else:
            pass

new_matrix = list(map(list, zip(*Perf_matrix)))
df = pd.DataFrame(new_matrix)
df.to_csv("C:/Users/Slayer/Desktop/연구실 자료/Kisti 관련/Performance Analysis/Perf Data/파일명t.csv", header=None, index=None)
k = len(Deduplication_list)
print(k)


df = pd.DataFrame(test)
df.to_csv("C:/Users/Slayer/Desktop/연구실 자료/Kisti 관련/Performance Analysis/Perf Data/파일명ttt.csv", header=None, index=None)

df = pd.DataFrame(Deduplication_list)
df.to_csv("C:/Users/Slayer/Desktop/연구실 자료/Kisti 관련/Performance Analysis/Perf Data/파일명tttt.csv", header=None, index=None)