import csv
import re

name = ["%user","%nice","%system","%iowait","%steal","%idle","proc/s","cswch/s","pswpin/s","pswpout/", "spgpgin/s","pgpgout/s","fault/s","majflt/s","pgfree/s","pgscank/s","pgscand/s","pgsteal/s","%vmeff","tps","rtps","wtps","bread/s","bwrtn/s", "kbmemfree","kbavail","kbmemused","%memused","kbbuffers","kbcached","kbcommit","%commit","kbactive","kbinact","kbdirty","kbswpfree","kbswpused","%swpused","kbswpcad","%swpcad","dentunusd","file-nr","inode-nr","pty-nr","runq-sz","plist-sz","ldavg-1","ldavg-5","ldavg-15","blocked","irec/s","fwddgm/s","idel/s","orq/s","asmrq/s","asmok/s","fragok/s","fragcrt/s","ihdrerr/s","iadrerr/s","iukwnpr/s","idisc/s","odisc/s","onort/s","asmf/s","fragf/s","active/s","passive/s","iseg/s","oseg/s"]
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
stack_4 = 0
stack_5 = 0
stack_6 = 0
stack_7 = 0
stack_8 = 0
stack_9 = 0
stack_10 = 0
stack_11 = 0
stack_12 = 0


for l in range(1,3):

    node = str(l).zfill(2)
    f = open("C:/Users/Slayer/Desktop/연구실 자료/Kisti 관련/Performance Analysis/원본 데이터/node" + str(node) + "_sar.txt", 'r', encoding='UTF8')
    ff = open("C:/Users/Slayer/Desktop/연구실 자료/Kisti 관련/Performance Analysis/1차 전처리/node" + str(node) + "_sar.csv", "w",newline='')

    write = csv.writer(ff)
    write.writerow(name)
    while True:
        line = f.readline()
        if not line: break

        if stack_1 == 1:
            line = split(line)
            for i in range(4, 10):
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
            for i in range(3, 5):
                tol = line.split(',')[i]
                tol = re.sub('\n', '', tol)
                tol = float(tol)
                add.append(tol)
            stack_3 = 0

        elif stack_4 == 1:
            line = split(line)
            for i in range(3, 12):
                tol = line.split(',')[i]
                tol = re.sub('\n', '', tol)
                tol = float(tol)
                add.append(tol)
            stack_4 = 0

        elif stack_5 == 1:
            line = split(line)
            for i in range(3, 8):
                tol = line.split(',')[i]
                tol = re.sub('\n', '', tol)
                tol = float(tol)
                add.append(tol)
            stack_5 = 0

        elif stack_6 == 1:
            line = split(line)
            for i in range(3, 14):
                tol = line.split(',')[i]
                tol = re.sub('\n', '', tol)
                tol = float(tol)
                add.append(tol)
            stack_6 = 0

        elif stack_7 == 1:
            line = split(line)
            for i in range(3, 8):
                tol = line.split(',')[i]
                tol = re.sub('\n', '', tol)
                tol = float(tol)
                add.append(tol)
            stack_7 = 0

        elif stack_8 == 1:
            line = split(line)
            for i in range(3, 7):
                tol = line.split(',')[i]
                tol = re.sub('\n', '', tol)
                tol = float(tol)
                add.append(tol)
            stack_8 = 0

        elif stack_9 == 1:
            line = split(line)
            for i in range(3, 9):
                tol = line.split(',')[i]
                tol = re.sub('\n', '', tol)
                tol = float(tol)
                add.append(tol)
            stack_9 = 0

        elif stack_10 == 1:
            line = split(line)
            for i in range(3, 11):
                tol = line.split(',')[i]
                tol = re.sub('\n', '', tol)
                tol = float(tol)
                add.append(tol)
            stack_10 = 0

        elif stack_11 == 1:
            line = split(line)
            for i in range(3, 11):
                tol = line.split(',')[i]
                tol = re.sub('\n', '', tol)
                tol = float(tol)
                add.append(tol)
            stack_11 = 0

        elif stack_12 == 1:
            line = split(line)
            for i in range(3, 7):
                tol = line.split(',')[i]
                tol = re.sub('\n', '', tol)
                tol = float(tol)
                add.append(tol)
            stack_12 = 0
            write.writerow(add)
            add = []
            stack = 0

        if '%user' in line:
            stack_1 = 1
        elif 'proc/s   cswch/s' in line:
            stack_2 = 1
        elif 'pswpin/s' in line:
            stack_3 = 1
        elif 'pgpgin/s' in line:
            stack_4 = 1
        elif 'tps' in line:
            stack_5 = 1
        elif 'kbmemfree' in line:
            stack_6 = 1
        elif 'kbswpfree' in line:
            stack_7 = 1
        elif 'dentunusd' in line:
            stack_8 = 1
        elif 'runq-sz' in line:
            stack_9 = 1
        elif 'irec/s' in line:
            stack_10 = 1
        elif 'ihdrerr/s' in line:
            stack_11 = 1
        elif 'active/s' in line:
            stack_12 = 1


