import csv
import re
import numpy as np
list_d = ["C:/Users/Slayer/Desktop/작업폴더/ddr/bt_collectl.csv"
,"C:/Users/Slayer/Desktop/작업폴더/ddr/cg_collectl.csv"
,"C:/Users/Slayer/Desktop/작업폴더/ddr/ep_collectl.csv"
,"C:/Users/Slayer/Desktop/작업폴더/ddr/ft_collectl.csv"
,"C:/Users/Slayer/Desktop/작업폴더/ddr/is_collectl.csv"
,"C:/Users/Slayer/Desktop/작업폴더/ddr/lu_collectl.csv"
,"C:/Users/Slayer/Desktop/작업폴더/ddr/mg_collectl.csv"
,"C:/Users/Slayer/Desktop/작업폴더/ddr/sp_collectl.csv"]

a = "C:/Users/Slayer/Desktop/작업폴더/tol.csv"
f_csv = open(a, 'w', newline='')
write = csv.writer(f_csv)
list = []
for i in range(0,1):
    open_csv = open(list_d[i], 'r')
    add =[]
    stack = 0
    while True:
        line = open_csv.readline()
        if not line: break
        add = []
        for j in range(0,40):
            tol = line.split(',')[j]
            tol = tol.strip()
            add.append(tol)
        list.append(add)
    if stack == 0:
        for i in range(0,40):
            pass

print(np.transpose(list))
