import csv
import re

f = open("C:/Users/Slayer/Desktop/공유할것/NPB_log_knl02_64/NPB_EP_log/sar_bdev/sar_bdev_2018-08-02.txt", 'r')
f_csv = open("C:/Users/Slayer/Desktop/공유할것/NPB_log_knl02_64/NPB_EP_log/sar_bdev/(평균제외)sar_bdev_2018-08-02.csv", 'w',
             newline='')
f_csv_avg = open("C:/Users/Slayer/Desktop/공유할것/NPB_log_knl02_64/NPB_EP_log/sar_bdev/(평균)sar_bdev_2018-08-02.csv", 'w',
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


write = csv.writer(f_csv)
write_avg = csv.writer(f_csv_avg)

while True:
    line = f.readline()
    add = []
    if not line: break

    if '\n' == line:
        pass
    else:
        string = string + line

count_pm = string.count('PM       DEV       tps  rd_sec/s  wr_sec/s')
print(count_pm)
count_avg = string.count('Average:          DEV       tps  rd_sec/s  wr_sec/s')
print(count_avg)

for i in range(1, count_pm):
    add = []
    time = string.split('PM       DEV       tps  rd_sec/s  wr_sec/s')[i]
    time = time.split('%util')[1]
    time = time.split('PM')[0]
    time = time.strip()
    split_line = string.split('PM       DEV       tps  rd_sec/s  wr_sec/s')[i]
    avg_count = split_line.count('PM')
    line_comma = split(split_line)
    add.append(time)
    for k in range(1, avg_count + 1):
        one_line = line_comma.split('PM')[k]
        for l in range(2, 10):
            tol = one_line.split(',')[l]
            tol = re.sub('Linux', '', tol)
            tol = re.sub(time, '', tol)
            tol = re.sub('Average:', '', tol)
            tol = tol.strip()
            add.append(tol)
    write.writerow(add)

for i_i in range(0, count_avg+1):
    add = []
    time = string.split('Linux 3.10.0-327.36.3.el7.x86_64 (knl02.kisti.re.kr) 	08/02/2018 	_x86_64_	(272 CPU)')[i_i]
    time = time.split('PM')[0]
    time = time.strip()
    print(time)
    print("=============")
    split_line = string.split('Average:          DEV')[i_i]
    avg_count = split_line.count('Average:')
    line_comma = split(split_line)
    add.append(time)
    for k_k in range(1, avg_count + 1):
        one_line = line_comma.split('Average:')[k_k]
        for l_l in range(2,10):
            tol = one_line.split(',')[l_l]
            tol = re.sub('Linux', '', tol)
            tol = tol.strip()
            add.append(tol)
    write_avg.writerow(add)
