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

name = ['sda_total','sda_reads_merged','sda_reads_sectors','sda_writes_ms','sda_writes_total','sda_writes_merged','sda_writes_sectors','sda_io_ms','sda_io_cur','sda_io_sec','day','time',
        'dm-0_total','dm-0_reads_merged','dm-0_reads_sectors','dm-0_writes_ms','dm-0_writes_total','dm-0_writes_merged','dm-0_writes_sectors','dm-0_io_ms','dm-0_io_cur','dm-0_io_sec',
        'dm-1_total', 'dm-1_reads_merged', 'dm-1_reads_sectors', 'dm-1_writes_ms', 'dm-1_writes_total', 'dm-1_writes_merged','dm-1_writes_sectors', 'dm-1_io_ms', 'dm-1_io_cur', 'dm-1_io_sec',
        'nvme0n1_total', 'nvme0n1_reads_merged', 'nvme0n1_reads_sectors', 'nvme0n1_writes_ms', 'nvme0n1_writes_total', 'nvme0n1_writes_merged','nvme0n1_writes_sectors', 'nvme0n1_io_ms', 'nvme0n1_io_cur', 'nvme0n1_io_sec',
        'dm-2_sda_total', 'dm-2_reads_merged', 'dm-2_reads_sectors', 'dm-2_writes_ms', 'dm-2_writes_total', 'dm-2_writes_merged','dm-2_writes_sectors', 'dm-2_io_ms', 'dm-2_io_cur', 'dm-2_io_sec']

write.writerow(name)

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

