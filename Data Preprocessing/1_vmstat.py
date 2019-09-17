import csv
import re

name = ["r","b","swpd","free","buff","cache","si","so","bi","bo","in","cs","us","sy","id","wa","st"]

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

for l in range(1,3):

    node = str(l).zfill(2)
    f = open("C:/Users/Slayer/Desktop/연구실 자료/Kisti 관련/Performance Analysis/원본 데이터/node" + str(node) + "_vmstat.txt", 'r', encoding='UTF8')
    ff = open("C:/Users/Slayer/Desktop/연구실 자료/Kisti 관련/Performance Analysis/1차 전처리/node" + str(node) + "_vmstat.csv", "w",newline='')

    write = csv.writer(ff)
    write.writerow(name)
    while True:
        line = f.readline()
        if not line: break

        if 'memory' in line:
            pass
        elif 'swpd' in line:
            pass
        else:
            line = split(line)
            for i in range(1, 18):
                tol = line.split(',')[i]
                tol = re.sub('\n', '', tol)
                tol = int(tol)
                add.append(tol)
            write.writerow(add)
            add = []