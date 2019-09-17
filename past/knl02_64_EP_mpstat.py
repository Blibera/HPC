import csv
import re

f = open("C:/Users/Slayer/Desktop/공유할것/NPB_log_knl02_64/NPB_EP_log/mpstat/mpstat_2018-08-02.txt", 'r')
f_csv = open("C:/Users/Slayer/Desktop/공유할것/NPB_log_knl02_64/NPB_EP_log/mpstat/(short)mpstat_2018-08-02.csv", 'w',
             newline='')
f_csv_avg = open("C:/Users/Slayer/Desktop/공유할것/NPB_log_knl02_64/NPB_EP_log/mpstat/(middle)mpstat_2018-08-02.csv", 'w',
             newline='')
f_csv_avg_avg = open("C:/Users/Slayer/Desktop/공유할것/NPB_log_knl02_64/NPB_EP_log/mpstat/(long)mpstat_2018-08-02.csv", 'w',
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
write_avg_avg = csv.writer(f_csv_avg_avg)
kl = 0
while True:
    line = f.readline()
    add = []
    if not line: break

    if '\n' == line:
        pass
    elif 'PMI' in line:
        string = string + line
    elif 'PM  CPU    %usr   %nice    %sys %iowait    %irq   %soft  %steal  %guest  %gnice   %idle' in line:
        kl = kl + 1
    elif 'PM' in line:
        pass
    else:
        string = string + line
print(kl)
count_short = string.count('Average:     CPU    intr/s')
print(count_short)
count_middle = string.count('PM  CPU    %usr   %nice    %sys %iowait    %irq   %soft  %steal  %guest  %gnice   %idle')
print(count_middle)
count_long = string.count('Average:     CPU        0/s        8/s        ')
print(count_long)