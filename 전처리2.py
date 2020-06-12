import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import csv

file_open = open("C:/Users/DI_Lab/Desktop/20년도 Kisti 과제/HMM/HMM(Up,Down).csv", 'r', encoding='UTF8')
save_file = open("C:/Users/DI_Lab/Desktop/20년도 Kisti 과제/HMM/HMM사후확률.csv", 'w', encoding='UTF8',newline='')
write = csv.writer(save_file)

hidden_states = ['up', 'down']
pi = [0.5044, 0.4956]
state_space = pd.Series(pi, index=hidden_states, name='states')
print(state_space)
print('\n', state_space.sum())

stack = 0
x_a = ""
x_b = ""

y_a = ""
y_b = ""
before_application = ""
add = []
def count(a,b):
    a = int(a)
    b = int(b)
    if a == 0 and b == 0:
        return 0
    elif a == 0 and b == 1:
        return 1
    elif a == 1 and b == 0:
        return 2
    elif a == 1 and b == 1:
        return 3

while True:
    line = file_open.readline()
    if not line: break
    result_x = []
    result_y = []
    add = []
    if stack == 0:
        a = line.split(',')[0]
        a = a.strip()
        add.append(a)
        a = line.split(',')[1]
        a = a.strip()
        add.append(a)
        a = line.split(',')[2]
        a = a.strip()
        add.append(a)
        write.writerow(add)

        stack = 1
    elif stack == 1:
        before_application = line.split(',')[0]
        x_a = line.split(',')[1]
        x_a = x_a.strip()
        y_a = line.split(',')[2]
        y_a = y_a.strip()
        stack = 2

    elif stack == 2:
        if before_application == line.split(',')[0]:
            x_b = line.split(',')[1]
            x_b = x_b.strip()
            y_b = line.split(',')[2]
            y_b = y_b.strip()
            result_x.append(x_a)
            result_x.append(x_b)
            result_y.append(y_a)
            result_y.append(y_b)
            tol = count(result_x[0],result_x[1])
            add.append(tol)
            tol = count(result_y[0], result_y[1])
            add.append(tol)
            write.writerow(add)
            stack = 3
        else:
            pass
        before_application = line.split(',')[0]

    elif stack == 3:
        if before_application == line.split(',')[0]:
            x_a = line.split(',')[1]
            x_a = x_a.strip()
            y_a = line.split(',')[2]
            y_a = y_a.strip()
            result_x.append(x_b)
            result_x.append(x_a)
            result_y.append(y_b)
            result_y.append(y_a)

            tol = count(result_x[0],result_x[1])
            add.append(tol)
            tol = count(result_y[0], result_y[1])
            add.append(tol)
            write.writerow(add)
            stack = 2
        else:
            pass
        before_application = line.split(',')[0]

