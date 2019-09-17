import csv
import re
import numpy

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
stack_name = 0
# 1차원 배열
add = []

# csv파일을 매트릭스로 저장하는 배열
add_list = []
add_list_2 = []
new_list_2 = []

# 해당 배열에 숫자를 저장하여 std값을 구함
add_std = []

# column의 이름을 저장하기 위함
add_name = []
k = 1

f = open("C:/Users/Slayer/Desktop/연구실 자료/Kisti 관련/Performance Analysis/3차 전처리/perf.csv", 'r', encoding='UTF8')
ff = open("C:/Users/Slayer/Desktop/연구실 자료/Kisti 관련/Performance Analysis/perf.csv", "w", newline='')

while True:
    line = f.readline()
    if not line: break
    if stack == 0 :
        comma_count = line.count(',')
        stack = 1
        for i in range(1,comma_count+1):
            tol = line.split(',')[i]
            tol = re.sub('\\n','',tol)
            add_name.append(tol)
    else:
        for i in range(1,comma_count+1):
            tol = line.split(',')[i]
            tol = re.sub('\n', '', tol)
            add.append(tol)
        add_list.append(add)
        add = []
new_list = list(map(list, zip(*add_list)))
list_count = len(new_list)

print(add_name)
print(len(add_name))
print(list_count)
for n in range(list_count):
    add = []
    add_std = []
    tol = new_list[n]
    tol = str(tol)
    tol = re.sub('\[', '', tol)
    tol = re.sub('\]', '', tol)
    tol = re.sub("'", '', tol)
    tol_count = tol.count(',')
    for nn in range(tol_count):
        column = tol.split(',')[nn]
        column = column.strip()
        column = float(column)
        add_std.append(column)
    std = numpy.std(add_std)

    if std == 0:
        pass
    else:
        for i in range(0, tol_count):
            add_tol = tol.split(',')[i]
            add_tol = re.sub('\n', '', add_tol)
            add.append(add_tol)
        add.insert(0, add_name[n])
        add_list_2.append(add)
        add = []
new_list_2 = list(map(list, zip(*add_list_2)))
print(new_list_2)
add = []
write = csv.writer(ff)
for i in range (nn):
    add = []
    line = new_list_2[i]
    line = str(line)
    line = re.sub('\[', '', line)
    line = re.sub('\]', '', line)
    line = re.sub("'", '', line)
    line_commna = line.count(',')

    for k in range (line_commna+1):
        if stack_name == 0:
            tol = line.split(',')[k]
            tol.strip()
            add.append(tol)

        else:
            tol = line.split(',')[k]
            tol.strip()
            tol = float(tol)
            add.append(tol)

    stack_name = 1
    write.writerow(add)
