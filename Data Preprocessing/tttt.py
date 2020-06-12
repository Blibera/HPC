import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.metrics import accuracy_score
import re
import csv
name_list = "Perf_node01_branch-instructions	Perf_node01_ branch-misses	Perf_node01_ bus-cycles	Perf_node01_ cache-misses	Perf_node01_ cache-references	Perf_node01_ cpu-cycles	Perf_node01_ instructions	Perf_node01_ ref-cycles	Perf_node01_ context-switches	Perf_node01_ cpu-clock	Perf_node01_ cpu-migrations	Perf_node01_ major-faults	Perf_node01_ minor-faults	Perf_node01_ page-faults	Perf_node01_ task-clock	Perf_node01_ L1-dcache-load-misses	Perf_node01_ L1-icache-load-misses	Perf_node01_ L1-icache-loads	Perf_node01_ LLC-loads	Perf_node01_ LLC-stores	Perf_node01_ branch-load-misses	Perf_node01_ branch-loads	Perf_node01_ dTLB-load-misses	Perf_node01_ iTLB-load-misses	Perf_node01_ iTLB-loads	Perf_node01_ cpu/branch-instructions/	Perf_node01_ cpu/branch-misses/	Perf_node01_ cpu/bus-cycles/	Perf_node01_ cpu/cache-misses/	Perf_node01_ cpu/cache-references/	Perf_node01_ cpu/cpu-cycles/	Perf_node01_ cpu/instructions/	Perf_node01_ msr/aperf/	Perf_node01_ msr/mperf/	Perf_node01_ msr/smi/	Perf_node01_ msr/tsc/	Perf_node01_ power/energy-pkg/	Perf_node01_ power/energy-ram/	Perf_node01_ cpu/ref-cycles/	Perf_node01_ power/energy-pkg/	Perf_node01_ power/energy-ram/"
f = open("C:/Users/DI_Lab/Desktop/20년도 Kisti 과제/knl_Data/knl01,2_perf_분산제거(1,2통합).csv", 'r', encoding='UTF8')

line = f.readline()
line = re.sub(' ','',line)
line = re.sub('-','_',line)
line = re.sub('/','_',line)
save_file = open("C:/Users/DI_Lab/Desktop/20년도 Kisti 과제/knl_Data/dawdawdaw.csv", 'w', encoding='UTF8',newline='')

save_column = []
for i in range(line.count(',')):
    tol = line.split(',')[i]
    save_column.append(tol)

write = csv.writer(save_file)
write.writerow(save_column)
print(line)