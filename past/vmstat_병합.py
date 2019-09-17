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
time_before = ""
loop_12 = 0
write = csv.writer(f_output)

while True:
    line_disk = f_disk.readline()
    line_mem = f_mem.readline()
    comma_count_disk = line_disk.count(',')
    comma_count_mem = line_mem.count(',')
    if not line_disk: break
    if stack == 0 :
        for i in range(0,comma_count_disk-1):
            tol = line_disk.split(',')[i]
            tol = tol.strip()
            add.append(tol)
        for i in range(0, comma_count_mem + 1):
            tol = line_mem.split(',')[i]
            tol = tol.strip()
            add.append(tol)
        write.writerow(add)
        stack = stack + 1
        add = []
    else:
        if loop_12 == 12:
            for i in range(0, 67):
                add[i] = add[i]/12
                add[i] = round(add[i],3)
            day = day.strip()
            time = time.strip()
            add.append(day)
            add.append(time)
            if time_before == time:
                time_before = time
                pass
            else:
                write.writerow(add)
                time_before = time
            loop_12 = 0
            add = []
            day = ''
            time = ''
            for i in range(0,52):
                if i == 50:
                    day = line_disk.split(',')[50]
                elif i == 51:
                    time = line_disk.split(',')[51]
                else:
                    tol = line_disk.split(',')[i]
                    tol = re.sub('\\n','',tol)
                    tol = int(tol)
                    add.append(tol)
            for j in range(0,17):
                tol = line_mem.split(',')[j]
                tol = re.sub('\\n', '', tol)
                tol = int(tol)
                add.append(tol)
            loop_12 = loop_12 + 1

        elif loop_12 == 0:
            for i in range(0,52):
                if i == 50:
                    day = line_disk.split(',')[50]
                elif i == 51:
                    time = line_disk.split(',')[51]
                else:
                    tol = line_disk.split(',')[i]
                    tol = re.sub('\\n','',tol)
                    tol = int(tol)
                    add.append(tol)
            for j in range(0,17):
                tol = line_mem.split(',')[j]
                tol = re.sub('\\n', '', tol)
                tol = int(tol)
                add.append(tol)
            loop_12 = loop_12 + 1

        else:
            loop_12 = loop_12 + 1

            for i in range(0,50):
                tol = line_disk.split(',')[i]
                tol = int(tol)
                add[i] = add[i] + tol
            for j in range(0,17):
                tol = line_mem.split(',')[j]
                tol = int(tol)
                add[j+50] = add[j+50] + tol