import csv
import re


name = ["User","Nice","Sys","Wait","IRQ","Soft","Steal","Guest","NiceG","Idle","CPUs","Intr","Ctxsw","Proc","RunQ","Run","Avg1","Avg5","Avg15","RunT","BlkT","KBRead","RMerged","Reads","SizeKB","KBWrite","WMerged","Writes","SizeKB","Reads","Writes","Meta","Comm","UDP","TCP","TCPConn","BadAuth","BadClnt","Reads","Writes","Meta","Comm","Retrans","Authref","Number","Unused","Alloc","MaxPct","Number","Total","Used","Free","Buff","Cached","Slab","Mapped","Anon","AnonH","Commit","Locked","Inact","Total","Used","Free","In","Out","Fault","MajFt","In","Out","1Pg","2Pgs","4Pgs","8Pgs","16Pgs","32Pgs","64Pgs","128Pgs","256Pgs","512Pgs","1024Pgs","KBIn","PktIn","SizeIn","MultI","CmpI","ErrsI","KBOut","PktOut","SizeO","CmpO","ErrsO","Used","Inuse","Orphan","Tw","Alloc","Mem","Inuse","Inuse","Inuse","Mem","Receiv","Delivr","Forwrd","DiscdI","InvAdd","Sent","DiscrO","ReasRq","ReasOK","FragOK","FragCr","ActOpn","PasOpn","Failed","ResetR","Estab","SegIn","SegOut","SegRtn","SegBad","SegRes","InDgm","OutDgm","NoPort","Errors","Recvd","FailI","UnreI","EchoI","ReplI","Trans","FailO","UnreO","EchoO","ReplO"]



add = []

# stack 변수 모음
cpu_stack = 0
disk_stack = 0
nfs_stack = 0
inode_stack = 0
memory_stack = 0
memory_fragementation_stack = 0
network_stack = 0
socket_stack = 0
tcp_stack = 0
infiniband_stack = 0

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
    count_k = text.count('K')
    count_m = text.count('M')
    if count_k == 0:
        pass
    elif count_k == 1:
        text = re.sub('K', '', text)
        text = int(text)
        text = text
    if count_m == 0:
        pass
    elif count_m == 1:
        text = re.sub('M', '', text)
        text = int(text)
        text = text * 1000
    return text

for l in range(2,3):

    node = str(l).zfill(2)
    new_name = []
    print(len(name))
    for i in range(len(name)):
        tol = "collectl" + node + "_" + name[i]
        new_name.append(tol)
    f = open("C:/Users/Slayer/Desktop/원본 데이터/Knl 싱글노드/knl" + str(node) + "_collectl.txt", 'r')
    ff = open("C:/Users/Slayer/Desktop/원본 데이터/Knl 싱글노드/1차 전처리/knl" + str(node) + "_collectl.csv", "w",
              newline='')
    print(f)
    write = csv.writer(ff)
    write.writerow(new_name)
    while True:
        line = f.readline()
        if not line: break


        if cpu_stack == 1:
            line = " " + line
            line = split(line)
            for i in range(1, 22):
                tol = line.split(',')[i]
                tol = re.sub('\n', '', tol)
                tol = int_num(tol)
                add.append(tol)
            cpu_stack = 0

        elif disk_stack == 1:
            line = " " + line
            line = split(line)
            for i in range(1, 9):
                tol = line.split(',')[i]
                tol = re.sub('\n', '', tol)
                tol = int_num(tol)
                add.append(tol)
            disk_stack = 0

        elif nfs_stack == 1:
            line = " " + line
            line = split(line)
            for i in range(1, 16):
                tol = line.split(',')[i]
                tol = re.sub('\n', '', tol)
                tol = int_num(tol)
                add.append(tol)
            nfs_stack = 0

        elif inode_stack == 1:
            line = " " + line
            line = split(line)
            for i in range(1, 6):
                tol = line.split(',')[i]
                tol = re.sub('\n', '', tol)
                tol = int_num(tol)
                add.append(tol)
            inode_stack = 0

        elif memory_stack == 1:
            line = " " + line
            line = split(line)
            for i in range(1, 22):
                tol = line.split(',')[i]
                tol = re.sub('\n', '', tol)
                tol = int_num(tol)
                add.append(tol)
            memory_stack = 0

        elif memory_fragementation_stack == 1:
            line = " " + line
            line = split(line)
            for i in range(1, 12):
                tol = line.split(',')[i]
                tol = re.sub('\n', '', tol)
                tol = int_num(tol)
                add.append(tol)
            memory_fragementation_stack = 0

        elif network_stack == 1:
            line = " " + line
            line = split(line)
            for i in range(1, 12):
                tol = line.split(',')[i]
                tol = re.sub('\n', '', tol)
                tol = int_num(tol)
                add.append(tol)
            network_stack = 0

        elif socket_stack == 1:
            line = " " + line
            line = split(line)
            for i in range(1, 11):
                tol = line.split(',')[i]
                tol = re.sub('\n', '', tol)
                tol = int_num(tol)
                add.append(tol)
            socket_stack = 0

        elif tcp_stack == 1:
            line = " " + line
            line = split(line)
            for i in range(1, 36):
                tol = line.split(',')[i]
                tol = re.sub('\n', '', tol)
                tol = int_num(tol)
                add.append(tol)
            write.writerow(add)
            add = []
            tcp_stack = 0

        """        elif infiniband_stack == 1:
            line = " " + line
            line = split(line)
            for i in range(1, 8):
                tol = line.split(',')[i]
                tol = re.sub('\n', '', tol)
                tol = int_num(tol)
                add.append(tol)
            print("check")
            write.writerow(add)
            add = []
            infiniband_stack = 0"""

        if 'User  Nice   Sys  Wait   IRQ' in line:
            cpu_stack = 1
        elif 'KBRead RMerged  Reads' in line:
            disk_stack = 1
        elif 'Reads Writes Meta Comm' in line:
            nfs_stack = 1
        elif 'Number   Unused   Alloc' in line:
            inode_stack = 1
        elif 'Total    Used    Free    Buff  Cached' in line:
            memory_stack = 1
        elif '1Pg    2Pgs    4Pgs    8Pgs' in line:
            memory_fragementation_stack = 1
        elif 'KBIn  PktIn SizeIn  MultI   CmpI  ' in line:
            network_stack = 1
        elif 'Used  Inuse Orphan    Tw  Alloc   Mem' in line:
            socket_stack = 1
        elif 'Receiv Delivr Forwrd DiscdI' in line:
            tcp_stack = 1
        """elif 'KBIn   PktIn  SizeIn   KBOut' in line:
            infiniband_stack = 1"""