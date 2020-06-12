import pandas as pd
import csv
name = ['단순 우선순위(3개)', '단순 우선순위(5개)', '선정 순위(3개)', '선정 순위(5개)']


for i in range(0,4):
    for l in range(1,18):
        if l == 6:
            pass
        else:
            f = open("C:/Users/DI_Lab/Desktop/knl16노드 수집/공유 파일/HMM 사용 데이터/" + str(l) + ".csv", 'r')
            ff = open("C:/Users/DI_Lab/Desktop/knl16노드 수집/공유 파일/HMM 사용 데이터/6. HMM 사용 데이터/" + str(name[i]) + "/" + str(l) + ".csv", "w",newline='')
            write = csv.writer(ff)

            if i == 0:
                while True:
                    line = f.readline()
                    if not line: break
                    add = []
                    tol = line.split(',')[18]
                    tol = tol.strip()
                    add.append(tol)
                    tol = line.split(',')[19]
                    tol = tol.strip()
                    add.append(tol)
                    tol = line.split(',')[20]
                    tol = tol.strip()
                    add.append(tol)
                    tol = line.split(',')[21]
                    tol = tol.strip()
                    add.append(tol)
                    tol = line.split(',')[22]
                    tol = tol.strip()
                    add.append(tol)
                    tol = line.split(',')[23]
                    tol = tol.strip()
                    add.append(tol)
                    tol = line.split(',')[24]
                    tol = tol.strip()
                    add.append(tol)
                    write.writerow(add)
            elif i == 1:
                while True:
                    line = f.readline()
                    if not line: break
                    add = []
                    tol = line.split(',')[14]
                    tol = tol.strip()
                    add.append(tol)
                    tol = line.split(',')[16]
                    tol = tol.strip()
                    add.append(tol)
                    tol = line.split(',')[18]
                    tol = tol.strip()
                    add.append(tol)
                    tol = line.split(',')[19]
                    tol = tol.strip()
                    add.append(tol)
                    tol = line.split(',')[20]
                    tol = tol.strip()
                    add.append(tol)
                    tol = line.split(',')[21]
                    tol = tol.strip()
                    add.append(tol)
                    tol = line.split(',')[22]
                    tol = tol.strip()
                    add.append(tol)
                    tol = line.split(',')[23]
                    tol = tol.strip()
                    add.append(tol)
                    tol = line.split(',')[24]
                    tol = tol.strip()
                    add.append(tol)
                    write.writerow(add)
            elif i == 2:
                while True:
                    line = f.readline()
                    if not line: break
                    add = []
                    tol = line.split(',')[13]
                    tol = tol.strip()
                    add.append(tol)
                    tol = line.split(',')[19]
                    tol = tol.strip()
                    add.append(tol)
                    tol = line.split(',')[20]
                    tol = tol.strip()
                    add.append(tol)
                    tol = line.split(',')[21]
                    tol = tol.strip()
                    add.append(tol)
                    tol = line.split(',')[22]
                    tol = tol.strip()
                    add.append(tol)
                    tol = line.split(',')[23]
                    tol = tol.strip()
                    add.append(tol)
                    tol = line.split(',')[24]
                    tol = tol.strip()
                    add.append(tol)
                    write.writerow(add)
            elif i == 3:
                while True:
                    line = f.readline()
                    if not line: break
                    add = []
                    tol = line.split(',')[11]
                    tol = tol.strip()
                    add.append(tol)
                    tol = line.split(',')[13]
                    tol = tol.strip()
                    add.append(tol)
                    tol = line.split(',')[18]
                    tol = tol.strip()
                    add.append(tol)
                    tol = line.split(',')[19]
                    tol = tol.strip()
                    add.append(tol)
                    tol = line.split(',')[20]
                    tol = tol.strip()
                    add.append(tol)
                    tol = line.split(',')[21]
                    tol = tol.strip()
                    add.append(tol)
                    tol = line.split(',')[22]
                    tol = tol.strip()
                    add.append(tol)
                    tol = line.split(',')[23]
                    tol = tol.strip()
                    add.append(tol)
                    tol = line.split(',')[24]
                    tol = tol.strip()
                    add.append(tol)
                    write.writerow(add)


