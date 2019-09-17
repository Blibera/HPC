import csv
import re
import numpy

f = open("C:/Users/Slayer/Desktop/연구실 자료/Kisti 관련/Performance Analysis/Perf Data/result_ep_80유지.csv", 'r', encoding='UTF8')
ff = open("C:/Users/Slayer/Desktop/연구실 자료/Kisti 관련/Performance Analysis/Perf Data/perf_list.csv", "w", newline='')
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
    save_matrix = []
    sort_matrix = []
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
    print(sort_matrix)

    top = sort_matrix[0]
    top_10 = top*0.9
    print(top)
    print(top_10)

    for i in range(list_count):
        if main_matrix[i][1] > top_10:
            tol = main_matrix[i][0]
            save_matrix.append(tol)
        else:
            pass
    write.writerow(save_matrix)