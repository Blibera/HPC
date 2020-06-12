import csv
import re
import operator

name ="단순 우선순위(5개)"

for jj in range(0,1):
    time = 1
    for l in range(1, 18):
        stack = 0
        time_stack = 1
        application_stack = 1
        if l == 6:
            pass
        else:
            f = open("C:/Users/DI_Lab/Desktop/knl16노드 수집/공유 파일/HMM 사용 데이터/6. HMM 사용 데이터/Total/" + str(name)+ "/"  + str(time) + "초/" + str(l) + ".csv", 'r')
            ff = open("C:/Users/DI_Lab/Desktop/knl16노드 수집/공유 파일/HMM 사용 데이터//6. HMM 사용 데이터/Low Stedv/" + str(name)+ "/" + str(time) + "초/" + str(l) + "-" + str(time) + "초 데이터.csv", "w",newline='')
            fff = open("C:/Users/DI_Lab/Desktop/knl16노드 수집/공유 파일/HMM 사용 데이터//6. HMM 사용 데이터/High Stedv/" + str(name)+ "/" + str(time) + "초/" + str(l) + "-" + str(time) + "초 데이터.csv", "w",newline='')
            print(f)
            print(ff)
            print(fff)
            write = csv.writer(ff)
            write_f = csv.writer(fff)
            while True:
                line = f.readline()
                if not line: break
                add = []
                add_list = []

                if stack == 1:
                    for j in range(line.count(',')+1):
                        tol = line.split(',')[j]
                        tol = tol.strip()
                        add.append(tol)
                    if "CG" in add:
                        write.writerow(add)
                    elif "FT" in add:
                        write.writerow(add)
                    elif "EP" in add:
                        pass
                    else:
                        write_f.writerow(add)

                else:
                    for j in range(line.count(',')):
                        tol = line.split(',')[j]
                        add.append(tol)
                    add.append("Appliction")
                    write.writerow(add)
                    write_f.writerow(add)
                    stack = 1




