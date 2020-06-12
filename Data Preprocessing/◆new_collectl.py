import csv
import re

name = ["cpu","sys","inter","ctxsw","Free","Buff","Cach","Inac","Slab","Map","KBRead","Reads","KBWrit","Writes","KBIn","PktIn","KBOut","PktOut","Handle","Inodes"]

add = []

# stack 변수 모음


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

def int_num(text):
    count_k = text.count('K')
    count_m = text.count('M')
    count_g = text.count('G')

    if count_k == 0:
        pass
    elif count_k == 1:
        text = re.sub('K', '', text)
        text = int(text)
        text = text
    if count_m == 0:
        pass
    elif count_m == 1:
        text = re.sub('M', '', text)
        text = int(text)
        text = text * 1000
    if count_g == 0:
        pass
    elif count_g == 1:
        text = re.sub('G', '', text)
        text = int(text)
        text = text * 1000 * 1000
    return text

for l in range(1, 2):
    stack = 0
    node = str(l).zfill(2)
    new_name = []
    print(len(name))
    for i in range(len(name)):
        tol = "collectl" + node + "_" + name[i]
        new_name.append(tol)
    f = open("C:/Users/DI_Lab/Desktop/Paper_Data/Knl/Cache/Core64/Single/전처리 이전 데이터/knl" + str(node) + "_collectl.txt", 'r')
    ff = open("C:/Users/DI_Lab/Desktop/Paper_Data/Knl/Cache/Core64/Single/1차 전처리(CSV화)/knl" + str(node) + "_collectl.csv", "w",newline='')

    print(f)
    write = csv.writer(ff)
    write.writerow(new_name)
    while True:
        line = f.readline()
        if not line: break
        print(line)

        if stack == 1:
            line = " " + line
            line = split(line)

            if 'CPU' in line:
                pass
            elif 'cpu' in line:
                pass
            elif 'Ouch' in line:
                pass
            elif 'second' in line:
                pass
            else:
                for i in range(1, 21):
                    tol = line.split(',')[i]
                    tol = re.sub('\n', '', tol)
                    tol = int_num(tol)
                    add.append(tol)
                write.writerow(add)
                add = []

        if '#cpu sys inter  ' in line:
            stack = 1