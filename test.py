import csv
import re
from operator import attrgetter
f_1 = open("C:/Users/Slayer/Desktop/공유할것 (2)/NPB_log_knl02_64/NPB_EP_log/pidstat_cpu/(평균)pidstat_cpu_2018-08-02.csv", 'r')
f_2 = open("C:/Users/Slayer/Desktop/공유할것 (2)/NPB_log_knl02_64/NPB_EP_log/pidstat_io/(평균)pidstat_io_2018-08-02.csv", 'r')
f_3 = open("C:/Users/Slayer/Desktop/공유할것 (2)/NPB_log_knl02_64/NPB_EP_log/pidstat_mem/(평균)pidstat_mem_2018-08-02.csv", 'r')
f_4 = open("C:/Users/Slayer/Desktop/공유할것 (2)/NPB_log_knl02_64/NPB_EP_log/pidstat_stack/(평균)pidstat_stack_2018-08-02.csv", 'r')
f_5 = open("C:/Users/Slayer/Desktop/공유할것 (2)/NPB_log_knl02_64/NPB_EP_log/pidstat_tswch/(평균)pidstat_tswch_2018-08-02.csv", 'r')
f = open("C:/Users/Slayer/Desktop/공유할것 (2)/NPB_log_knl02_64/NPB_EP_log/()작업/1차처리.csv", 'w',newline='')

write = csv.writer(f)

stack = 0
string = ""
add = []
loop_12 = 0
time = ""
def split(text):
    cleaned_text = re.sub('                   ', ',', text)
    cleaned_text = re.sub('                  ', ',', cleaned_text)
    cleaned_text = re.sub('                 ', ',', cleaned_text)
    cleaned_text = re.sub('                ', ',', cleaned_text)
    cleaned_text = re.sub('               ', ',', cleaned_text)
    cleaned_text = re.sub('              ', ',', cleaned_text)
    cleaned_text = re.sub('             ', ',', cleaned_text)
    cleaned_text = re.sub('            ', ',', cleaned_text)
    cleaned_text = re.sub('           ', ',', cleaned_text)
    cleaned_text = re.sub('          ', ',', cleaned_text)
    cleaned_text = re.sub('         ', ',', cleaned_text)
    cleaned_text = re.sub('        ', ',', cleaned_text)
    cleaned_text = re.sub('       ', ',', cleaned_text)
    cleaned_text = re.sub('      ', ',', cleaned_text)
    cleaned_text = re.sub('     ', ',', cleaned_text)
    cleaned_text = re.sub('    ', ',', cleaned_text)
    cleaned_text = re.sub('   ', ',', cleaned_text)
    cleaned_text = re.sub('  ', ',', cleaned_text)
    cleaned_text = re.sub(' ', ',', cleaned_text)
    return cleaned_text

def time_sec(text):
    hour = text.split(':')[0]
    min = text.split(':')[1]
    sec = text.split(':')[2]
    hour = int(hour)
    min = int(min)
    sec = int(sec)
    total = (3600 * hour) + (60 * min) + sec

    return total

def sec_time(text):
    hour = text//3600
    min = (text%3600)//60
    sec = (text%3600)%60
    hour = str(hour)
    min = str(min)
    sec = str(sec)
    total = hour + " : " + min + " : " + sec

    return total

# 1차 처리
# (command_pid ,time) 형식으로 만들기

while True:
    add= []
    if stack == 0:
        line = f_1.readline()
        stack = 1
    else:
        line = f_1.readline()
        if not line: break
        command_cpu = line.split(',')[7]
        pid_cpu = line.split(',')[2]
        time_cpu = line.split(',')[0]
        command_cpu = command_cpu.strip()
        pid_cpu = pid_cpu.strip()
        name_cpu = command_cpu + "_" + pid_cpu
        name_cpu = name_cpu.strip()
        time_cpu = time_cpu.strip()
        add.append(name_cpu)
        add.append(time_cpu)
        write.writerow(add)
stack = 0
while True:
    add= []
    if stack == 0:
        stack = 1
        line = f_2.readline()
    else:
        line = f_2.readline()
        if not line: break
        command_io = line.split(',')[6]
        pid_io = line.split(',')[2]
        time_io = line.split(',')[0]
        command_io = command_io.strip()
        pid_io = pid_io.strip()
        name_io = command_io + "_" + pid_io
        name_io = name_io.strip()
        time_io = time_io.strip()
        add.append(name_io)
        add.append(time_io)
        write.writerow(add)
stack = 0
while True:
    add= []
    if stack == 0:
        line = f_3.readline()
        stack = 1
    else:
        line = f_3.readline()
        if not line: break
        command_mem = line.split(',')[8]
        pid_mem = line.split(',')[2]
        time_mem = line.split(',')[0]
        command_mem = command_mem.strip()
        pid_mem = pid_mem.strip()
        name_mem = command_mem + "_" + pid_mem
        name_mem = name_mem.strip()
        time_mem = time_mem.strip()
        add.append(name_mem)
        add.append(time_mem)
        write.writerow(add)
stack = 0
while True:
    add= []
    if stack == 0:
        stack = 1
        line = f_4.readline()
    else:
        line = f_4.readline()
        if not line: break
        command_stack = line.split(',')[5]
        pid_stack = line.split(',')[2]
        time_stack = line.split(',')[0]
        command_stack = command_stack.strip()
        pid_stack = pid_stack.strip()
        name_stack = command_stack + "_" + pid_stack
        name_stack = name_stack.strip()
        time_stack = time_stack.strip()
        add.append(name_stack)
        add.append(time_stack)
        write.writerow(add)
stack = 0
while True:
    add= []
    if stack == 0:
        stack = 1
        line = f_5.readline()
    else:
        line = f_5.readline()
        if not line: break
        command_tswch = line.split(',')[5]
        pid_tswch = line.split(',')[2]
        time_tswch = line.split(',')[0]
        command_tswch = command_tswch.strip()
        pid_tswch = pid_tswch.strip()
        name_tswch = command_tswch + "_" + pid_tswch
        name_tswch = name_tswch.strip()
        time_tswch = time_tswch.strip()
        add.append(name_tswch)
        add.append(time_tswch)
        write.writerow(add)
stack = 0
f_1.close()
# 2차 처리
# sort 정렬 후 중복제거

f_2 = open("C:/Users/Slayer/Desktop/공유할것 (2)/NPB_log_knl02_64/NPB_EP_log/()작업/1차처리.csv", 'r')
f_avg = open("C:/Users/Slayer/Desktop/공유할것 (2)/NPB_log_knl02_64/NPB_EP_log/()작업/2차처리.csv", 'w',newline='')
write = csv.writer(f_avg)
add = []

while True:
    line = f_2.readline()
    if not line: break
    tol = re.sub("\r\n", '', line)
    tol = re.sub("\n", '', tol)
    add.append(tol)

add = list(set(add))
nn = len(add)

new_list = []

for i in add:
    line = i
    one = line.split(',')[0]
    two = line.split(',')[1]
    two = time_sec(two)
    new_list.append([one,two])
add = sorted(new_list, key=lambda x: x[1])
result = sorted(add, key=lambda x : x[0])

last_time = 0
now_list = []

for i in range (0,nn):
    now_list = result[i]
    now_time = now_list[1]
    add = []

    if last_time-12 < now_time and now_time < last_time+12:
        pass
    else:
        tol = now_list[0]
        add.append(tol)
        tol = now_list[1]
        tol = sec_time(tol)
        add.append(tol)
        last_time = now_time
        write.writerow(add)
f_avg.close()

# 3차 처리
# cpu 병합
f_3_1 = open("C:/Users/Slayer/Desktop/공유할것 (2)/NPB_log_knl02_64/NPB_EP_log/pidstat_cpu/(평균)pidstat_cpu_2018-08-02.csv", 'r')
f_3_2 = open("C:/Users/Slayer/Desktop/공유할것 (2)/NPB_log_knl02_64/NPB_EP_log/()작업/2차처리.csv", 'r',newline='')
f_avg = open("C:/Users/Slayer/Desktop/공유할것 (2)/NPB_log_knl02_64/NPB_EP_log/()작업/3차처리.csv", 'w',newline='')

write = csv.writer(f_avg)

test_list = []
rdr = csv.reader(f_3_1)
i = 0
stack = 0
time_1 = 0
while True:
    if stack == 0:
        line_1 = f_3_1.readline()
        stack = 1
    else:
        line_1 = f_3_1.readline()
        if not line_1: break
        line_1 = re.sub("\n",'',line_1)
        test_list.append(line_1)
while True:
    line_2 = f_3_2.readline()
    if not line_2: break
    name = line_2.split(',')[0]
    name = name.strip()
    time = line_2.split(',')[1]
    time = time_sec(time)
    time = int(time)
    input_time = sec_time(time)
    i = 0
    j = 0
    add = []
    add.append(name)
    add.append(input_time)
    while i < len(test_list):
        line_1 = test_list[i]

        command = line_1.split(',')[7]
        pid = line_1.split(',')[2]

        command = command.strip()
        pid = pid.strip()
        name_cpu = command + "_" + pid
        name_cpu = name_cpu.strip()
        name = name.strip()
        if name == name_cpu :
            tol = line_1.split(',')[0]
            time_1 = time_sec(tol)
            if time-10 < time_1 and time_1 < time+10:
                tol = line_1.split(',')[1]
                add.append(tol)
                tol = line_1.split(',')[3]
                add.append(tol)
                tol = line_1.split(',')[4]
                add.append(tol)
                tol = line_1.split(',')[5]
                add.append(tol)
                tol = line_1.split(',')[6]
                add.append(tol)
                del test_list[i]
                i = i - 1
                break
        i = i + 1
        if i == len(test_list):
            add.append(0)
            add.append(0)
            add.append(0)
            add.append(0)
            add.append(0)
            break
    write.writerow(add)
f_avg.close()

# 4차 처리
# io 병합
f_4_1 = open("C:/Users/Slayer/Desktop/공유할것 (2)/NPB_log_knl02_64/NPB_EP_log/pidstat_io/(평균)pidstat_io_2018-08-02.csv", 'r')
f_4_2 = open("C:/Users/Slayer/Desktop/공유할것 (2)/NPB_log_knl02_64/NPB_EP_log/()작업/3차처리.csv", 'r',newline='')
f_avg = open("C:/Users/Slayer/Desktop/공유할것 (2)/NPB_log_knl02_64/NPB_EP_log/()작업/4차처리.csv", 'w',newline='')

write = csv.writer(f_avg)

test_list = []
rdr = csv.reader(f_4_1)
i = 0
stack = 0
time_1 = 0
while True:
    if stack == 0:
        line_1 = f_4_1.readline()
        stack = 1
    else:
        line_1 = f_4_1.readline()
        if not line_1: break
        line_1 = re.sub("\n",'',line_1)
        test_list.append(line_1)
while True:
    line_2 = f_4_2.readline()
    if not line_2: break
    name = line_2.split(',')[0]
    name = name.strip()
    time = line_2.split(',')[1]
    time = time_sec(time)
    time = int(time)
    input_time = sec_time(time)
    i = 0
    j = 0
    add = []
    add.append(name)
    add.append(input_time)
    for i in range(2, 7):
        tol = line_2.split(',')[i]
        tol = tol.strip()
        add.append(tol)
    while i < len(test_list):
        line_1 = test_list[i]

        command = line_1.split(',')[6]
        pid = line_1.split(',')[2]

        command = command.strip()
        pid = pid.strip()
        name_cpu = command + "_" + pid
        name_cpu = name_cpu.strip()
        name = name.strip()
        if name == name_cpu :
            tol = line_1.split(',')[0]
            time_1 = time_sec(tol)
            if time-10 < time_1 and time_1 < time+10:
                tol = line_1.split(',')[1]
                add.append(tol)
                tol = line_1.split(',')[3]
                add.append(tol)
                tol = line_1.split(',')[4]
                add.append(tol)
                tol = line_1.split(',')[5]
                add.append(tol)
                del test_list[i]
                i = i - 1
                break
        i = i + 1
        if i == len(test_list):
            add.append(0)
            add.append(0)
            add.append(0)
            add.append(0)
            break
    write.writerow(add)
f_avg.close()

# 5차 처리
# mem 병합
f_5_1 = open("C:/Users/Slayer/Desktop/공유할것 (2)/NPB_log_knl02_64/NPB_EP_log/pidstat_mem/(평균)pidstat_mem_2018-08-02.csv", 'r')
f_5_2 = open("C:/Users/Slayer/Desktop/공유할것 (2)/NPB_log_knl02_64/NPB_EP_log/()작업/4차처리.csv", 'r',newline='')
f_avg = open("C:/Users/Slayer/Desktop/공유할것 (2)/NPB_log_knl02_64/NPB_EP_log/()작업/5차처리.csv", 'w',newline='')

write = csv.writer(f_avg)
test_list = []
rdr = csv.reader(f_4_1)
i = 0
stack = 0
time_1 = 0
while True:
    if stack == 0:
        line_1 = f_5_1.readline()
        stack = 1
    else:
        line_1 = f_5_1.readline()
        if not line_1: break
        line_1 = re.sub("\n",'',line_1)
        test_list.append(line_1)
while True:
    line_2 = f_5_2.readline()
    if not line_2: break
    name = line_2.split(',')[0]
    name = name.strip()
    time = line_2.split(',')[1]
    time = time_sec(time)
    time = int(time)
    input_time = sec_time(time)
    i = 0
    j = 0
    add = []
    add.append(name)
    add.append(input_time)
    for i in range(2, 11):
        tol = line_2.split(',')[i]
        tol = tol.strip()
        add.append(tol)
    while i < len(test_list):
        line_1 = test_list[i]

        command = line_1.split(',')[8]
        pid = line_1.split(',')[2]

        command = command.strip()
        pid = pid.strip()
        name_cpu = command + "_" + pid
        name_cpu = name_cpu.strip()
        name = name.strip()
        if name == name_cpu :
            tol = line_1.split(',')[0]
            time_1 = time_sec(tol)
            if time-10 < time_1 and time_1 < time+10:
                tol = line_1.split(',')[1]
                add.append(tol)
                tol = line_1.split(',')[3]
                add.append(tol)
                tol = line_1.split(',')[4]
                add.append(tol)
                tol = line_1.split(',')[5]
                add.append(tol)
                tol = line_1.split(',')[6]
                add.append(tol)
                tol = line_1.split(',')[7]
                add.append(tol)
                del test_list[i]
                i = i - 1
                break
        i = i + 1
        if i == len(test_list):
            add.append(0)
            add.append(0)
            add.append(0)
            add.append(0)
            add.append(0)
            add.append(0)
            break
    write.writerow(add)
f_avg.close()

# 6차 처리
# stack 병합
f_6_1 = open("C:/Users/Slayer/Desktop/공유할것 (2)/NPB_log_knl02_64/NPB_EP_log/pidstat_stack/(평균)pidstat_stack_2018-08-02.csv", 'r')
f_6_2 = open("C:/Users/Slayer/Desktop/공유할것 (2)/NPB_log_knl02_64/NPB_EP_log/()작업/5차처리.csv", 'r',newline='')
f_avg = open("C:/Users/Slayer/Desktop/공유할것 (2)/NPB_log_knl02_64/NPB_EP_log/()작업/6차처리.csv", 'w',newline='')

write = csv.writer(f_avg)
test_list = []
rdr = csv.reader(f_4_1)
i = 0
stack = 0
time_1 = 0
while True:
    if stack == 0:
        line_1 = f_6_1.readline()
        stack = 1
    else:
        line_1 = f_6_1.readline()
        if not line_1: break
        line_1 = re.sub("\n",'',line_1)
        test_list.append(line_1)
while True:
    line_2 = f_6_2.readline()
    if not line_2: break
    name = line_2.split(',')[0]
    name = name.strip()
    time = line_2.split(',')[1]
    time = time_sec(time)
    time = int(time)
    input_time = sec_time(time)
    i = 0
    j = 0
    add = []
    add.append(name)
    add.append(input_time)
    for i in range(2, 17):
        tol = line_2.split(',')[i]
        tol = tol.strip()
        add.append(tol)
    while i < len(test_list):
        line_1 = test_list[i]

        command = line_1.split(',')[5]
        pid = line_1.split(',')[2]

        command = command.strip()
        pid = pid.strip()
        name_cpu = command + "_" + pid
        name_cpu = name_cpu.strip()
        name = name.strip()
        if name == name_cpu :
            tol = line_1.split(',')[0]
            time_1 = time_sec(tol)
            if time-10 < time_1 and time_1 < time+10:
                tol = line_1.split(',')[1]
                add.append(tol)
                tol = line_1.split(',')[3]
                add.append(tol)
                tol = line_1.split(',')[4]
                add.append(tol)
                del test_list[i]
                i = i - 1
                break
        i = i + 1
        if i == len(test_list):
            add.append(0)
            add.append(0)
            add.append(0)
            break
    write.writerow(add)
f_avg.close()


# 7차 처리
# tswch 병합
f_7_1 = open("C:/Users/Slayer/Desktop/공유할것 (2)/NPB_log_knl02_64/NPB_EP_log/pidstat_tswch/(평균)pidstat_tswch_2018-08-02.csv", 'r')
f_7_2 = open("C:/Users/Slayer/Desktop/공유할것 (2)/NPB_log_knl02_64/NPB_EP_log/()작업/6차처리.csv", 'r',newline='')
f_avg = open("C:/Users/Slayer/Desktop/공유할것 (2)/NPB_log_knl02_64/NPB_EP_log/()작업/7차처리.csv", 'w',newline='')

write = csv.writer(f_avg)

name = ['command_pid','time	','cpu_uid','usr','system','guest','%cpu','io_uid','kb_rd/s','kb_wr/s','kb_ccwr/s',
        'mem_uid','minflt/s','majflt/s','vsz','rss','%mem','stack_uid','stksize','stkref','tswch_uid','cswch/s','nvcswch/s']
write.writerow(name)

test_list = []
rdr = csv.reader(f_4_1)
i = 0
stack = 0
time_1 = 0
while True:
    if stack == 0:
        line_1 = f_7_1.readline()
        stack = 1
    else:
        line_1 = f_7_1.readline()
        if not line_1: break
        line_1 = re.sub("\n",'',line_1)
        test_list.append(line_1)
while True:
    line_2 = f_7_2.readline()
    if not line_2: break
    name = line_2.split(',')[0]
    name = name.strip()
    time = line_2.split(',')[1]
    time = time_sec(time)
    time = int(time)
    input_time = sec_time(time)
    i = 0
    j = 0
    add = []
    add.append(name)
    add.append(input_time)
    for i in range(2, 20):
        tol = line_2.split(',')[i]
        tol = tol.strip()
        add.append(tol)
    while i < len(test_list):
        line_1 = test_list[i]

        command = line_1.split(',')[5]
        pid = line_1.split(',')[2]

        command = command.strip()
        pid = pid.strip()
        name_cpu = command + "_" + pid
        name_cpu = name_cpu.strip()
        name = name.strip()
        if name == name_cpu :
            tol = line_1.split(',')[0]
            time_1 = time_sec(tol)
            if time-10 < time_1 and time_1 < time+10:
                tol = line_1.split(',')[1]
                add.append(tol)
                tol = line_1.split(',')[3]
                add.append(tol)
                tol = line_1.split(',')[4]
                add.append(tol)
                del test_list[i]
                i = i - 1
                break
        i = i + 1
        if i == len(test_list):
            add.append(0)
            add.append(0)
            add.append(0)
            break
    write.writerow(add)
f_avg.close()
