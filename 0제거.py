import csv
import re

a = "NPB_23_21_53"

list_d = ["C:/Users/Slayer/Desktop/작업폴더/"+str(a)+"/bt_collectl.csv"
,"C:/Users/Slayer/Desktop/작업폴더/"+str(a)+"//bt_dstat.csv"
,"C:/Users/Slayer/Desktop/작업폴더/"+str(a)+"//cg_collectl.csv"
,"C:/Users/Slayer/Desktop/작업폴더/"+str(a)+"//cg_dstat.csv"
,"C:/Users/Slayer/Desktop/작업폴더/"+str(a)+"//ep_collectl.csv"
,"C:/Users/Slayer/Desktop/작업폴더/"+str(a)+"//ep_dstat.csv"
,"C:/Users/Slayer/Desktop/작업폴더/"+str(a)+"//ft_collectl.csv"
,"C:/Users/Slayer/Desktop/작업폴더/"+str(a)+"//ft_dstat.csv"
,"C:/Users/Slayer/Desktop/작업폴더/"+str(a)+"//is_collectl.csv"
,"C:/Users/Slayer/Desktop/작업폴더/"+str(a)+"//is_dstat.csv"
,"C:/Users/Slayer/Desktop/작업폴더/"+str(a)+"//lu_collectl.csv"
,"C:/Users/Slayer/Desktop/작업폴더/"+str(a)+"//lu_dstat.csv"
,"C:/Users/Slayer/Desktop/작업폴더/"+str(a)+"//mg_collectl.csv"
,"C:/Users/Slayer/Desktop/작업폴더/"+str(a)+"//mg_dstat.csv"
,"C:/Users/Slayer/Desktop/작업폴더/"+str(a)+"//sp_collectl.csv"
,"C:/Users/Slayer/Desktop/작업폴더/"+str(a)+"//sp_dstat.csv"]
name_list_add = ['bt_collectl','bt_dstat','cg_collectl','cg_dstat','ep_collectl','ep_dstat','ft_collectl','ft_dstat',
                 'is_collectl','is_dstat','mg_collectl','mg_dstat','mg_collectl','mg_dstat','sp_collectl','sp_dstat']

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

for i in range(0,16):
    f = open(list_d[i], 'r', newline='')
    listt = []
    list_t = []
    list_name = []
    list_new = []
    stack = 0
    stack_list = 0
    add = []
    name_add = name_list_add[i]

    # 경로 설정
    b = "C:/Users/Slayer/Desktop/작업폴더/" + name_add + "(0제거).csv"

    # 파일 열기
    f_csv = open(b, 'w', newline='')
    write = csv.writer(f_csv)

    line = f.readline()
    comma_count = line.count(',')
    list_count = 0
    for j in range(0,comma_count+1):
        f = open(list_d[i], 'r', newline='')
        listt = []
        while True:
            line = f.readline()
            if not line: break
            if stack == 0:
                tol = line.split(',')[j]
                tol = re.sub('\r\n', '', tol)
                listt.append(tol)
                stack = 1


            else:
                tol = line.split(',')[j]
                tol = re.sub('\r\n', '', tol)
                listt.append(tol)
        list_name = listt[:]
        del list_name[0]
        list_name.sort()
        if list_name[0] == list_name[-1]:
            pass
        else:
            list_t.append(listt)

    new_list = list(map(list, zip(*list_t)))
    list_count = len(new_list)

    for n in range(list_count):
        add = []
        tol = new_list[n]
        tol = str(tol)
        tol = re.sub('\[','',tol)
        tol = re.sub('\]','',tol)
        tol = re.sub("'",'',tol)
        tol_count = tol.count(',')
        for nn in range(tol_count):
            column = tol.split(',')[nn]
            column = column.strip()
            add.append(column)
        write.writerow(add)