import csv
import re

directory = "C:/Users/Slayer/Desktop/"
name_list_add = ['bt.c','cg.c','ep.d','ft.c',
                 'is.d','lu.c','mg.d','sp.c']

ram = ['mcdram/','ddr/']

for i in range(0,2):
    ram_name = ram[i]

    for j in range(0,8):
        folder_name =  name_list_add[j]

        for k in range(0,10):
            file_name = "/00" + str(k) + "_collectl_log.txt"

            file_dirctory = directory + ram_name + folder_name + file_name

            open_txt = open(file_dirctory, 'r')
            while True:
                line = open_txt.readline()
                if not line: break
                print(line)
