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

for l in range(1, 2):

    node = str(l).zfill(2)
    new_name = []
    print(len(name))
    for i in range(len(name)):
        tol = "vmstat" + node + "_" + name[i]
        new_name.append(tol)
    f = open("C:/Users/DI_Lab/Desktop/Paper_Data/Epyc/Core64/Single/전처리 이전 데이터/Epyc" + str(node) + "_vmstat.txt", 'r')
    ff = open("C:/Users/DI_Lab/Desktop/Paper_Data/Epyc/Core64/Single/1차 전처리(CSV화)/Epyc" + str(node) + "_vmstat.csv", "w",newline='')

    write = csv.writer(ff)
    write.writerow(new_name)
    while True:
        line = f.readline()
        if not line: break
        line = " " + line
        if 'memory' in line:
            pass
        elif 'swpd' in line:
            pass
        else:
            line = split(line)
            print(line)
            for i in range(1, 18):
                tol = line.split(',')[i]
                tol = re.sub('\n', '', tol)
                tol = int(tol)
                add.append(tol)
            write.writerow(add)
            add = []