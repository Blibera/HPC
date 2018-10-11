import csv
import re

f_disk = open("C:/Users/Slayer/Desktop/공유할것/NPB_log_knl02_64/NPB_EP_log/vmstat_disk/vmstat_disk_2018-08-02.csv", 'r',newline='')
f_mem = open("C:/Users/Slayer/Desktop/공유할것/NPB_log_knl02_64/NPB_EP_log/vmstat_mem/vmstat_mem_2018-08-02.csv", 'r',
             newline='')
f_output = open("C:/Users/Slayer/Desktop/공유할것/NPB_log_knl02_64/NPB_EP_log/vmstat.csv", 'w',
             newline='')
# 변수
stack = 0
string = ""
add = []
loop_12 = 0
write = csv.writer(f_output)

while True:
    line_disk = f_disk.readline()
    line_mem = f_mem.readline()
    comma_count_disk = line_disk.count(',')
    comma_count_mem = line_mem.count(',')
    print(comma_count_disk)
    print(comma_count_mem)
    if stack == 0 :
        for i in range(0,comma_count_disk):
            if i == 10:
                pass
            elif i == 11:
                pass
            else:
                tol = line_disk.split(',')[i]
                add.append(tol)
        for i in range(0,comma_count_mem):
            tol = line_mem.split(',')[i]
            add.append(tol)
        write.writerow(add)
        stack = stack + 1
        add = []
    else:
        if not line_disk: break
        if loop_12 == 0:
            for i in range(0, comma_count_disk+1):
                if i == 10:
                    pass
                elif i == 11:
                    pass
                else:
                    tol = line_disk.split(',')[i]
                    tol = int(tol)
                    add.append(tol)
            for i in range(0, comma_count_mem):
                if i == 17:
                    break
                tol = line_mem.split(',')[i]
                tol = int(tol)
                add.append(tol)
            loop_12 = loop_12 + 1

        elif loop_12 < 11:
            for i in range(0, comma_count_disk):
                if i == 10:
                    pass
                elif i == 11:
                    pass
                else:
                    tol = line_disk.split(',')[i]
                    add[i] = int(add[i]) + int(tol)
            for i in range(0, comma_count_mem-1):
                if i+comma_count_disk == 17+comma_count_disk:
                    break
                else:
                    tol = line_mem.split(',')[i]
                    add[i+comma_count_disk] = int(add[i+comma_count_disk]) + int(tol)
            loop_12 = loop_12 + 1
        else:
            for i in range(0, comma_count_disk + comma_count_mem - 3):
                add[i] = add[i] / 12
                add[i] = round(add[i], 3)
            loop_12 = 0
            write.writerow(add)
            add = []