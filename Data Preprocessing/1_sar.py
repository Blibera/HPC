import csv
import re

name = ["proc/s","cswch/s","pswpin/s","pswpout/","tps","rtps","wtps","bread/s","bwrtn/s"]
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
stack = 0
add = []
stack_1 = 0
stack_2 = 0
stack_3 = 0


for l in range(1,2):

    node = str(l).zfill(2)
    new_name = []
    print(len(name))
    for i in range(len(name)):
        tol = "sar" + node + "_" + name[i]
        new_name.append(tol)
    f = open("C:/Users/Slayer/Desktop/원본 데이터/knl 싱글노드/knl_sar.txt", 'r', encoding='UTF8')
    ff = open("C:/Users/Slayer/Desktop/원본 데이터/knl 싱글노드/1차 전처리/knl_sar.csv", "w",newline='')

    write = csv.writer(ff)
    write.writerow(new_name)
    while True:
        line = f.readline()
        if not line: break

        if stack_1 == 1:
            line = split(line)
            for i in range(3, 5):
                tol = line.split(',')[i]
                tol = re.sub('\n', '', tol)
                tol = float(tol)
                add.append(tol)
            stack_1 = 0

        elif stack_2 == 1:
            line = split(line)
            for i in range(3, 5):
                tol = line.split(',')[i]
                tol = re.sub('\n', '', tol)
                tol = float(tol)
                add.append(tol)
            stack_2 = 0

        elif stack_3 == 1:
            line = split(line)
            print(line)
            for i in range(3, 8):
                tol = line.split(',')[i]
                tol = re.sub('\n', '', tol)
                tol = float(tol)
                add.append(tol)
            write.writerow(add)
            add = []
            stack_3 = 0

        if 'proc/s' in line:
            stack_1 = 1
        elif 'pswpin/s' in line:
            stack_2 = 1
        elif 'tps' in line:
            stack_3 = 1
