import csv
import re

f = open("C:/Users/Slayer/Desktop/공유할것/NPB_log_knl02_64/NPB_EP_log/free/free_2018-08-02.txt", 'r')
f_csv = open("C:/Users/Slayer/Desktop/공유할것/NPB_log_knl02_64/NPB_EP_log/free/free.csv",'w',newline='')
f_avg = open("C:/Users/Slayer/Desktop/공유할것/NPB_log_knl02_64/NPB_EP_log/free_avg.csv",'w',newline='')
# 변수
stack = 0
row = []
b = []
loop_12 = 0
time_before = ""
def split(text):
    cleaned_text = re.sub('              ', ',', text)
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
name = ['mem_used','mem_free','mem_shard','mem_buff','mem_cache','mem_available','swap_used','swap_free','swap_shard','total_used','total_free','total_shard','day','time']

write = csv.writer(f_csv)
write.writerow(name)
write_avg = csv.writer(f_avg)

while True:
    line = f.readline()
    if not line: break

    if stack == 0:
        stack = stack + 1

    elif stack == 1:
        tol = split(str(line))
        for j in range (1,7):
            b = tol.split(',')[j]
            b = b.strip()
            row.append(b)
        stack = stack + 1
    elif stack == 2 :
        line = split(str(line))
        for k in range (1,4):
            b = line.split(',')[k]
            b = b.strip()
            row.append(b)
        stack = stack + 1
    elif stack == 3 :
        line = split(str(line))
        for l in range (1,7):
            if l == 4:
                pass
            else:
                b = line.split(',')[l]
                b = b.strip()
                row.append(b)
            if l == 6:
                time = line.split(',')[6]
        stack = stack + 1
    else:
        if time_before == time:
            time_before = time
            pass
        else:
            write.writerow(row)
            time_before = time
        row = []
        stack = 0
f_csv.close()
f_free = open("C:/Users/Slayer/Desktop/공유할것/NPB_log_knl02_64/NPB_EP_log/free/free.csv",'r',newline='')
add = []
stack = 0

op = 0
while True:
    line_free = f_free.readline()
    print(line_free)
    if not line_free: break
    comma_count_free = line_free.count(',')
    if stack == 0 :
        for i in range(0,comma_count_free+1):
            tol = line_free.split(',')[i]
            tol = tol.strip()
            add.append(tol)
        write_avg.writerow(add)
        stack = stack + 1
        add = []
    else:
        if loop_12 == 12:
            print("수행")
            for i in range(0, 11):
                add[i] = add[i]/12
                add[i] = round(add[i],3)
            day = day.strip()
            time = time.strip()
            add.append(day)
            add.append(time)
            write_avg.writerow(add)
            loop_12 = 0
            add = []
            loop_12 = loop_12 + 1
            for i in range(0,14):
                if i == 12:
                    day = line_free.split(',')[12]
                    day = day.strip()
                elif i == 13:
                    time = line_free.split(',')[13]
                    time = time.strip()
                else:
                    tol = line_free.split(',')[i]
                    tol = int(tol)
                    add.append(tol)

        elif loop_12 == 0:
            for i in range(0,14):
                if i == 12:
                    day = line_free.split(',')[12]
                    day = day.strip()
                elif i == 13:
                    time = line_free.split(',')[13]
                    time = time.strip()
                else:
                    tol = line_free.split(',')[i]
                    tol = int(tol)
                    add.append(tol)


            loop_12 = loop_12 + 1

        else:
            for i in range(0, 11):
                tol = line_free.split(',')[i]
                tol = int(tol)
                add[i] = add[i] + tol
            loop_12 = loop_12 + 1
    op = op + 1


f.close()
f_free.close()
f_avg.close()