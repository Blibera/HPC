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
for l in range(1, 2):

    node = str(l).zfill(2)
    new_name = []
    print(len(name))
    for i in range(len(name)):
        tol = "free" + node + "_" + name[i]
        new_name.append(tol)
    f = open("C:/Users/DI_Lab/Desktop/Paper_Data/Knl/Cache/Core64/Single/전처리 이전 데이터/knl" + str(node) + "_free.txt", 'r')
    ff = open("C:/Users/DI_Lab/Desktop/Paper_Data/Knl/Cache/Core64/Single/1차 전처리(CSV화)/knl" + str(node) + "_free.csv", "w",newline='')

    write = csv.writer(ff)
    write.writerow(new_name)
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

