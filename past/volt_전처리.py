import csv
import re
import pandas as pd
import math

# 결정해주기
select = ["node01","node02"]

# Dstat의 앞의 5줄을 잘라내기 위한 코드
dstat_cut_stack = 0

# csv에 저장하는 배열
add = []

name = ["node01","node02"]
node = 8

def split(text):
    cleaned_text = re.sub('                          ', '★', text)
    cleaned_text = re.sub('                         ', '★', cleaned_text)
    cleaned_text = re.sub('                        ', '★', cleaned_text)
    cleaned_text = re.sub('                       ', '★', cleaned_text)
    cleaned_text = re.sub('                      ', '★', cleaned_text)
    cleaned_text = re.sub('                     ', '★', cleaned_text)
    cleaned_text = re.sub('                    ', '★', cleaned_text)
    cleaned_text = re.sub('                   ', '★', cleaned_text)
    cleaned_text = re.sub('                  ', '★', cleaned_text)
    cleaned_text = re.sub('                 ', '★', cleaned_text)
    cleaned_text = re.sub('                ', '★', cleaned_text)
    cleaned_text = re.sub('               ', '★', cleaned_text)
    cleaned_text = re.sub('              ', '★', cleaned_text)
    cleaned_text = re.sub('             ', '★', cleaned_text)
    cleaned_text = re.sub('            ', '★', cleaned_text)
    cleaned_text = re.sub('           ', '★', cleaned_text)
    cleaned_text = re.sub('          ', '★', cleaned_text)
    cleaned_text = re.sub('         ', '★', cleaned_text)
    cleaned_text = re.sub('        ', '★', cleaned_text)
    cleaned_text = re.sub('       ', '★', cleaned_text)
    cleaned_text = re.sub('      ', '★', cleaned_text)
    cleaned_text = re.sub('     ', '★', cleaned_text)
    cleaned_text = re.sub('    ', '★', cleaned_text)
    cleaned_text = re.sub('   ', '★', cleaned_text)
    cleaned_text = re.sub('  ', '★', cleaned_text)
    cleaned_text = re.sub(' ', '★', cleaned_text)
    cleaned_text = re.sub('\t', '★', cleaned_text)
    return cleaned_text

# Perf
for i in range (0,2):
    # Perf 관련 정의
    perf_count = 0
    time_count = 1
    perf_full_text = ""
    perf_column_noname = ["cycles", "instructions", "branch-instructions", "branch-misses", "L1-dcache-load-misses",
                        "L1-dcache-loads", "L1-icache-load-misses", "LLC-loads", "LLC-load-misses", "LLC-stores",
                        "LLC-store-misses", "branch-loads", "branch-load-misses", "dTLB-loads", "dTLB-load-misses",
                        "dTLB-stores", "dTLB-store-misses", "iTLB-loads", "iTLB-load-misses", "node-loads",
                        "node-load-misses", "node-stores", "node-store-misses", "mem-loads", "mem-stores", "cpu-clock",
                        "migrations", "context-switches", "page-faults", "minor-faults", "major-faults", "Time"]
    perf_column_name =[]
    for j in range(0, 32):
        tol = str(select[i]) + "_" + str(perf_column_noname[j])
        perf_column_name.append(tol)
    num = i
    a = "C:/Users/Slayer/Desktop/연구실 자료/Kisti 관련/프로파일링 데이터/" + str(select[i]) + "_perf.txt"
    f = open(a, 'r')
    print(a)

    # 읽기 쉬운 txt 파일을 생성하기 위해 저장할 txt파일 생성
    make_txt = open("C:/Users/Slayer/Desktop/연구실 자료/Kisti 관련/프로파일링 데이터/전처리/CG_" + str(select[i]) + "_perf.txt", 'w')


    while True:
        line = f.readline()
        if not line: break
        if "unit" in line:
            pass
        elif "started" in line:
            pass
        elif "\n" == line:
            pass
        else:
            line = split(line)
            make_txt.write(line)
    # 읽기 쉽게 바꾼 txt 파일을 다시 읽음
    c = "C:/Users/Slayer/Desktop/연구실 자료/Kisti 관련/프로파일링 데이터/전처리/CG_" + str(select[i]) + "_perf.txt"
    f = open(c, 'r')
    b = "C:/Users/Slayer/Desktop/연구실 자료/Kisti 관련/프로파일링 데이터/전처리/CG_" + str(select[i]) + "_perf.csv"
    ff = open(b, 'w', newline='')
    write = csv.writer(ff)
    write.writerow(perf_column_name)
    add = []
    while True:
        line = f.readline()
        if not line: break


        if perf_count == 31:
            perf_count = 0
            write.writerow(add)
            add = []
            tol = line.split('★')[2]
            tol = re.sub(',','',tol)
            add.append(tol)
            perf_count = perf_count + 1
        elif perf_count == 30:
            tol = line.split('★')[2]
            tol = re.sub(',','',tol)
            add.append(tol)
            tol = line.split('★')[1]
            tol = time_count*2
            tol = int(tol)
            add.append(tol)
            perf_count = perf_count + 1
            time_count = time_count + 1
        else:
            tol = line.split('★')[2]
            tol = re.sub(',','',tol)
            if "<" in tol:
                pass
            else:
                tol = int(round(float(tol)))
            add.append(tol)
            perf_count = perf_count + 1

ff.close()
# Volt
for i in range (0,2):
    # Vol 관련 정의
    vol_column_name_noname = ["Time (s)", "Package0(W)", "Cores(W)", "Cach(W)", "DRAM(W)"]
    vol_column_name = []
    vol_stack = 0
    for j in range(0, 5):
        tol = str(select[i]) + "_" + str(vol_column_name_noname[j])
        vol_column_name.append(tol)
    a = "C:/Users/Slayer/Desktop/연구실 자료/Kisti 관련/프로파일링 데이터/" + str(select[i]) + "_vol.txt"
    f = open(a, 'r')
    b = "C:/Users/Slayer/Desktop/연구실 자료/Kisti 관련/프로파일링 데이터/전처리/CG_" + str(select[i]) + "_vol.csv"
    ff = open(b, 'w', newline='')
    write = csv.writer(ff)
    write.writerow(vol_column_name)

    while True:
        line = f.readline()
        if not line: break
        line = split(line)
        add =[]
        if vol_stack == 1:
            for k in range(0,5):
                if k == 0 :
                    tol = line.split('★')[k]
                    tol = tol.split('.')[0]
                    tol = float(tol)
                    add.append(tol)
                elif k == 1 :
                    tol = line.split('★')[k]
                    tol = float(tol)
                    tol = round(tol, 3)
                    tol = float(tol)
                    add.append(tol)
                    package_v = tol
                elif k == 2 :
                    tol = line.split('★')[k]
                    tol = float(tol)
                    tol = round(tol, 3)
                    tol = float(tol)
                    add.append(tol)
                    core_v = tol
                elif k == 3 :
                    tol = line.split('★')[k]
                    tol = package_v - core_v
                    add.append(tol)
                else:
                    tol = line.split('★')[k]
                    tol = float(tol)
                    tol = round(tol, 3)
                    tol = float(tol)
                    add.append(tol)
            write.writerow(add)
        elif "Time" in line:
            vol_stack = 1
        else:
            pass
ff.close()
# Merge_Perf
for i in range (0,1):

    a = pd.read_csv("C:/Users/Slayer/Desktop/연구실 자료/Kisti 관련/프로파일링 데이터/전처리/CG_node01_perf.csv")
    b = pd.read_csv("C:/Users/Slayer/Desktop/연구실 자료/Kisti 관련/프로파일링 데이터/전처리/CG_node02_perf.csv")
    print(a)
    print(b)

    merged = pd.merge(a,b, left_on="node01_Time", right_on="node02_Time")

    merged = pd.DataFrame(merged)
    merged = merged.drop('node01_Time', axis=1)
    merged = merged.drop('node02_Time', axis=1)
    merged.to_csv("C:/Users/Slayer/Desktop/연구실 자료/Kisti 관련/프로파일링 데이터/전처리/CG_Perf.csv",header=True)

# Merge_Volt
for i in range (0,1):

    a = pd.read_csv("C:/Users/Slayer/Desktop/연구실 자료/Kisti 관련/프로파일링 데이터/전처리/CG_node01_vol.csv")
    b = pd.read_csv("C:/Users/Slayer/Desktop/연구실 자료/Kisti 관련/프로파일링 데이터/전처리/CG_node02_vol.csv")
    merged = pd.merge(a,b, left_on="node01_Time (s)", right_on="node02_Time (s)")

    merged = pd.DataFrame(merged)
    merged = merged.drop('node02_Time (s)', axis=1)

    merged.to_csv("C:/Users/Slayer/Desktop/연구실 자료/Kisti 관련/프로파일링 데이터/전처리/CG_" + str(node) + "_Volt.csv",header=True,index=False)