import csv
import re
import math
file_name = "epyc_single_perf_정규화"

#save_column = ["CPU","SRAM","Memory","Scheduler","VM"]
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
        for i in range (0,27):
            if i == 0 or i == 1 or i == 3 or i == 4:
                add_num = line.split(',')[i]
                add_num = float(add_num)
                CPU = CPU + add_num
            elif i == 12 or i == 13 or i == 14 or i == 15 or i == 7:
                add_num = line.split(',')[i]
                add_num = float(add_num)
                VM = VM + add_num
            elif i == 9 or i == 10 or i == 8 or i == 16 or i == 5 or i == 6:
                add_num = line.split(',')[i]
                add_num = float(add_num)
                Scheduler = Scheduler + add_num
            else:
                add_num = line.split(',')[i]
                add_num = float(add_num)
                Memory = Memory + add_num
        add_list.append(CPU)
        add_list.append(Memory)
        add_list.append(Scheduler)
        add_list.append(VM)

        write.writerow(add_list)
    else:
        stack = 1
