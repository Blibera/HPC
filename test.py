import csv
import re

f_disk = open("C:/Users/Slayer/Desktop/공유할것/NPB_log_knl02_64/NPB_EP_log/pidstat_tswch/pidstat_tswch_2018-08-02.csv", 'r')
# 변수
stack = 0
string = ""
add = []
loop_12 = 0
while True:
    line_disk = f_disk.readline()
    comma_count_disk = line_disk.count(',')
    if not line_disk: break
    print(line_disk)