import csv
import re
import math
file_name = "epyc_multi_perf_정규화_svm_label"

save_column = ["CPU","Memory","Scheduler","VM"]

stack = 0

f = open("C:/Users/DI_lab/Desktop/클러스터/" + str(file_name) + ".csv", 'r', encoding='UTF8')
save_file = open("C:/Users/DI_lab/Desktop/클러스터/" + str(file_name) + "_svm_label.csv", 'w', encoding='UTF8',newline='')
write = csv.writer(save_file)
write.writerow(save_column)

while True:
    line = f.readline()
    if not line: break

    # 초기화
    CPU = 0
    SRAM = 0
    Memory = 0
    Scheduler = 0
    VM = 0
    add_list = []
    if stack == 1:
        for i in range (0,4):
            if i == 0 :
                tol = line.split(',')[i]
                tol = float(tol)
                if tol > 2.2:
                    CPU = 2
                elif tol > 1:
                    CPU = 1
                else:
                    CPU = 0
            elif i == 1 :
                tol = line.split(',')[i]
                tol = float(tol)
                if tol > 4.5:
                    Memory = 2
                else:
                    Memory = 0
            elif i == 2 :
                tol = line.split(',')[i]
                tol = float(tol)
                if tol > 2.2:
                    Scheduler = 2
                else:
                    Scheduler = 0
            elif i == 3 :
                tol = line.split(',')[i]
                tol = float(tol)
                if tol > 0.2:
                    VM = 2
                else:
                    VM = 0
        add_list.append(CPU)
        add_list.append(Memory)
        add_list.append(Scheduler)
        add_list.append(VM)

        write.writerow(add_list)
    else:
        stack = 1
