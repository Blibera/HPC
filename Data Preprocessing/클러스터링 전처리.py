import glob
import csv
import re
files = glob.glob('C:/Users/DI_Lab/Desktop/Paper_Data/Single_Paper작업/클러스터링 중점/보존비율 80퍼/*.csv')

def change(tol):
    if "collectl01_" in tol:
        tol = re.sub("collectl01_",'',tol)
    if "Perf_" in tol:
        tol = re.sub("Perf_",'',tol)
    if "node01_" in tol:
        tol = re.sub("node01_",'',tol)
    return tol
for file in files:
    with open(file, 'r') as f:
        save_file = open(file + "_문자 제거.csv", 'w', encoding='UTF8',newline='')
        write = csv.writer(save_file)
        while True:
            line = f.readline()
            if not line: break
            print(line)
            count = line.count(',')
            print(count)
            add = []
            for i in range(0,count):
                tol = line.split(',')[i]
                tol = change(tol)
                tol = re.sub("\"",'',tol)
                add.append(tol)
            write.writerow(add)