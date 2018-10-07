import csv
import re

f = open("C:/Users/Slayer/Desktop/공유할것/NPB_log_knl02_64/NPB_EP_log/iostat/iostat_2018-08-02.txt", 'r')
f_csv = open("C:/Users/Slayer/Desktop/공유할것/NPB_log_knl02_64/NPB_EP_log/iostat/iostat_2018-08-02.csv",'w',newline='')
# 변수
stack = 0
row = []
b = []
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

write = csv.writer(f_csv)
write.writerow(row)
while True:
    line = f.readline()
    if not line: break

    if stack == 0:
        stack = stack + 1

    elif stack == 1:
        tol = split(str(line))
        print(tol)
        for j in range (1,10):
            b = tol.split(',')[j]
            row.append(b)
        stack = stack + 1
    elif stack == 2 :
        line = split(str(line))
        for k in range (1,6):
            b = line.split(',')[k]
            row.append(b)
        stack = stack + 1
    elif stack == 3 :
        line = split(str(line))
        for l in range (1,6):
            b = line.split(',')[l]
            row.append(b)
        stack = stack + 1
    else:
        write.writerow(row)
        row = []
        stack = 0

f.close()
f_csv.close()