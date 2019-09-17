import csv
import re

f = open("C:/Users/Slayer/Desktop/공유할것/NPB_log_knl02_64/NPB_EP_log/pidstat_io/pidstat_io_2018-08-02.txt", 'r')
f_csv = open("C:/Users/Slayer/Desktop/공유할것/NPB_log_knl02_64/NPB_EP_log/pidstat_io/pidstat_io_2018-08-02.csv",'w',newline='')
# 변수
stack = 0
string = ""
add = []

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

name = ['time','uid','pid','stksize','stkref','command']
write = csv.writer(f_csv)
write.writerow(name)

while True:
    line = f.readline()
    if not line: break
    string = string + line

count = string.count('PM   UID       PID   kB_rd/s   kB_wr/s kB_ccwr/s  Command')

for i in range(1,count+1):
    time = string.split('PM   UID       PID   kB_rd/s   kB_wr/s kB_ccwr/s  Command')[i]
    time = time.split('PM')[0]
    time = time.strip()
    split_line = string.split('PM   UID       PID   kB_rd/s   kB_wr/s kB_ccwr/s  Command')[i]
    print(split_line)
    avg_count = split_line.count('PM')
    line_comma = split(split_line)
    for k in range(1, avg_count + 1):
        add = []
        add.append(time)
        one_line = line_comma.split('PM')[k]
        for l in range(1, 7):
            tol = one_line.split(',')[l]
            tol = re.sub(time, '', tol)
            tol = re.sub('Average:', '', tol)
            tol = re.sub("Linux",'',tol)
            tol = tol.strip()
            add.append(tol)
        write.writerow(add)

"""
# 모든값 추출
count = string.count('PM   UID       PID   kB_rd/s   kB_wr/s kB_ccwr/s  Command')

for i in range(1,count+1):
    time = string.split('PM   UID       PID   kB_rd/s   kB_wr/s kB_ccwr/s  Command')[i]
    time = time.split('PM')[0]
    time = time.strip()
    split_line = string.split('PM   UID       PID   kB_rd/s   kB_wr/s kB_ccwr/s  Command')[i]
    print(split_line)
    avg_count = split_line.count('PM')
    line_comma = split(split_line)
    for k in range(1, avg_count + 1):
        add = []
        add.append(time)
        one_line = line_comma.split('PM')[k]
        for l in range(1, 7):
            tol = one_line.split(',')[l]
            tol = re.sub(time, '', tol)
            tol = re.sub('Average:', '', tol)            
            tol = tol.strip()
            add.append(tol)
        write.writerow(add)
        
# avg추출

count = string.count('UID       PID   kB_rd/s   kB_wr/s kB_ccwr/s  Command')

for i in range(0,count):
    time = string.split('Average:      UID       PID    %usr %system  %guest    %CPU   CPU  Command')[i]
    time = time.split('Command')[1]
    time = time.split('PM')[0]
    time = time.strip()
    split_line = string.split('Average:      UID')[i+1]
    print(split_line)
    avg_count = split_line.count('Average:')
    line_comma = split(split_line)
    for k in range(1, avg_count + 1):
        add = []
        add.append(time)
        one_line = line_comma.split('Average:')[k]
        for l in range(1, 9):
            if l == 7:
                pass
            else:
                tol = one_line.split(',')[l]
                tol = tol.strip()
                add.append(tol)
        write.writerow(add)

"""