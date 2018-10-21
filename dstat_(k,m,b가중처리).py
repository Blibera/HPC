import csv
import re

name_list = ['bt.c','cg.c','ep.d','ft.c','is.d','lu.c','mg.d','sp.c']
name_list_add = ['bt_dstat','cg_dstat','ep_dstat','ft_dstat','is_dstat','lu_dstat','mg_dstat','sp_dstat']

add = []

mem_stack = 0

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
    M = 0
    G = 0
    M = text.count('M')
    G = text.count('G')

    if M == 0:
        pass
    else:
        text = re.sub('M', '', text)
        text = float(text)
        text = text * 1000

    if G == 0:
        pass
    else:
        text = re.sub('G', '', text)
        text = float(text)
        text = text * 1000 * 1000


    return text
name = ""
name_add = ""
for i in range(0,8):
    name = name_list[i]
    name_add = name_list_add[i]

    a = "C:/Users/Slayer/Desktop/NPB_19_18_45/" + name + "/000_dstat_log.txt"
    b = "C:/Users/Slayer/Desktop/NPB_19_18_45/" + name_add + "(가중처리).csv"
    f_1 = open(a, 'r')
    f_2 = open(a, 'r')
    f_3 = open(a, 'r')
    f_4 = open(a, 'r')
    f_5 = open(a, 'r')
    f = open(b, 'w', newline='')
    name = ['usr', 'sys', 'idl', 'wai', 'hiq', 'siq|', 'read', 'writ', 'recv', 'send', 'in', 'out', 'int', 'csw', 'run',
            'blk', 'new',
            'used', 'buff', 'cach', 'memory-usage_free', 'used', 'swap_free', 'one_m', 'five_m', 'fifteen_m', 'read',
            'writ', 'aio', 'files', 'inodes', 'msg', 'sem',
            'shm', 'pos', 'lck', 'rea', 'wri', 'raw', 'tot', 'tcp', 'udp', 'raw', 'frg', 'lis', 'act', 'syn', 'tim',
            'clo', 'lis',
            'act', 'dgm', 'str', 'lis', 'act', 'majpf', 'minpf', 'alloc', 'virtual-memory_free', 'epoch']

    write = csv.writer(f)
    write.writerow(name)

    while True:
        line = f_1.readline()
        if not line: break
        tol = 0
        num = 0

        # 스택 반환
        if mem_stack == 1:
            line = re.sub('\|',' ',line)
            line = split(line)
            t = line.count(',')
            for i in range(1,54):
                tol = line.split(',')[i]
                tol = re.sub('\n','',tol)
                tol = re.sub('K', '', tol)
                tol = re.sub('k', '', tol)
                tol = re.sub('B', '', tol)
                tol = int_num(tol)
                add.append(tol)

            write.writerow(add)
            tol = 0
            add = []
            mem_stack = 0

        # 스택작업
        if 'usr sys idl wai hiq siq| read  writ| recv  send|  in   out | int   csw |run blk new| used  buff  cach  free| used  free' in line:
            mem_stack = 1

    while True:
        line = f_2.readline()
        if not line: break
        tol = 0
        num = 0

        # 스택 반환
        if mem_stack == 1:
            line = re.sub('\|',' ',line)
            line = split(line)
            t = line.count(',')
            for i in range(1,54):
                tol = line.split(',')[i]
                tol = re.sub('\n', '', tol)
                tol = re.sub('K', '', tol)
                tol = re.sub('k', '', tol)
                tol = re.sub('B', '', tol)
                tol = int_num(tol)
                add.append(tol)

            write.writerow(add)
            tol = 0
            add = []
            mem_stack = 0

        # 스택작업
        if 'usr sys idl wai hiq siq| read  writ| recv  send|  in   out | int   csw |run blk new| used  buff  cach  free| used  free' in line:
            mem_stack = 1

    while True:
        line = f_3.readline()
        if not line: break
        tol = 0
        num = 0

        # 스택 반환
        if mem_stack == 1:
            line = re.sub('\|',' ',line)
            line = split(line)
            t = line.count(',')
            for i in range(1,54):
                tol = line.split(',')[i]
                tol = re.sub('\n', '', tol)
                tol = re.sub('K', '', tol)
                tol = re.sub('k', '', tol)
                tol = re.sub('B', '', tol)
                tol = int_num(tol)
                add.append(tol)
            write.writerow(add)
            tol = 0
            add = []
            mem_stack = 0

        # 스택작업
        if 'usr sys idl wai hiq siq| read  writ| recv  send|  in   out | int   csw |run blk new| used  buff  cach  free| used  free' in line:
            mem_stack = 1

    while True:
        line = f_4.readline()
        if not line: break
        tol = 0
        num = 0

        # 스택 반환
        if mem_stack == 1:
            line = re.sub('\|',' ',line)
            line = split(line)
            t = line.count(',')
            for i in range(1,54):
                tol = line.split(',')[i]
                tol = re.sub('\n', '', tol)
                tol = re.sub('K', '', tol)
                tol = re.sub('k', '', tol)
                tol = re.sub('B', '', tol)
                tol = int_num(tol)
                add.append(tol)

            write.writerow(add)
            tol = 0
            add = []
            mem_stack = 0

        # 스택작업
        if 'usr sys idl wai hiq siq| read  writ| recv  send|  in   out | int   csw |run blk new| used  buff  cach  free| used  free' in line:
            mem_stack = 1

    while True:
        line = f_5.readline()
        if not line: break
        tol = 0
        num = 0

        # 스택 반환
        if mem_stack == 1:
            line = re.sub('\|',' ',line)
            line = split(line)
            t = line.count(',')
            for i in range(1,54):
                tol = line.split(',')[i]
                tol = re.sub('\n', '', tol)
                tol = re.sub('K', '', tol)
                tol = re.sub('k', '', tol)
                tol = re.sub('B', '', tol)
                tol = int_num(tol)
                add.append(tol)

            write.writerow(add)
            tol = 0
            add = []
            mem_stack = 0

        # 스택작업
        if 'usr sys idl wai hiq siq| read  writ| recv  send|  in   out | int   csw |run blk new| used  buff  cach  free| used  free' in line:
            mem_stack = 1
    f.close()