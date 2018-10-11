import csv
import re

f_disk = open("C:/Users/Slayer/Desktop/공유할것/NPB_log_knl02_64/NPB_EP_log/vmstat_disk/vmstat_disk_2018-08-02.csv", 'r')
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
    comma_count_disk = line_disk.count(',')
    print(comma_count_disk)
    add = []
    if stack == 0 :
        for i in range(0,comma_count_disk):
            tol = line_disk.split(',')[i]
            add.append(tol)
        write.writerow(add)
        stack = stack + 1
    if not line_disk: break