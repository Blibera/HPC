import csv
import re

name_list = ['bt.c','cg.c','ep.d','ft.c','is.d','lu.c','mg.d','sp.c']
name_list_add = ['bt_dstat','cg_dstat','ep_dstat','ft_dstat','is_dstat','lu_dstat','mg_dstat','sp_dstat']

add = []

name_stack = 0
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

for i in range(0,8):
    # 변수 초기화
    name_stack = 0

    # 자동 루프를 위한 변수 정의
    name = name_list[i]
    name_add = name_list_add[i]

    # 경로 설정
    b = "C:/Users/Slayer/Desktop/작업폴더/knl_npb_mcdram_newtype_1124/" + name_add + ".csv"

    # 파일 열기
    f_csv = open(b, 'w', newline='')

    # log파일이 10개라 10번 루프
    for j in range(0, 10):
        a = ""
        a = "C:/Users/Slayer/Desktop/작업폴더/knl_npb_mcdram_newtype_1124/" + str(name) + "/00" + str(j) + "_dstat_log.txt"
        mem_stack = 0
        # 변수명을 적어주기 위해 1번만 수행
        if name_stack == 0:
            name_csv = ['usr', 'sys', 'idl', 'wai', 'hiq', 'siq|', 'read', 'writ', 'recv', 'send', 'in', 'out', 'int',
                    'csw', 'run',
                    'blk', 'new',
                    'used', 'buff', 'cach', 'memory-usage_free', 'used', 'swap_free', 'one_m', 'five_m', 'fifteen_m',
                    'read',
                    'writ', 'aio', 'files', 'inodes', 'msg', 'sem',
                    'shm', 'pos', 'lck', 'rea', 'wri', 'raw', 'tot', 'tcp', 'udp', 'raw', 'frg', 'lis', 'act', 'syn',
                    'tim',
                    'clo', 'lis',
                    'act', 'dgm', 'str', 'lis', 'act', 'majpf', 'minpf', 'alloc', 'virtual-memory_free', 'epoch']

            # 파일 읽기
            f = open(a, 'r')

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
                if mem_stack == 1:
                    line = re.sub('\|', ' ', line)
                    line = split(line)

                    for i in range(1, 61):
                        tol = line.split(',')[i]
                        tol = re.sub('\n', '', tol)
                        add.append(tol)

                    write.writerow(add)
                    add = []
                    mem_stack = 0

                # 스택작업
                if 'free|  epoch' in line:
                    mem_stack = 1

        else:
            f = open(a, 'r')
            mem_stack = 0
            while True:
                line = f.readline()
                if not line: break
                # 스택 반환
                if mem_stack == 1:
                    line = re.sub('\|', ' ', line)
                    line = split(line)

                    for i in range(1, 61):
                        tol = line.split(',')[i]
                        tol = re.sub('\n', '', tol)
                        add.append(tol)

                    write.writerow(add)
                    add = []

                # 스택작업
                if 'free|  epoch' in line:
                    mem_stack = 1