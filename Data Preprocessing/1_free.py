import csv
import re

name = ["used", "free", "shared", "buff/cache", "available"]
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
    f = open("C:/Users/Slayer/Desktop/연구실 자료/Kisti 관련/Performance Analysis/원본 데이터/node" + str(node) + "_free.txt", 'r')
    ff = open("C:/Users/Slayer/Desktop/연구실 자료/Kisti 관련/Performance Analysis/1차 전처리/node" + str(node) + "_free.csv", "w",newline='')

    write = csv.writer(ff)
    write.writerow(name)
    while True:
        line = f.readline()
        if not line: break

        if stack == 1:
            line = " " + line
            line = split(line)
            for k in range(1, 8):
                if k == 1 :
                    pass
                elif k == 2 :
                    pass
                else:
                    tol = line.split(",")[k]
                    tol = re.sub('\n', '', tol)
                    tol = int(tol)
                    add.append(tol)
            write.writerow(add)
            add = []
            stack = 0

        if 'available' in line:
            stack = 1

