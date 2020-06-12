import re
import csv

open_file = open("C:/Users/DI_Lab/Desktop/20년도 Kisti 과제/knl_Data/막 다루는 곳/knl01,2_perf_분산제거(1,2통합)full_PCA.csv", 'r', encoding='UTF8')
save_file = open("C:/Users/DI_Lab/Desktop/20년도 Kisti 과제/knl_Data/막 다루는 곳/Up_down(1% 버전).csv", 'w', encoding='UTF8',newline='')

write = csv.writer(save_file)

# 첫줄의 변수를 그대로 사용하기 위함
stack = 0

# up, dowm 비율 설정
rate = 0.01
under = 1 - rate
uper = 1 + rate

# 첫 수행값은 before에 저장
before_stack = 0
before_pkg = 0
before_dram = 0
while True:
    line = open_file.readline()
    if not line: break

    # 입력 list
    add = []

    if stack == 0:
        for i in range(line.count(',') + 1):
            tol = line.split(',')[i]
            tol = tol.strip()
            add.append(tol)
        stack = 1
        write.writerow(add)
    else:
        if before_stack == 0:
            for i in range(line.count(',') + 1):
                if i == 25:
                    tol = line.split(',')[i]
                    before_pkg = float(tol)
                elif i == 26:
                    tol = line.split(',')[i]
                    before_dram = float(tol)
            before_stack = 1
        else:
            for i in range(line.count(',')+1):
                if i == 25:
                    tol = float(line.split(',')[i])
                    tol_down = before_pkg * under
                    tol_up = before_pkg * uper
                    if tol_down < tol and tol < tol_up:
                        before_pkg = tol
                        tol = 1
                    elif before_pkg>tol:
                        before_pkg = tol
                        tol = 0
                    else:
                        before_pkg = tol
                        tol = 2
                    add.append(tol)
                elif i == 26:
                    tol = float(line.split(',')[i])
                    tol_down = before_dram * under
                    tol_up = before_dram * uper
                    if tol_down < tol and tol < tol_up:
                        before_dram = tol
                        tol = 1
                    elif before_dram > tol:
                        before_dram = tol
                        tol = 0
                    else:
                        before_dram = tol
                        tol = 2
                    add.append(tol)
                else :
                    tol = line.split(',')[i]
                    add.append(tol)
            write.writerow(add)





