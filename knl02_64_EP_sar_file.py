import csv
import re

f = open("C:/Users/Slayer/Desktop/공유할것/NPB_log_knl02_64/NPB_EP_log/sar_file/sar_file_2018-08-02.txt", 'r')
f_csv = open("C:/Users/Slayer/Desktop/공유할것/NPB_log_knl02_64/NPB_EP_log/sar_file/(평균제외)sar_file_2018-08-02.csv", 'w',
             newline='')
f_csv_avg = open("C:/Users/Slayer/Desktop/공유할것/NPB_log_knl02_64/NPB_EP_log/sar_file/(평균)sar_file_2018-08-02.csv", 'w',
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
    elif 'Linux 3.10.0-327.36.3.el7.x86_64 (knl02.kisti.re.kr) 	08/02/2018 	_x86_64_	(272 CPU)' in line:
        pass
    elif 'PM dentunusd   file-nr  inode-nr    pty-nr' in line:
        pass
    elif 'Average' in line:
        line_comma = split(line)
        add.append(time)
        for i in range(1,5):
            tol = line_comma.split(',')[i]
            tol = tol.strip()
            add.append(tol)
        write_avg.writerow(add)
    else:
        line_comma = split(line)
        print(line_comma)
        for i in range (0,6):
            tol = line_comma.split(',')[i]
            tol = tol.strip()
            add.append(tol)
        time = line_comma.split(',')[0]
        write.writerow(add)

