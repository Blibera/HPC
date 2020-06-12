import re
import csv

file_open = open("C:/Users/DI_Lab/Desktop/20년도 Kisti 과제/HMM/HMM.csv", 'r', encoding='UTF8')
save_file = open("C:/Users/DI_Lab/Desktop/20년도 Kisti 과제/HMM/HMM(Up,Down).csv", 'w', encoding='UTF8',newline='')
write = csv.writer(save_file)
stack = 0

add = []
x_a = ""
x_b = ""

y_a = ""
y_b = ""
before_application = ""
while True:
    line = file_open.readline()
    if not line: break
    add_result = []
    if stack == 0:
        for i in range(line.count(',')+1):
            tol = line.split(',')[i]
            tol = tol.strip()
            add.append(tol)
        write.writerow(add)
        stack = 1

    elif stack == 1:
        x_a = line.split(',')[1]
        y_a = line.split(',')[2]
        before_application = line.split(',')[0]
        stack = 2

    elif stack == 2:
        if before_application == line.split(',')[0]:
            x_b = line.split(',')[1]
            y_b = line.split(',')[2]
            add_result.append(before_application)
            if x_a > x_b:
                tol = 0
                add_result.append(tol)
            else:
                tol = 1
                add_result.append(tol)
            if y_a > y_b:
                tol = 0
                add_result.append(tol)
            else:
                tol = 1
                add_result.append(tol)
            stack = 3
            print(x_a, x_b)
            print(y_a, y_b)
            print("=================")
            print("=================")
            write.writerow(add_result)
        else:
            pass

        before_application = line.split(',')[0]

    elif stack == 3:
        if before_application == line.split(',')[0]:
            x_a = line.split(',')[1]
            y_a = line.split(',')[2]
            add_result.append(before_application)
            if x_a < x_b:
                tol = 0
                add_result.append(tol)
            else:
                tol = 1
                add_result.append(tol)
            if y_a < y_b:
                tol = 0
                add_result.append(tol)
            else:
                tol = 1
                add_result.append(tol)
            stack = 2
            write.writerow(add_result)
            print(x_a, x_b)
            print(y_a, y_b)
            print("=================")
            print("=================")
        else:
            pass
        before_application = line.split(',')[0]


