import csv
import re

name_list = ['bt.c','cg.c','ep.d','ft.c','is.d','lu.c','mg.d','sp.c']
name_list_add = ['bt_dstat','cg_dstat','ep_dstat','ft_dstat','is_dstat','lu_dstat','mg_dstat','sp_dstat']
add = []


directory = ""

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
    count_k = text.count("k")
    count_kk = text.count("K")
    count_b = text.count("B")
    count_m = text.count("M")
    count_g = text.count("G")

    if count_k == 0:
        pass
    else:
        text = re.sub("k", "", text)
        text = float(text)
        text = text * 1024

    if count_kk == 0:
        pass
    else:
        text = re.sub("K", "", text)
        text = float(text)
        text = text * 1024

    if count_b == 0:
        pass
    else:
        text = re.sub("B", "", text)
        text = float(text)
        text = text

    if count_m == 0:
        pass
    else:
        text = re.sub("M", "", text)
        text = float(text)
        text = text * 1024

    if count_g == 0:
        pass
    else:
        text = re.sub("G", "", text)
        text = float(text)
        text = text * 1024 * 1024
    return text
name = ""
name_add = ""
for i in range(0,8):
    log_count = 0
    name_aple = name_list[i]
    name_add = name_list_add[i]
    b = "C:/Users/Slayer/Desktop/Kisti/작업폴더/ddr/" + name_add + ".csv"
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
    for j in range(0,10):
        print(str(log_count).zfill(3))
        a = "C:/Users/Slayer/Desktop/Kisti/작업폴더/ddr/" + name_aple + "/" + str(log_count).zfill(3) + "_dstat_log.txt"

        f_1 = open(a, 'r')

        mem_stack = 0

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
                for i in range(1,61):
                    tol = line.split(',')[i]
                    tol = re.sub('\n','',tol)
                    tol = int_num(tol)
                    add.append(tol)

                write.writerow(add)
                add = []

            # 스택작업
            if 'usr sys idl wai hiq siq| read  writ| recv  send|  in   out | int   csw |run blk new| used  buff  cach  free| used  free' in line:
                mem_stack = 1
        log_count = log_count + 1


    f.close()