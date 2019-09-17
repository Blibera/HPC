import csv
import re

f = open("C:/Users/Slayer/Desktop/공유할것/NPB_log_knl02_64/NPB_EP_log/pidstat_mem/pidstat_mem_2018-08-02.txt", 'r')
f_csv = open("C:/Users/Slayer/Desktop/공유할것/NPB_log_knl02_64/NPB_EP_log/pidstat_mem/pidstat_mem_2018-08-02.csv", 'w',
             newline='')
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

count = string.count('PM   UID       PID  minflt/s  majflt/s     VSZ    RSS   %MEM  Command')
print(count)
for i in range(1, count+1):
    time = string.split('PM   UID       PID  minflt/s  majflt/s     VSZ    RSS   %MEM  Command')[i]
    time = time.split('PM')[0]
    time = time.strip()
    split_line = string.split('PM   UID       PID  minflt/s  majflt/s     VSZ    RSS   %MEM  Command')[i]
    print(time)
    avg_count = split_line.count('PM')
    line_comma = split(split_line)
    print(avg_count)
    for k in range(1, avg_count + 1):
        add = []
        add.append(time)
        one_line = line_comma.split('PM')[k]
        for l in range(1, 9):
            tol = one_line.split(',')[l]
            tol = re.sub('Linux', '', tol)
            tol = re.sub(time, '', tol)
            tol = re.sub('Average:', '', tol)
            tol = tol.strip()
            add.append(tol)
        write.writerow(add)

"""
# 모든값 추출
count = string.count('PM   UID       PID  minflt/s  majflt/s     VSZ    RSS   %MEM  Command')
print(count)
for i in range(1, count+1):
    time = string.split('PM   UID       PID  minflt/s  majflt/s     VSZ    RSS   %MEM  Command')[i]
    time = time.split('PM')[0]
    time = time.strip()
    split_line = string.split('PM   UID       PID  minflt/s  majflt/s     VSZ    RSS   %MEM  Command')[i]
    print(time)
    avg_count = split_line.count('PM')
    line_comma = split(split_line)
    print(avg_count)
    for k in range(1, avg_count + 1):
        add = []
        add.append(time)
        one_line = line_comma.split('PM')[k]
        for l in range(1, 9):
            tol = one_line.split(',')[l]
            tol = re.sub('Linux', '', tol)
            tol = re.sub(time, '', tol)
            tol = re.sub('Average:', '', tol)
            tol = tol.strip()
            add.append(tol)
        write.writerow(add)

# avg추출

count = string.count('Average:      UID       PID  minflt/s  majflt/s     VSZ    RSS   %MEM  Command')
print(count)
for i in range(0, count):
    time = string.split('Average:      UID       PID  minflt/s  majflt/s     VSZ    RSS   %MEM  Command')[i]
    time = time.split('PM')[0]
    time = time.strip()
    split_line = string.split('Average:      UID')[i+1]
    print(time)
    avg_count = split_line.count('Average:')
    line_comma = split(split_line)
    print(avg_count)
    for k in range(1, avg_count + 1):
        add = []
        add.append(time)
        one_line = line_comma.split('Average:')[k]
        for l in range(1, 9):
            tol = one_line.split(',')[l]
            tol = re.sub('Linux', '', tol)
            tol = re.sub(time, '', tol)
            tol = re.sub('Average:', '', tol)
            tol = tol.strip()
            add.append(tol)
        write.writerow(add)

"""