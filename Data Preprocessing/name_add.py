import csv
import re
f = open("C:/Users/Slayer/Desktop/연구실 자료/Kisti 관련/Performance Analysis/3차 전처리/활용 데이터/dstat.csv", 'r', encoding='UTF8')
ff = open("C:/Users/Slayer/Desktop/연구실 자료/Kisti 관련/Performance Analysis/3차 전처리/이름파일/dstat_name.csv", "w",newline='', encoding='UTF8')

add = []
check = 0
name = ["User","Nice","Sys","Wait","IRQ","Soft","Steal","Guest","NiceG","Idle","CPUs","Intr","Ctxsw","Proc","RunQ","Run","Avg1","Avg5","Avg15","RunT","BlkT","KBRead","RMerged","Reads","SizeKB","KBWrite","WMerged","Writes","SizeKB","Reads","Writes","Meta","Comm","UDP","TCP","TCPConn","BadAuth","BadClnt","Reads","Writes","Meta","Comm","Retrans","Authref","Number","Unused","Alloc","MaxPct","Number","Total","Used","Free","Buff","Cached","Slab","Mapped","Anon","AnonH","Commit","Locked","Inact","Total","Used","Free","In","Out","Fault","MajFt","In","Out","1Pg","2Pgs","4Pgs","8Pgs","16Pgs","32Pgs","64Pgs","128Pgs","256Pgs","512Pgs","1024Pgs","KBIn","PktIn","SizeIn","MultI","CmpI","ErrsI","KBOut","PktOut","SizeO","CmpO","ErrsO","Used","Inuse","Orphan","Tw","Alloc","Mem","Inuse","Inuse","Inuse","Mem","Receiv","Delivr","Forwrd","DiscdI","InvAdd","Sent","DiscrO","ReasRq","ReasOK","FragOK","FragCr","ActOpn","PasOpn","Failed","ResetR","Estab","SegIn","SegOut","SegRtn","SegBad","SegRes","InDgm","OutDgm","NoPort","Errors","Recvd","FailI","UnreI","EchoI","ReplI","Trans","FailO","UnreO","EchoO","ReplO"]


add.append("Application")
print(len(name))
write = csv.writer(ff)
for i in range(len(name)):
    tol = "dstat_" + str(name[i])
    add.append(tol)
write.writerow(add)
while True:
    line = f.readline()
    add = []
    if not line: break
    if check == 0:
        count = line.count(',')
        check = 1
    else:
        for i in range(count+1):
            tol = line.split(',')[i]
            tol = tol.strip()
            add.append(tol)
        write.writerow(add)
