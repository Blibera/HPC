import csv
import re

name_list = ['bt.c','cg.c','ep.d','ft.c','is.d','lu.c','mg.d','sp.c']
name_list_add = ['bt_dstat','cg_dstat','ep_dstat','ft_dstat','is_dstat','lu_dstat','mg_dstat','sp_dstat']
directory = "knl_npb_mcdram_newtype_1124"
add = []

name_stack = 0
cpu_stack = 0
disk_stack = 0
network_stack = 0
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
    count_k = text.count("K")

    if count_k == 0:
        pass
    else:
        text = re.sub("K", "", text)
        text = float(text)
        text = text*1000
    text = float(text)
    return text

for i in range(0,8):
    # 변수 초기화
    name_stack = 0

    # 자동 루프를 위한 변수 정의
    name = name_list[i]
    name_add = name_list_add[i]

    # 경로 설정
    b = "C:/Users/Slayer/Desktop/작업폴더/" + directory + "/" + name_add + ".csv"

    # 파일 열기
    f_csv = open(b, 'w', newline='')
    # log파일이 10개라 10번 루프
    for j in range(0,10):
        a = ""
        a = "C:/Users/Slayer/Desktop/작업폴더/" + directory + "/" + str(name) + "/00" + str(j) + "_collectl_log.txt"

        # 변수명을 적어주기 위해 1번만 수행
        if name_stack == 0 :
            name_csv = ['User','Nice','Sys','Wait','IRQ','Soft','Steal','Guest','NiceG','Idle','CPUs','Intr','Ctxsw','Proc','RunQ','Run','Avg1','Avg5','Avg15','RunT','BlkT',
                    'KBRead','RMerged','Reads','SizeKB','KBWrite','WMerged','Writes','SizeKB',
                    'KBIn','PktIn','SizeIn','MultI','CmpI','ErrsI','KBOut','PktOut','SizeO','CmpO','ErrsO']
            """
            1번째줄 (User)  : cpu summary
            2번째줄 (KBRead): disk summary
            3번째줄 (KBln)  : network summary
            """

            # 파일 읽기
            f = open(a,'r')

            # 변수 적어주기
            write = csv.writer(f_csv)
            write.writerow(name_csv)

            # 스택 증가
            name_stack = 1

            # 1줄씩 읽기
            while True:
                line = f.readline()
                if not line: break

                # 스택 반환
                if cpu_stack == 1:
                    line = re.sub('\|', ' ', line)
                    line = split(line)
                    for i in range(1, 22):
                        tol = line.split(',')[i]
                        tol = re.sub('\n', '', tol)
                        tol = int_num(tol)
                        add.append(tol)
                    cpu_stack = 0

                if disk_stack == 1:
                    line = re.sub('\|', ' ', line)
                    line = split(line)
                    for i in range(1, 9):
                        tol = line.split(',')[i]
                        tol = re.sub('\n', '', tol)
                        tol = int_num(tol)
                        add.append(tol)
                    disk_stack = 0

                if network_stack == 1:
                    line = re.sub('\|', ' ', line)
                    line = split(line)
                    for i in range(1, 12):
                        tol = line.split(',')[i]
                        tol = re.sub('\n', '', tol)
                        tol = int_num(tol)
                        add.append(tol)

                    write.writerow(add)
                    add = []
                    network_stack = 0

                # 스택작업
                if 'User  Nice   Sys  Wait   IRQ  Soft Steal Guest NiceG  Idle  CPUs  Intr  Ctxsw  Proc  RunQ   Run   Avg1  Avg5 Avg15 RunT BlkT' in line:
                    cpu_stack = 1
                elif 'KBRead RMerged  Reads SizeKB  KBWrite WMerged Writes SizeKB' in line:
                    disk_stack = 1
                elif 'KBIn  PktIn SizeIn  MultI   CmpI  ErrsI  KBOut PktOut  SizeO   CmpO  ErrsO' in line:
                    network_stack = 1

        else:
            f = open(a, 'r')
            while True:
                line = f.readline()
                if not line: break

                # 스택 반환
                if cpu_stack == 1:
                    line = re.sub('\|', ' ', line)
                    line = split(line)
                    for i in range(1, 22):
                        tol = line.split(',')[i]
                        tol = re.sub('\n', '', tol)
                        tol = int_num(tol)
                        add.append(tol)
                    cpu_stack = 0

                if disk_stack == 1:
                    line = re.sub('\|', ' ', line)
                    line = split(line)
                    for i in range(1, 9):
                        tol = line.split(',')[i]
                        tol = re.sub('\n', '', tol)
                        tol = int_num(tol)
                        add.append(tol)
                    disk_stack = 0

                if network_stack == 1:
                    line = re.sub('\|', ' ', line)
                    line = split(line)
                    for i in range(1, 12):
                        tol = line.split(',')[i]
                        tol = re.sub('\n', '', tol)
                        tol = int_num(tol)
                        add.append(tol)

                    write.writerow(add)
                    add = []
                    network_stack = 0

                # 스택작업
                if 'User  Nice   Sys  Wait   IRQ  Soft Steal Guest NiceG  Idle  CPUs  Intr  Ctxsw  Proc  RunQ   Run   Avg1  Avg5 Avg15 RunT BlkT' in line:
                    cpu_stack = 1
                elif 'KBRead RMerged  Reads SizeKB  KBWrite WMerged Writes SizeKB' in line:
                    disk_stack = 1
                elif 'KBIn  PktIn SizeIn  MultI   CmpI  ErrsI  KBOut PktOut  SizeO   CmpO  ErrsO' in line:
                    network_stack = 1
