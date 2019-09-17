import csv
import re

f = open("C:/Users/Slayer/Desktop/공유할것/NPB_log_knl02_64/NPB_EP_log/iostat/iostat_2018-08-02.txt", 'r')
f_csv = open("C:/Users/Slayer/Desktop/공유할것/NPB_log_knl02_64/NPB_EP_log/iostat/iostat_2018-08-02.csv",'w',newline='')
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
    if not line: break

    # 08/02/2018수를 세서 해당 줄을 하나의 묶음으로 관리하기 위해서
    string = string + line

count = string.count('08/02/2018')
write = csv.writer(f_csv)

for i in range(2,count+1):
    add = []
    split_line = string.split('08/02/2018')[i]
    line_comma = split(split_line)
    time = split_line.split('PM')[0]
    time = time.strip()
    add.append(time)

    sda_find = line_comma.find('dm-2')

    if '_x86_64_	(272 CPU)' in add:
        pass
    elif sda_find == -1:
        write.writerow(add)
    else:
        for k in range(1, 14):
            tol = line_comma.split('dm-2')[1]
            tol = tol.split(',')[k]
            tol = re.sub('Linux', '', tol)
            tol = tol.strip()
            add.append(tol)
        add.append(1)
        write.writerow(add)
f.close()
f_csv.close()

"""

# avg-cpu
add = []
    split_line = string.split('08/02/2018')[i]
    line_comma = split(split_line)
    time = split_line.split('PM')[0]
    time = time.strip()
    add.append(time)

    for k in range(9, 15):
        try:
            tol = line_comma.split(',')[k]
            tol = re.sub("Device:","",tol)
            tol = tol.strip()
            add.append(tol)
        except:
            pass
    if '_x86_64_	(272 CPU)' in add:
        pass
    else:
        add.append(1)
        write.writerow(add)

# sda
add = []
    split_line = string.split('08/02/2018')[i]
    line_comma = split(split_line)
    time = split_line.split('PM')[0]
    time = time.strip()
    add.append(time)

    sda_find = line_comma.find('sda')

    if '_x86_64_	(272 CPU)' in add:
        pass
    elif sda_find == -1:
        write.writerow(add)
    else:
        for k in range(1,14):
            tol = line_comma.split('sda')[1]
            tol = tol.split(',')[k]
            tol = re.sub('dm-0', '', tol)
            tol = re.sub('dm-1', '', tol)
            tol = re.sub('dm-2', '', tol)
            tol = re.sub('nvme0n1', '', tol)
            tol = tol.strip()
            add.append(tol)
        add.append(1)
        write.writerow(add)

# dm-0
add = []
    split_line = string.split('08/02/2018')[i]
    line_comma = split(split_line)
    time = split_line.split('PM')[0]
    time = time.strip()
    add.append(time)

    sda_find = line_comma.find('dm-0')

    if '_x86_64_	(272 CPU)' in add:
        pass
    elif sda_find == -1:
        write.writerow(add)
    else:
        for k in range(1,14):
            tol = line_comma.split('dm-0')[1]
            tol = tol.split(',')[k]
            tol = re.sub('dm-1', '', tol)
            tol = re.sub('dm-2', '', tol)
            tol = re.sub('nvme0n1', '', tol)
            tol = tol.strip()
            add.append(tol)
        add.append(1)
        write.writerow(add)
        
# dm-1
add = []
    split_line = string.split('08/02/2018')[i]
    line_comma = split(split_line)
    time = split_line.split('PM')[0]
    time = time.strip()
    add.append(time)

    sda_find = line_comma.find('dm-1')

    if '_x86_64_	(272 CPU)' in add:
        pass
    elif sda_find == -1:
        write.writerow(add)
    else:
        for k in range(1,14):
            tol = line_comma.split('dm-1')[1]
            tol = tol.split(',')[k]
            tol = re.sub('dm-2', '', tol)
            tol = re.sub('nvme0n1', '', tol)
            tol = tol.strip()
            add.append(tol)
        add.append(1)
        write.writerow(add)
       
# dm-2 
add = []
    split_line = string.split('08/02/2018')[i]
    line_comma = split(split_line)
    time = split_line.split('PM')[0]
    time = time.strip()
    add.append(time)

    sda_find = line_comma.find('dm-2')

    if '_x86_64_	(272 CPU)' in add:
        pass
    elif sda_find == -1:
        write.writerow(add)
    else:
        for k in range(1, 14):
            tol = line_comma.split('dm-2')[1]
            tol = tol.split(',')[k]
            tol = re.sub('Linux', '', tol)
            tol = tol.strip()
            add.append(tol)
        add.append(1)
        write.writerow(add)
        
"""