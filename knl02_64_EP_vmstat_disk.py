import csv
import re

f = open("C:/Users/Slayer/Desktop/공유할것/NPB_log_knl02_64/NPB_EP_log/vmstat_disk/vmstat_disk_2018-08-02.txt", 'r')
f_csv = open("C:/Users/Slayer/Desktop/공유할것/NPB_log_knl02_64/NPB_EP_log/vmstat_disk/vmstat_disk_2018-08-02.csv", 'w',
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

while True:
    line = f.readline()
    add = []
    if not line: break
    if '\n' == line:
        pass
    elif 'disk- ------------reads------------ ------------writes----------- -----IO------ -----timestamp-----' in line:
        pass
    elif 'total merged sectors' in line:
        pass
    else:
        string = string + line

sda_count = string.count('sda')
print(sda_count)

for i in range(1,sda_count+1):
    add = []
    split_line = string.split('sda')[i]

    line_comma = split(split_line)
    for k in range(1,13):
        tol = line_comma.split(',')[k]
        tol = re.sub("dm-0",'',tol)
        tol = tol.strip()
        add.append(tol)

    line_comma = line_comma.split('dm-0')[1]
    for k in range(1, 11):
        tol = line_comma.split(',')[k]
        add.append(tol)

    line_comma = line_comma.split('dm-1')[1]
    for k in range(1, 11):
        tol = line_comma.split(',')[k]
        add.append(tol)

    line_comma = line_comma.split('nvme0n1')[1]
    for k in range(1, 11):
        tol = line_comma.split(',')[k]
        add.append(tol)

    line_comma = line_comma.split('dm-2')[1]
    for k in range(1, 11):
        tol = line_comma.split(',')[k]
        add.append(tol)
    write.writerow(add)

