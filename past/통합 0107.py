import csv
import re

a = "NPB_23_21_53"

list_d = ["C:/Users/Slayer/Desktop/0제거/bt_collectl.csv"
,"C:/Users/Slayer/Desktop/0제거/cg_collectl.csv"
,"C:/Users/Slayer/Desktop/0제거/ep_collectl.csv"
,"C:/Users/Slayer/Desktop/0제거/ft_collectl.csv"
,"C:/Users/Slayer/Desktop/0제거/is_collectl.csv"
,"C:/Users/Slayer/Desktop/0제거/lu_collectl.csv"
,"C:/Users/Slayer/Desktop/0제거/mg_collectl.csv"
,"C:/Users/Slayer/Desktop/0제거/sp_collectl.csv"]
name_list_add = ['bt_collectl','cg_collectl','ep_collectl','ft_collectl',
                 'is_collectl','lu_collectl','mg_collectl','sp_collectl']

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
b = "C:/Users/Slayer/Desktop/0제거/()완료.csv"
f_csv = open(b, 'w', newline='')
write = csv.writer(f_csv)

for i in range(0,8):
    stack = 0
    f = open(list_d[i], 'r', newline='')
    add = []
    if name_list_add[i] == "bt_collectl" :
        name = "BT"
    elif name_list_add[i] == "cg_collectl":
        name = "CG"
    elif name_list_add[i] == "ep_collectl":
        name = "EP"
    elif name_list_add[i] == "ft_collectl":
        name = "FT"
    elif name_list_add[i] == "is_collectl":
        name = "IS"
    elif name_list_add[i] == "lu_collectl":
        name = "LU"
    elif name_list_add[i] == "mg_collectl":
        name = "MG"
    elif name_list_add[i] == "sp_collectl":
        name = "SP"
    while True:
        line = f.readline()
        if not line: break
        if stack == 0:
            stack = 1
        else:
            add = []
            add.append(name)
            for j in range(0,40):
                tol = line.split(',')[j]
                tol = tol.strip()
                add.append(tol)
            write.writerow(add)
