import csv
import re
f = open("C:/Users/Slayer/Desktop/공유할것/NPB_log_knl02_64/NPB_EP_log/iostat/iostat_2018-08-02.txt", 'r')
f_avg = open("C:/Users/Slayer/Desktop/공유할것/NPB_log_knl02_64/NPB_EP_log/iostat/iostat_2018-08-02.csv", 'w',newline='')
"""
name = ['time','<-----------------------------avg-cpu------------------------->','','','','','','<--------------------------------------------------------------------------sda------------------------------------------------------------------------>','','','','','','','','','','','','','<--------------------------------------------------------------------------dm-0------------------------------------------------------------------------>','','','','','','','','','','','','','<--------------------------------------------------------------------------dm-1------------------------------------------------------------------------>','','','','','','','','','','','','','<----------------------------------------------------------------------nvme0n1--------------------------------------------------------------------->','','','','','','','','','','','','','<--------------------------------------------------------------------------dm-2------------------------------------------------------------------------>']
name_2 = ['time','cpu_user','cpu_nice','cpu_system','cpu_iowait','cpu_wait','cpu_idle',
          '1_rrqm/s','1_wrqm/s','1_r/s','1_w/s','1_rkb/s','1_wkb/s','1_avgrq-sz','1_avgqu-sz','1_await','1_r_await','1_w_await','1_svctm','1_util',
          '2_rrqm/s','2_wrqm/s','2_r/s','2_w/s','2_rkb/s','2_wkb/s','2_avgrq-sz','2_avgqu-sz','2_await','2_r_await','2_w_await','2_svctm','2_util',
          '3_rrqm/s','3_wrqm/s','3_r/s','3_w/s','3_rkb/s','3_wkb/s','3_avgrq-sz','3_avgqu-sz','3_await','3_r_await','3_w_await','3_svctm','3_util',
          '4_rrqm/s','4_wrqm/s','4_r/s','4_w/s','4_rkb/s','4_wkb/s','4_avgrq-sz','4_avgqu-sz','4_await','4_r_await','4_w_await','4_svctm','4_util',
          '5_rrqm/s','5_wrqm/s','5_r/s','5_w/s','5_rkb/s','5_wkb/s','5_avgrq-sz','5_avgqu-sz','5_await','5_r_await','5_w_await','5_svctm','5_util']
write = csv.writer(f_avg)
write.writerow(name)
write.writerow(name_2)
"""
write = csv.writer(f_avg)
# 변수
stack = 0
string = ""
add = []
loop_12 = 0
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

while True:
    line = f.readline()
    if not line: break

    # 08/02/2018수를 세서 해당 줄을 하나의 묶음으로 관리하기 위해서
    string = string + line

count = string.count('08/02/2018')
for i in range(2, count + 1):
    add = []
    split_line = string.split('08/02/2018')[i]
    line_comma = split(split_line)
    time = split_line.split('PM')[0]
    time = time.strip()
    add.append(time)
    i = 1
    if '_x86_64_' in line_comma:
        pass
    else:
        if loop_12 == 0:
            for k in range(9, 15):
                tol = line_comma.split(',')[k]
                tol = re.sub("Device:", "", tol)
                tol = tol.strip()
                tol = float(tol)
                add.append(tol)
            for k in range(1, 14):
                try:
                    tol = line_comma.split('sda')[1]
                    tol = tol.split(',')[k]
                    tol = re.sub('dm-0', '', tol)
                    tol = re.sub('dm-1', '', tol)
                    tol = re.sub('dm-2', '', tol)
                    tol = re.sub('nvme0n1', '', tol)
                    tol = re.sub('Linux', '', tol)
                    tol = tol.strip()
                    tol = float(tol)
                except:
                    tol = 0
                add.append(tol)
            for k in range(1, 14):
                try:
                    tol = line_comma.split('dm-0')[1]
                    tol = tol.split(',')[k]
                    tol = re.sub('dm-1', '', tol)
                    tol = re.sub('dm-2', '', tol)
                    tol = re.sub('nvme0n1', '', tol)
                    tol = re.sub('Linux', '', tol)
                    tol = tol.strip()
                    tol = float(tol)
                except:
                    tol = 0
                add.append(tol)
            for k in range(1, 14):
                try:
                    tol = line_comma.split('dm-1')[1]
                    tol = tol.split(',')[k]
                    tol = re.sub('dm-2', '', tol)
                    tol = re.sub('nvme0n1', '', tol)
                    tol = re.sub('Linux', '', tol)
                    tol = tol.strip()
                    tol = float(tol)
                except:
                    tol = 0
                add.append(tol)
            for k in range(1, 14):
                try:
                    tol = line_comma.split('nvme0n1')[1]
                    tol = tol.split(',')[k]
                    tol = re.sub('dm-2', '', tol)
                    tol = re.sub('Linux', '', tol)
                    tol = tol.strip()
                    tol = float(tol)
                except:
                    tol = 0
                add.append(tol)
            for k in range(1, 14):
                try:
                    tol = line_comma.split('dm-2')[1]
                    tol = tol.split(',')[k]
                    tol = re.sub('Linux', '', tol)
                    tol = tol.strip()
                    tol = float(tol)
                except:
                    tol = 0
                add.append(tol)
        write.writerow(add)
f_avg.close()

f = open("C:/Users/Slayer/Desktop/공유할것/NPB_log_knl02_64/NPB_EP_log/iostat/iostat_2018-08-02.csv", 'r')
f_avg = open("C:/Users/Slayer/Desktop/공유할것/NPB_log_knl02_64/NPB_EP_log/iostat.csv", 'w', newline='')
name = ['time','<-----------------------------avg-cpu------------------------->','','','','','','<--------------------------------------------------------------------------sda------------------------------------------------------------------------>','','','','','','','','','','','','','<--------------------------------------------------------------------------dm-0------------------------------------------------------------------------>','','','','','','','','','','','','','<--------------------------------------------------------------------------dm-1------------------------------------------------------------------------>','','','','','','','','','','','','','<----------------------------------------------------------------------nvme0n1--------------------------------------------------------------------->','','','','','','','','','','','','','<--------------------------------------------------------------------------dm-2------------------------------------------------------------------------>']
name_2 = ['time','cpu_user','cpu_nice','cpu_system','cpu_iowait','cpu_wait','cpu_idle',
          '1_rrqm/s','1_wrqm/s','1_r/s','1_w/s','1_rkb/s','1_wkb/s','1_avgrq-sz','1_avgqu-sz','1_await','1_r_await','1_w_await','1_svctm','1_util',
          '2_rrqm/s','2_wrqm/s','2_r/s','2_w/s','2_rkb/s','2_wkb/s','2_avgrq-sz','2_avgqu-sz','2_await','2_r_await','2_w_await','2_svctm','2_util',
          '3_rrqm/s','3_wrqm/s','3_r/s','3_w/s','3_rkb/s','3_wkb/s','3_avgrq-sz','3_avgqu-sz','3_await','3_r_await','3_w_await','3_svctm','3_util',
          '4_rrqm/s','4_wrqm/s','4_r/s','4_w/s','4_rkb/s','4_wkb/s','4_avgrq-sz','4_avgqu-sz','4_await','4_r_await','4_w_await','4_svctm','4_util',
          '5_rrqm/s','5_wrqm/s','5_r/s','5_w/s','5_rkb/s','5_wkb/s','5_avgrq-sz','5_avgqu-sz','5_await','5_r_await','5_w_await','5_svctm','5_util']
write = csv.writer(f_avg)
write.writerow(name)
write.writerow(name_2)


before_time = ""
time = ""
write_time = []
add = []
while True:
    line_free = f.readline()
    if not line_free: break
    count = line_free.count(',')
    time = line_free.split(',')[0]
    if before_time == time:
        pass
    else:
        before_time = time
        if loop_12 == 0:
            for i in range (1,72):
                tol = line_free.split(',')[i]
                tol = float(tol)
                add.append(tol)
            loop_12 = loop_12 + 1
        elif loop_12 == 12:
            write_time.append(time)
            for i in range(0,71):
                add[i] = add[i]/3
                add[i] = round(add[i],5)
                write_time.append(add[i])

            write.writerow(write_time)
            add = []
            write_time = []
            loop_12 = 1
            for i in range (1,72):
                tol = line_free.split(',')[i]
                tol = float(tol)
                add.append(tol)
        else:
            for i in range (1,72):
                tol = line_free.split(',')[i]
                tol = float(tol)
                add[i-1] = add[i-1] + tol
            loop_12 = loop_12 + 1


f_avg.close()