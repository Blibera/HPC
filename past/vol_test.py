import csv
import re
import pandas as pd
import math

# 결정해주기
select = ["node01","node02"]
node = 4

for i in range (0,2):
    # Perf 관련 정의
    dstat_count = 0
    time_count = 1
    perf_full_text = ""
    """perf_column_noname = ["cpu0 usage:usr","cpu0 usage:sys","cpu0 usage:idl","cpu0 usage:wai","cpu0 usage:stl","cpu1 usage:usr","cpu1 usage:sys","cpu1 usage:idl","cpu1 usage:wai","cpu1 usage:stl","cpu2 usage:usr","cpu2 usage:sys","cpu2 usage:idl","cpu2 usage:wai","cpu2 usage:stl","cpu3 usage:usr","cpu3 usage:sys","cpu3 usage:idl","cpu3 usage:wai","cpu3 usage:stl","cpu4 usage:usr","cpu4 usage:sys","cpu4 usage:idl","cpu4 usage:wai","cpu4 usage:stl","cpu5 usage:usr","cpu5 usage:sys","cpu5 usage:idl","cpu5 usage:wai","cpu5 usage:stl","cpu6 usage:usr","cpu6 usage:sys","cpu6 usage:idl","cpu6 usage:wai","cpu6 usage:stl","cpu7 usage:usr","cpu7 usage:sys","cpu7 usage:idl","cpu7 usage:wai","cpu7 usage:stl","read","writ","recv","send","int","csw","run","blk","new","used","free","buff","cach","1m","5m","15m","read","writ"]"""
    perf_column_noname = ["cpu0 usage:usr", "cpu0 usage:sys", "cpu0 usage:idl", "cpu0 usage:wai", "cpu0 usage:stl",
                          "cpu1 usage:usr", "cpu1 usage:sys", "cpu1 usage:idl", "cpu1 usage:wai", "cpu1 usage:stl",
                          "cpu2 usage:usr", "cpu2 usage:sys", "cpu2 usage:idl", "cpu2 usage:wai", "cpu2 usage:stl",
                          "cpu3 usage:usr", "cpu3 usage:sys", "cpu3 usage:idl", "cpu3 usage:wai", "cpu3 usage:stl",
                          "total cpu usage:usr", "total cpu usage:sys", "total cpu usage:idl", "total cpu usage:wai", "total cpu usage:stl",
                          "read", "writ", "recv", "send", "in", "out" "int", "csw", "run", "blk", "new", "used", "free", "buff",
                          "cach", "swap_used", "swap_free","1m", "5m", "15m", "I/O_read", "I/O_writ"]

    perf_column_name =[]
    a = "C:/Users/Slayer/Desktop/연구실 자료/Kisti 관련/프로파일링 데이터/" + str(select[i]) + "_" + str(node) + "_dstat.csv"
    f = open(a, 'r')

    b = "C:/Users/Slayer/Desktop/연구실 자료/Kisti 관련/프로파일링 데이터/전처리/" + str(select[i]) + "_" + str(node) + "_dstat.csv"
    ff = open(b,'w', newline='')
    print(a)
    print(b)
    for j in range(0, 46):
        tol = str(select[i]) + "_" + str(perf_column_noname[j])
        perf_column_name.append(tol)
    write = csv.writer(ff)
    write.writerow(perf_column_name)
    while True:
        line = f.readline()
        if not line: break
        add = []
        if dstat_count == 0:
            dstat_count = 1
        else:
            for k in range(0, 46):


                if k > 37 and k < 42:

                    tol = line.split(',')[k]
                    tol = tol.strip()
                    if "." in tol:
                        tol = tol.split('.')[0]
                    tol = int(tol)
                    add.append(tol)
                elif k>26 and k <29:
                    tol = line.split(',')[k]
                    if "." in tol:
                        tol = tol.split('.')[0]
                    tol = tol.strip()
                    tol = int(tol)
                    add.append(tol)
                else:
                    tol = line.split(',')[k]
                    tol = tol.strip()
                    tol = float(tol)
                    add.append(tol)

            write.writerow(add)
"""
for i in range (0,1):

    a = pd.read_csv("C:/Users/Slayer/Desktop/연구실 자료/Kisti 관련/프로파일링 데이터/전처리/node01_" + str(node) + "_dstat.csv")
    b = pd.read_csv("C:/Users/Slayer/Desktop/연구실 자료/Kisti 관련/프로파일링 데이터/전처리/node02_" + str(node) + "_dstat.csv")
    merged = pd.merge(a,b, left_on="node01_cpu0 usage:usr", right_on="node02_cpu0 usage:usr")

    merged = pd.DataFrame(merged)

    merged.to_csv("C:/Users/Slayer/Desktop/연구실 자료/Kisti 관련/프로파일링 데이터/전처리/Merge_" + str(node) + "_dstat.csv",header=True,index=False)

"""

