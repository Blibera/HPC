import csv
import re

f = open("C:/Users/Slayer/Desktop/공유할것/NPB_log_knl02_64/NPB_EP_log/sar_pow/sar_pow_2018-08-02.txt", 'r')
f_csv = open("C:/Users/Slayer/Desktop/공유할것/NPB_log_knl02_64/NPB_EP_log/sar_pow/sar_pow_2018-08-02.csv", 'w',
             newline='')
f_csv_avg = open("C:/Users/Slayer/Desktop/공유할것/NPB_log_knl02_64/NPB_EP_log/sar_pow/(평균)sar_pow_2018-08-02.csv", 'w',
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
    if not line: break
    if '\n' == line:
        pass
    elif 'Linux 3.10.0-327.36.3.el7.x86_64 (knl02.kisti.re.kr) 	08/02/2018 	_x86_64_	(272 CPU)' in line:
        pass
    else:
        string = string + line

count = string.count('PM    TEMP')
count_avg = string.count('Average:       TEMP      degC     %temp               DEVICE')

for i in range(1,count+1):
    add = []
    time = string.split('PM    TEMP      degC     %temp               DEVICE')[i]
    time = time.split('PM')[0]
    time = time.strip()
    split_line = string.split('PM    TEMP      degC     %temp               DEVICE')[i]
    line_comma = split(split_line)
    add.append(time)
    for j in range(1,30):
        tol = line_comma.split('PM')[j]
        for l in range(2,4):
            toll = tol.split(',')[l]
            add.append(toll)
    write.writerow(add)

for i in range(1,count_avg+1):
    add = []
    split_line = string.split('Average:       TEMP      degC     %temp               DEVICE')[i]
    split_line = split_line.split('PM')[0]
    line_comma = split(split_line)
    for j in range(1, 30):
        tol = line_comma.split('Average:')[j]
        for l in range(2, 4):
            toll = tol.split(',')[l]
            add.append(toll)
    write_avg.writerow(add)


