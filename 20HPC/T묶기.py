import csv
import re
import operator

for l in range(1, 18):
    stack = 0
    time = 10
    time_stack = 1
    application_stack = 1
    if l == 6:
        pass
    else:
        f = open("C:/Users/DI_Lab/Desktop/knl16노드 수집/공유 파일/HMM 사용 데이터/6. HMM 사용 데이터/선정 순위(5개)/" + str(l) + ".csv", 'r')
        ff = open("C:/Users/DI_Lab/Desktop/knl16노드 수집/공유 파일/HMM 사용 데이터//6. HMM 사용 데이터/선정 순위(5개)/" + str(time) + "초/" + str(l) + "-" + str(time) + "초 데이터.csv", "w",newline='')

        print(f)
        write = csv.writer(ff)
        while True:
            line = f.readline()
            if not line: break
            add = []
            add_list = []

            if stack == 1:
                if "BT" in line:

                    if application_stack == 1:
                        application_stack = 2
                        time_stack = 1
                    else:
                        if time_stack == 1:
                            for k in range(line.count(',')):
                                tol = line.split(',')[k]
                                add.append(tol)
                            time_stack = time_stack + 1
                        elif time_stack == time:
                            for k in range(line.count(',')):
                                tol = line.split(',')[k]
                                add_list.append(tol)
                            add = add + add_list
                            time_stack = 1
                            add.append("BT")
                            write.writerow(add)
                            print(add)
                        else:
                            for k in range(line.count(',')):
                                tol = line.split(',')[k]
                                add_list.append(tol)
                            add = map(operator.add, add, add_list)
                            time_stack = time_stack + 1
                elif "CG" in line:
                    if application_stack == 2:
                        application_stack = 3
                        time_stack = 1
                    else:
                        if time_stack == 1:
                            for k in range(line.count(',')):
                                tol = line.split(',')[k]
                                add.append(tol)
                            time_stack = time_stack + 1
                        elif time_stack == time:
                            for k in range(line.count(',')):
                                tol = line.split(',')[k]
                                add_list.append(tol)
                            add = add + add_list
                            time_stack = 1
                            add.append("CG")
                            write.writerow(add)
                            print(add)
                        else:
                            for k in range(line.count(',')):
                                tol = line.split(',')[k]
                                add_list.append(tol)
                            add = map(operator.add, add, add_list)
                            time_stack = time_stack + 1
                elif "EP" in line:
                    if application_stack == 3:
                        application_stack = 4
                        time_stack = 1
                    else:
                        if time_stack == 1:
                            for k in range(line.count(',')):
                                tol = line.split(',')[k]
                                add.append(tol)
                            time_stack = time_stack + 1
                        elif time_stack == time:
                            for k in range(line.count(',')):
                                tol = line.split(',')[k]
                                add_list.append(tol)
                            add = add + add_list
                            time_stack = 1
                            add.append("EP")
                            write.writerow(add)
                            print(add)
                        else:
                            for k in range(line.count(',')):
                                tol = line.split(',')[k]
                                add_list.append(tol)
                            add = map(operator.add, add, add_list)
                            time_stack = time_stack + 1
                elif "FT" in line:
                    if application_stack == 4:
                        application_stack = 5
                        time_stack = 1
                    else:
                        if time_stack == 1:
                            for k in range(line.count(',')):
                                tol = line.split(',')[k]
                                add.append(tol)
                            time_stack = time_stack + 1
                        elif time_stack == time:
                            for k in range(line.count(',')):
                                tol = line.split(',')[k]
                                add_list.append(tol)
                            add = add + add_list
                            time_stack = 1
                            add.append("FT")
                            write.writerow(add)
                            print(add)
                        else:
                            for k in range(line.count(',')):
                                tol = line.split(',')[k]
                                add_list.append(tol)
                            add = map(operator.add, add, add_list)
                            time_stack = time_stack + 1
                elif "LU" in line:
                    if application_stack == 5:
                        application_stack = 6
                        time_stack = 1
                    else:
                        if time_stack == 1:
                            for k in range(line.count(',')):
                                tol = line.split(',')[k]
                                add.append(tol)
                            time_stack = time_stack + 1
                        elif time_stack == time:
                            for k in range(line.count(',')):
                                tol = line.split(',')[k]
                                add_list.append(tol)
                            add = add + add_list
                            time_stack = 1
                            add.append("LU")
                            write.writerow(add)
                            print(add)
                        else:
                            for k in range(line.count(',')):
                                tol = line.split(',')[k]
                                add_list.append(tol)
                            add = map(operator.add, add, add_list)
                            time_stack = time_stack + 1
                elif "MG" in line:
                    if application_stack == 6:
                        application_stack = 7
                        time_stack = 1
                    else:
                        if time_stack == 1:
                            for k in range(line.count(',')):
                                tol = line.split(',')[k]
                                add.append(tol)
                            time_stack = time_stack + 1
                        elif time_stack == time:
                            for k in range(line.count(',')):
                                tol = line.split(',')[k]
                                add_list.append(tol)
                            add = add + add_list
                            time_stack = 1
                            add.append("MG")
                            write.writerow(add)
                            print(add)
                        else:
                            for k in range(line.count(',')):
                                tol = line.split(',')[k]
                                add_list.append(tol)
                            add = map(operator.add, add, add_list)
                            time_stack = time_stack + 1
                else:
                    if application_stack == 7:
                        application_stack = 8
                        time_stack = 1
                    else:
                        if time_stack == 1:
                            for k in range(line.count(',')):
                                tol = line.split(',')[k]
                                add.append(tol)
                            time_stack = time_stack + 1
                        elif time_stack == time:
                            for k in range(line.count(',')):
                                tol = line.split(',')[k]
                                add_list.append(tol)
                            add = add + add_list
                            time_stack = 1
                            add.append("SP")
                            write.writerow(add)
                            print(add)
                        else:
                            for k in range(line.count(',')):
                                tol = line.split(',')[k]
                                add_list.append(tol)
                            add = map(operator.add, add, add_list)
                            time_stack = time_stack + 1


            else:
                for j in range(line.count(',')):
                    tol = line.split(',')[j]
                    add.append(tol)
                add.append("Appliction")
                write.writerow(add)
                stack = 1




