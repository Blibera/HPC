import csv
import re
f = open("C:/Users/Slayer/Desktop/공유할것 (2)/NPB_log_knl02_64/NPB_EP_log/pidstat_tswch/(평균)pidstat_tswch_2018-08-02.csv", 'r')
f_1 = open("C:/Users/Slayer/Desktop/공유할것 (2)/NPB_log_knl02_64/NPB_EP_log/1차처리.csv", 'w',newline='')

write = csv.writer(f_1)

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

# 1차 처리
# command_pid 형식으로 만들기

while True:
    add= []
    line = f.readline()
    if not line: break
    command = line.split(',')[5]
    pid = line.split(',')[2]
    command = command.strip()
    pid = pid.strip()
    name = command + "_" + pid
    add.append(name)
    pass
    write.writerow(add)
f_1.close()
# 2차 처리
# 중복제거 및 command_pid를 sort

f_2 = open("C:/Users/Slayer/Desktop/공유할것 (2)/NPB_log_knl02_64/NPB_EP_log/1차처리.csv", 'r')
f_avg = open("C:/Users/Slayer/Desktop/공유할것 (2)/NPB_log_knl02_64/NPB_EP_log/2차처리.csv", 'w',newline='')
write = csv.writer(f_avg)
add = []

while True:
    line = f_2.readline()
    if not line: break
    tol = re.sub("\r\n",'',line)
    add.append(tol)
add = list(set(add))
nn = len(add)
add.sort()

for i in range (0,nn):
    tol = []
    ad = add[i]
    ad = ad.strip()
    tol.append(ad)
    write.writerow(tol)



# 3차 처리
# pidstat_tswch 합병
f_3_1 = open("C:/Users/Slayer/Desktop/공유할것 (2)/NPB_log_knl02_64/NPB_EP_log/pidstat_tswch/(평균)pidstat_tswch_2018-08-02.csv", 'r')
f_3_2 = open("C:/Users/Slayer/Desktop/공유할것 (2)/NPB_log_knl02_64/NPB_EP_log/2차처리.csv", 'r')
f_avg = open("C:/Users/Slayer/Desktop/공유할것 (2)/NPB_log_knl02_64/NPB_EP_log/3차처리.csv", 'w',newline='')
write = csv.writer(f_avg)

test_list = []
rdr = csv.reader(f_3_1)
i = 0
stack = 0
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
    name = line_2
    name = name.strip()
    i = 0
    j = 0
    while i < len(test_list):
        add = []
        line_1 = test_list[i]

        command = line_1.split(',')[5]
        pid = line_1.split(',')[2]

        command = command.strip()
        pid = pid.strip()
        name_tswch = command + "_" + pid
        name_tswch = name_tswch.strip()
        name = name.strip()
        if name == name_tswch:
            add.append(name)
            tol = line_1.split(',')[0]
            add.append(tol)
            tol = line_1.split(',')[1]
            add.append(tol)
            tol = line_1.split(',')[3]
            add.append(tol)
            tol = line_1.split(',')[4]
            add.append(tol)
            del test_list[i]
            write.writerow(add)
            i = i - 1
        i = i + 1
f_3_1.close()
f_3_2.close()
f_avg.close()

# 4차 처리
f_4_1 = open("C:/Users/Slayer/Desktop/공유할것 (2)/NPB_log_knl02_64/NPB_EP_log/pidstat_stack/(평균)pidstat_stack_2018-08-02.csv", 'r')
f_4_2 = open("C:/Users/Slayer/Desktop/공유할것 (2)/NPB_log_knl02_64/NPB_EP_log/3차처리.csv", 'r',newline='')
f_avg = open("C:/Users/Slayer/Desktop/공유할것 (2)/NPB_log_knl02_64/NPB_EP_log/4차처리.csv", 'w',newline='')

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
    i = 0
    j = 0
    add = []

    add.append(name)
    tol = line_2.split(',')[1]
    add.append(tol)
    tol = line_2.split(',')[2]
    add.append(tol)
    tol = line_2.split(',')[3]
    add.append(tol)
    tol = line_2.split(',')[4]
    tol = tol.strip()
    add.append(tol)
    while i < len(test_list):
        line_1 = test_list[i]

        command = line_1.split(',')[5]
        pid = line_1.split(',')[2]

        command = command.strip()
        pid = pid.strip()
        name_tswch = command + "_" + pid
        name_tswch = name_tswch.strip()
        name = name.strip()
        if name == name_tswch :
            print(line_1)
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


f_4_1.close()
f_4_2.close()
f_avg.close()