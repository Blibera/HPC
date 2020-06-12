import csv
import re
# slx
#name = ["branch-instructions","branch-misses","bus-cycles","cache-misses","cache-references","cpu-cycles","instructions","ref-cycles","alignment-faults","context-switches","cpu-clock","cpu-migrations","dummy","emulation-faults","major-faults","minor-faults","page-faults","task-clock","L1-dcache-load-misses","L1-icache-load-misses","L1-icache-loads","LLC-loads","LLC-stores","branch-load-misses","branch-loads","dTLB-load-misses","iTLB-load-misses","iTLB-loads","cpu/branch-instructions/","cpu/branch-misses/","cpu/bus-cycles/","cpu/cache-misses/","cpu/cache-references/","cpu/cpu-cycles/","cpu/instructions/","intel_bts//","msr/aperf/","msr/mperf/","msr/smi/","msr/tsc/","cpu/ref-cycles/","power/energy-pkg/","power/energy-ram/","power/energy-cores/"]

# knl
name = ["branch-instructions","branch-misses","bus-cycles","cache-misses","cache-references","cpu-cycles","instructions","ref-cycles","alignment-faults","context-switches","cpu-clock","cpu-migrations","dummy","emulation-faults","major-faults","minor-faults","page-faults","task-clock","L1-dcache-load-misses","L1-icache-load-misses","L1-icache-loads","LLC-loads","LLC-stores","branch-load-misses","branch-loads","dTLB-load-misses","iTLB-load-misses","iTLB-loads","cpu/branch-instructions/","cpu/branch-misses/","cpu/bus-cycles/","cpu/cache-misses/","cpu/cache-references/","cpu/cpu-cycles/","cpu/instructions/","intel_bts//","msr/aperf/","msr/mperf/","msr/smi/","msr/tsc/","cpu/ref-cycles/","power/energy-pkg/","power/energy-ram/"]

# epyc
#name =["branch-instructions","branch-misses","bus-cycles","cache-misses","cache-references","cpu-cycles","instructions","ref-cycles","alignment-faults","context-switches","cpu-clock","cpu-migrations","dummy","emulation-faults","major-faults","minor-faults","page-faults","task-clock","L1-dcache-load-misses","L1-icache-load-misses","L1-icache-loads","LLC-loads","LLC-stores","branch-load-misses","branch-loads","dTLB-load-misses","iTLB-load-misses","iTLB-loads","cpu/branch-instructions/","cpu/branch-misses/","cpu/cache-misses/","cpu/cache-references/","cpu/cpu-cycles/","cpu/instructions/","msr/aperf/","msr/mperf/","msr/tsc/"]

print(len(name))

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
stack = 0
add = []
k = 1
for l in range(1, 2):
    k = 1
    node = str(l).zfill(2)
    print(node)

    #Slx
    #f = open("C:/Users/DI_Lab/Desktop/Paper_Data/Slx/Core64/Single/전처리 이전 데이터/slx" + str(node) + "_perf.txt", 'r', encoding='UTF8')
    #ff = open("C:/Users/DI_Lab/Desktop/Paper_Data/Slx/Core64/Single/1차 전처리(CSV화)/slx" + str(node) + "_perf.csv", "w",newline='')

    #knl
    f = open("C:/Users/DI_Lab/Desktop/Paper_Data/Knl/Cache/Core64/Single/전처리 이전 데이터/knl" + str(node) + "_perf.txt", 'r')
    ff = open("C:/Users/DI_Lab/Desktop/Paper_Data/Knl/Cache/Core64/Single/1차 전처리(CSV화)/knl" + str(node) + "_perf.csv", "w",newline='')

    #epyc
    #f = open("C:/Users/DI_Lab/Desktop/Paper_Data/Epyc/Core64/Single/전처리 이전 데이터/Epyc" + str(node) + "_perf.txt", 'r')
    #ff = open("C:/Users/DI_Lab/Desktop/Paper_Data/Epyc/Core64/Single/1차 전처리(CSV화)/Epyc" + str(node) + "_perf.csv", "w",newline='')

    for i in range(len(name)):
        tol = "Perf_node" + str(node) + str("_") + str(name[i])
        add.append(tol)
    write = csv.writer(ff)
    write.writerow(add)
    add = []
    while True:
        line = f.readline()
        line = re.sub(',','',line)
        if not line: break


        if stack == 1:
            if 'counts' in line:
                pass

            #slx31
            #knl
            elif "counted" in line:
                tol = "NULL"
                add.append(tol)
                k = k + 1

            elif "supported>" in line:
                add.append(0)
                k = k + 1

            elif k == len(name):
                line = split(line)
                tol = line.split(',')[2]
                tol = float(tol)
                add.append(tol)
                k=1
                write.writerow(add)
                add = []

            else:
                line = split(line)
                tol = line.split(',')[2]
                tol = float(tol)
                add.append(tol)
                k = k + 1

        if 'events' in line:
            stack = 1
    stack = 0