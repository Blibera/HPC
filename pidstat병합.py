import csv
import re
f = open("C:/Users/Slayer/Desktop/공유할것/NPB_log_knl02_64/NPB_EP_log/pidstat_tswch/(평균)pidstat_tswch_2018-08-02.csv", 'r')
f_1 = open("C:/Users/Slayer/Desktop/공유할것/NPB_log_knl02_64/NPB_EP_log/1차처리.csv", 'w',newline='')

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

# 2차 처리
# 중복제거 및 command_pid를 sort

f_2 = open("C:/Users/Slayer/Desktop/공유할것/NPB_log_knl02_64/NPB_EP_log/1차처리.csv", 'r')
f_avg = open("C:/Users/Slayer/Desktop/공유할것/NPB_log_knl02_64/NPB_EP_log/2차처리.csv", 'w',newline='')
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
f_3_1 = open("C:/Users/Slayer/Desktop/공유할것/NPB_log_knl02_64/NPB_EP_log/pidstat_tswch/(평균)pidstat_tswch_2018-08-02.csv", 'r')
f_3_2 = open("C:/Users/Slayer/Desktop/공유할것/NPB_log_knl02_64/NPB_EP_log/2차처리.csv", 'r')
f_avg = open("C:/Users/Slayer/Desktop/공유할것/NPB_log_knl02_64/NPB_EP_log/3차처리.csv", 'w',newline='')
write = csv.writer(f_avg)
while True:
    line_2 = f_3_2.readline()
    if not line_2: break
    name = line_2
    name = name.strip()
    rdr = csv.reader(f_3_1)
    print("수행")
    line_1 = []
    for line_1 in rdr:
        add = []
        if not line_1: break
        command = line_1[5]
        pid = line_1[2]
        command = command.strip()
        pid = pid.strip()
        name_tswch = command + "_" + pid
        name_tswch = name_tswch.strip()
        if name == name_tswch:
            add.append(name)
            tol = line_1[0]
            add.append(tol)
            tol = line_1[1]
            add.append(tol)
            tol = line_1[3]
            add.append(tol)
            tol = line_1[4]
            add.append(tol)
            write.writerow(add)





f_1.close()
f_avg.close()