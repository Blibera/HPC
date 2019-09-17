import csv
import re

name = ["%usr","%nice","%sys","%iowait","%irq","%soft","%steal","%guest","%gnice","%idle","HI/s","TIMER/s","NET_TX/s","NET_RX/s","BLOCK/s","IRQ_POLL/s","TASKLET/s","SCHED/s","HRTIMER/s","RCU/s"]

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
cpu_stack = 0
detail_stack = 0
for l in range(1,3):

    node = str(l).zfill(2)
    f = open("C:/Users/Slayer/Desktop/연구실 자료/Kisti 관련/Performance Analysis/원본 데이터/node" + str(node) + "_mpstat.txt", 'r', encoding='UTF8')
    ff = open("C:/Users/Slayer/Desktop/연구실 자료/Kisti 관련/Performance Analysis/1차 전처리/node" + str(node) + "_mpstat.csv", "w",newline='')

    write = csv.writer(ff)
    write.writerow(name)
    while True:
        line = f.readline()
        if not line: break

        if cpu_stack == 1:
            line = split(line)
            for i in range(4, 14):
                tol = line.split(',')[i]
                tol = re.sub('\n', '', tol)
                tol = float(tol)
                add.append(tol)
            cpu_stack = 0

        elif detail_stack == 1:
            line = split(line)
            if stack == 0:
                for k in range(4, 14):
                    tol = line.split(',')[k]
                    tol = re.sub('\n', '', tol)
                    tol = float(tol)
                    add.append(tol)
                stack = stack + 1
            elif stack == 1:
                for k in range(4, 14):
                    tol = line.split(',')[k]
                    tol = re.sub('\n', '', tol)
                    tol = float(tol)
                    add[k+6] = add[k+6] + tol
                stack = stack + 1
            elif stack == 2:
                for k in range(4, 14):
                    tol = line.split(',')[k]
                    tol = re.sub('\n', '', tol)
                    tol = float(tol)
                    add[k+6] = add[k+6] + tol
                stack = stack + 1
            elif stack == 3:
                for k in range(4, 14):
                    tol = line.split(',')[k]
                    tol = re.sub('\n', '', tol)
                    tol = float(tol)
                    add[k+6] = add[k+6] + tol
                stack = 0
                detail_stack = 0
                write.writerow(add)
                add = []

        if '%usr' in line:
            cpu_stack = 1
        elif 'HI/s' in line:
            detail_stack = 1