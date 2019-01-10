import csv
import re
import os

# 파일이 있는 디렉토리 (폴더 까지만)
directory = "C:/Users/Slayer/Desktop/작업폴더/ddr/"

# 어플리 케이션이 담긴 디렉토리 이름
application_directory = ["bt.c", "cg.c", "ep.d", "ft.c",
                         "is.d", "lu.c", "mg.d", "sp.c"]

# 모니터링 종류
# 모니터링 정보가 추가/삭제될 경우 해당부분에서 수정하기 위해 따로 정의해놓음
monitoring_name = ["_collectl_log.txt","_dstat_log.txt"]

# 첫줄에 변수명 입력을 위해서
name_csv_collectl = [
            'User', 'Nice', 'Sys', 'Wait', 'IRQ', 'Soft', 'Steal', 'Guest', 'NiceG', 'Idle', 'CPUs', 'Intr', 'Ctxsw', 'Proc', 'RunQ', 'Run', 'Avg1', 'Avg5', 'Avg15', 'RunT', 'BlkT', 'interrupt',
            'KBRead', 'RMerged', 'Reads_DISK', 'SizeKB', 'KBWrite', 'WMerged', 'Writes_DISK', 'SizeKB',
            'Reads_server', 'Writes_server', 'Meta_server', 'Comm_server', 'UDP', 'TCP', 'TCPConn', 'BadAuth', 'BadClnt', 'Reads_client', 'Writes_client', 'Meta_client', 'Comm_client', 'Retrans', 'Authref',
            'Number_Dentries', 'Unused', 'Alloc_INODE', 'MaxPct', 'Number_Inodes',
            'Total_Physical-Memory', 'Used_Physical-Memory', 'Free_Physical-Memory', 'Buff', 'Cached', 'Slab', 'Mapped', 'Anon', 'AnonH', 'Commit', 'Locked', 'Inact', 'Total_Swap', 'Used_Swap', 'Free_Swap', 'In_Swap', 'Out_Swap', 'Fault', 'MajFt', 'In_Paging', 'Out_Paging',
            '1Pg', '2Pgs', '4Pgs', '8Pgs', '16Pgs', '32Pgs', '64Pgs', '128Pgs', '256Pgs', '512Pgs', '1024Pgs',
            'KBIn', 'PktIn', 'SizeIn', 'MultI', 'CmpI', 'ErrsI', 'KBOut', 'PktOut', 'SizeO', 'CmpO', 'ErrsO',
            'Used_SOCKET', 'Inuse_Tcp', 'Orphan', 'Tw', 'Alloc_SOCKET', 'Mem_Tcp', 'Inuse_Udp', 'Inuse_Raw', 'Inuse_Frag', 'Mem_Frag',
            'Receiv', 'Delivr', 'Forwrd', 'DiscdI', 'InvAdd', 'Sent', 'DiscrO', 'ReasRq', 'ReasOK', 'FragOK', 'FragCr', 'ActOpn', 'PasOpn', 'Failed', 'ResetR', 'Estab', 'SegIn', 'SegOut', 'SegRtn', 'SegBad', 'SegRes', 'InDgm', 'OutDgm', 'NoPort', 'Errors', 'Recvd', 'FailI', 'UnreI', 'EchoI', 'ReplI', 'Trans', 'FailO', 'UnreO', 'EchoO', 'ReplO',
            'KBIn', 'PktIn', 'SizeIn', 'KBOut', 'PktOut', 'SizeOut', 'Errors',
            ]
"""
1번째줄 (User ~ BlkT + interrupt)  : CPU SUMMARY (INTR, CTXSW & PROC /sec) + INTERRUPT SUMMARY
2번째줄 (KBRead ~ SizeKB): DISK SUMMARY (/sec)
3번째줄 (Reads ~ Authref)  : NFS SUMMARY (/sec) 
4번째줄 (Number ~ Number) : INODE SUMMARY
5번째줄 (Total ~ Out) : MEMORY SUMMARY
6번째줄 (1Pg ~ 1024Pgs) : MEMORY FRAGMENTATION SUMMARY (4K pages)
7번째줄 (KBIn ~ ErrsO) : NETWORK SUMMARY (/sec)
8번째줄 (#Used ~ Mem) : SOCKET STATISTICS
9번째줄 (Receiv ~ ReplO) : TCP STACK SUMMARY (/sec)
10번째줄 (KBIn ~ Errors) : INFINIBAND SUMMARY (/sec)
"""

name_csv_dstat = [
    'usr','sys','idl','wai','hiq','siq',
    'read','writ',
    'recv','send',
    'in','out',
    'int','csw',
    'run','blk','new',
    'used','buff','cach','free',
    'used','free',
    '1m','5m','15m',
    'read','writ',
    '#aio',
    'files','inodes',
    'msg', 'sem','shm',
    'pos','lck','rea','wri',
    'raw',
    'tot','tcp','udp','raw','frg',
    'lis','act','syn','tim','clo',
    'lis','act',
    'dgm','str','lis','act',
    'majpf','minpf','alloc','free',
    'epoch'
]
"""
1번째줄 (usr ~ siq)  : total-cpu-usage
2번째줄 (read ~ writ): dsk/total
3번째줄 (recv ~ send)  : net/total
4번째줄 (in ~ out) : paging
5번째줄 (int ~ csw) : system
6번째줄 (run ~ new) : procs
7번째줄 (used ~ free) : memory-usage
8번째줄 (used ~ free) : swap
9번째줄 (1m ~ 15m) : load-avg
10번째줄 (read ~ writ) : io/total
11번째줄 (#aio)  : async
12번째줄 (files ~ inodes): filesystem
13번째줄 (msg ~ shm)  : sysv-ipc
14번째줄 (pos ~ wri) : file-locks
15번째줄 (raw) : raw
16번째줄 (tot ~ frg) : sockets
17번째줄 (lis ~ clo) : tcp-sockets
18번째줄 (lis ~ act) : udp
19번째줄 (dgm ~ act) : unix-sockets
20번째줄 (majpf ~ free) : virtual-memory
21번째줄 (epoch) : epoch
"""

# input txt의 구분형태인 공백을 ,으로 변환시켜 저장하기 쉽게함
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

# 부호 처리
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

# collectl 처리
def input_collectl(text):
    # 패턴
    collect_pattern = ['Avg15 RunT BlkT', ' Cpu269 Cpu270 Cpu271','WMerged Writes SizeKB', 'Comm Retrans  Authref', 'Alloc  MaxPct   Number', 'MajFt   In  Out',
                        '256Pgs  512Pgs 1024Pgs', 'SizeO   CmpO  ErrsO', 'Inuse  Inuse   Mem', 'UnreO EchoO ReplO', 'PktOut SizeOut  Errors' ]

    # 몇회 데이터가 발생했는지 ex) 001,002,003_collectl 데이터
    rupe_count = text.count("RECORD")

    # 발생한 횟수만큼 루프
    for i in range (1,rupe_count+1):
        summary = 0
        summary_num_add = 0

        # 1회 루프를 끊어서 파싱하기 위해
        split_line = text.split('RECORD')[i]
        split_line_column_total = []

        # 11개의 분류로 이루어져 있음
        for j in range (0,11):

            # interrupt summary의 경우 다른 부분과 다른 방식의 계산이 필요하여 interrput summary를 읽을때 따로 처리
            if j == 1:
                summary_list = []
                split_line_column = split_line.split(collect_pattern[j])[1]
                split_line_column = split_line_column.split('#')[0]
                split_line_column = re.sub('\\n','',split_line_column)
                split_line_column = split(split_line_column)
                comma_count = split_line_column.count(',')

                # interrput summary를 모두 더하기 위함
                for k in range(1, comma_count+1):
                    summary_num = split_line_column.split(',')[k]
                    summary_num_add = summary_num_add + int(summary_num)
                    summary_list.append(summary_num)

                # interrput summary를 평균냄
                summary_num_add = float(summary_num_add)
                summary_avg = summary_num_add / 272

                # interrput summary의 평균보다 높은 interrupt만 저장
                for k in range(0, comma_count):
                    if float(summary_list[k]) > summary_avg:
                        summary = summary + int(summary_list[k])
                summary = str(summary)
                summary = summary.strip()
                split_line_column_total.append(summary)

            else:
                split_line_column = split_line.split(collect_pattern[j])[1]
                split_line_column = split_line_column.split('#')[0]
                split_line_column = split(split_line_column)
                comma_count = split_line_column.count(',')

                # , 개수를 세서 그만큼 저장하는곳 (변수에 알맞는 값을 넣어주는 부분)
                # 현재 txt파일기준 40번 루프
                for k in range(1,comma_count+1):
                    split_line_column_add = split_line_column.split(',')[k]
                    split_line_column_add = split_line_column_add.strip()
                    split_line_column_add = int_num(split_line_column_add)
                    split_line_column_total.append(split_line_column_add)

        # csv에 값 저장
        write_pca.writerow(split_line_column_total)

# dstat 처리
def input_dstat(text):

    # 몇회의 데이터가 들어왔는지 ex) 001,002,003_dstat데이터
    rupe_count = text.count('Monitoring command')

    for i in range(1,rupe_count+1):
        split_line = text.split('majpf minpf alloc  free|  epoch')[i]
        split_line = split_line.split('#')[0]
        # 실제 값이있는 줄마다 카운트
        line_jump = split_line.count('\n')

        for j in range(1,line_jump):
            split_line_column_total = []
            text_line_column = split_line.split('\n')[j]
            text_line_column = re.sub("\|", '  ',text_line_column)
            text_line_column = split(text_line_column)
            comma_count = text_line_column.count(',')

            # 현재 txt파일기준 60번 루프
            for k in range(1, comma_count + 1):
                split_line_column_add = text_line_column.split(',')[k]
                split_line_column_add = split_line_column_add.strip()
                split_line_column_add = int_num(split_line_column_add)
                split_line_column_total.append(split_line_column_add)

            # csv에 값 저장
            write_pca.writerow(split_line_column_total)




if __name__ == "__main__":

    # 모니터링 수에따라 루프
    for monitor_rupe in range (0,len(monitoring_name)):

        # 어플리케이션 수에따라 루프
        for application_rupe in range (0, len(application_directory)):

            # 어플리케이션이 변경되면 초기화 하는 변수명
            file_num = 0
            Full_line = ""

            # 저장할 파일 (PCA)
            save_csv = directory + application_directory[application_rupe] + "/" + application_directory[application_rupe]+ monitoring_name[monitor_rupe] + "_PCA.csv"
            print(save_csv)
            open_pca_csv = open(save_csv, 'w', newline='')
            write_pca = csv.writer(open_pca_csv)

            # 기초통계분석
            save_csv_2 = directory + application_directory[application_rupe] + "/" + application_directory[application_rupe] + monitoring_name[monitor_rupe] + "_Basic-statistical-analysis.csv"
            open_basic = open(save_csv_2, 'w', newline='')
            write_open_basic = csv.writer(open_basic)

            if monitor_rupe == 0:
                write_pca.writerow(name_csv_collectl)
            else:
                write_pca.writerow(name_csv_dstat)

            # 파일 읽기
            while True:
                file_read = directory + application_directory[application_rupe] + "/" + str(file_num).zfill(3) + monitoring_name[monitor_rupe]
                file_num = file_num + 1
                # 파일이 있는지 체크
                check_file = os.path.isfile(file_read)

                if check_file == True:
                    f = open(file_read, 'r')

                    # txt파일 읽기
                    while True:
                        line = f.readline()
                        if not line: break
                        Full_line = Full_line + line


                else:
                    break
            if monitor_rupe == 0:
                input_collectl(Full_line)
                input_collectl_basic(Full_line)
            else:
                input_dstat(Full_line)