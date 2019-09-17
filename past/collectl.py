import csv
import re

f_1 = open("C:/Users/Slayer/Desktop/NPB_19_18_45/sp.c/000_collectl_log.txt", 'r')
f_2 = open("C:/Users/Slayer/Desktop/NPB_19_18_45/sp.c/001_collectl_log.txt", 'r')
f_3 = open("C:/Users/Slayer/Desktop/NPB_19_18_45/sp.c/002_collectl_log.txt", 'r')
f_4 = open("C:/Users/Slayer/Desktop/NPB_19_18_45/sp.c/003_collectl_log.txt", 'r')
f_5 = open("C:/Users/Slayer/Desktop/NPB_19_18_45/sp.c/004_collectl_log.txt", 'r')
f = open("C:/Users/Slayer/Desktop/NPB_19_18_45/sp_collect.csv", 'w',newline='')

name = ['User','Nice','Sys','Wait','IRQ','Soft','Steal','Guest','NiceG','Idle','CPUs','Intr','Ctxsw',
        'Proc','RunQ','Run','Avg1','Avg5','Avg15','RunT','BlkT','interrupt',
        'KBRead','RMerged','Reads','SizeKB','KBWrite','WMerged','Writes','SizeKB',
        'KBIn','PktIn','SizeIn','MultI','CmpI','ErrsI','KBOut','PktOut','SizeO','CmpO','ErrsO']

write = csv.writer(f)
write.writerow(name)

add = []

cpu_stack = 0
inter_stack = 0
disk_stack = 0
network_stack = 0

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
    elif count_m == 0:
        text = int(text)
    elif count_m == 1:
        text = re.sub('M', '', text)
        text = int(text)
        text = text * 1000
    return text


while True:
    line = f_1.readline()
    if not line: break
    tol = 0
    num = 0

    # 스택 반환
    if cpu_stack == 1:
        line = split(line)
        for i in range(1,22):
            tol = line.split(',')[i]
            tol = re.sub('\n','',tol)
            tol = int_num(tol)
            add.append(tol)
        cpu_stack = 0

    elif inter_stack == 1:
        line = split(line)
        for i in range(1,272):
            tol = line.split(',')[i]
            tol = int(tol)
            num = num + tol
        add.append(num)
        inter_stack = 0

    elif disk_stack == 1:
        line = split(line)
        for i in range(1,9):
            tol = line.split(',')[i]
            tol = int(tol)
            add.append(tol)
        disk_stack = 0

    elif network_stack == 1:
        line = split(line)
        for i in range(1,12):
            tol = line.split(',')[i]
            tol = int(tol)
            add.append(tol)
        write.writerow(add)
        add = []
        network_stack = 0

    # 스택작업
    if 'User  Nice   Sys  Wait   IRQ  Soft Steal Guest NiceG  Idle  CPUs  Intr  Ctxsw  Proc  RunQ   Run   Avg1  Avg5 Avg15 RunT BlkT' in line:
        cpu_stack = 1
    elif 'Cpu0   Cpu1   Cpu2   Cpu3   Cpu4   Cpu5   Cpu6   Cpu7   Cpu8   Cpu9  Cpu10  Cpu11  Cpu12  Cpu13  Cpu14  Cpu15  Cpu16  Cpu17  Cpu18  Cpu19  Cpu20  Cpu21  Cpu22  Cpu23  Cpu24  Cpu25  Cpu26  Cpu27  Cpu28  Cpu29  Cpu30  Cpu31  Cpu32  Cpu33  Cpu34  Cpu35  Cpu36  Cpu37  Cpu38  Cpu39  Cpu40  Cpu41  Cpu42  Cpu43  Cpu44  Cpu45  Cpu46  Cpu47  Cpu48  Cpu49  Cpu50  Cpu51  Cpu52  Cpu53  Cpu54  Cpu55  Cpu56  Cpu57  Cpu58  Cpu59  Cpu60  Cpu61  Cpu62  Cpu63  Cpu64  Cpu65  Cpu66  Cpu67  Cpu68  Cpu69  Cpu70  Cpu71  Cpu72  Cpu73  Cpu74  Cpu75  Cpu76  Cpu77  Cpu78  Cpu79  Cpu80  Cpu81  Cpu82  Cpu83  Cpu84  Cpu85  Cpu86  Cpu87  Cpu88  Cpu89  Cpu90  Cpu91  Cpu92  Cpu93  Cpu94  Cpu95  Cpu96  Cpu97  Cpu98  Cpu99 Cpu100 Cpu101 Cpu102 Cpu103 Cpu104 Cpu105 Cpu106 Cpu107 Cpu108 Cpu109 Cpu110 Cpu111 Cpu112 Cpu113 Cpu114 Cpu115 Cpu116 Cpu117 Cpu118 Cpu119 Cpu120 Cpu121 Cpu122 Cpu123 Cpu124 Cpu125 Cpu126 Cpu127 Cpu128 Cpu129 Cpu130 Cpu131 Cpu132 Cpu133 Cpu134 Cpu135 Cpu136 Cpu137 Cpu138 Cpu139 Cpu140 Cpu141 Cpu142 Cpu143 Cpu144 Cpu145 Cpu146 Cpu147 Cpu148 Cpu149 Cpu150 Cpu151 Cpu152 Cpu153 Cpu154 Cpu155 Cpu156 Cpu157 Cpu158 Cpu159 Cpu160 Cpu161 Cpu162 Cpu163 Cpu164 Cpu165 Cpu166 Cpu167 Cpu168 Cpu169 Cpu170 Cpu171 Cpu172 Cpu173 Cpu174 Cpu175 Cpu176 Cpu177 Cpu178 Cpu179 Cpu180 Cpu181 Cpu182 Cpu183 Cpu184 Cpu185 Cpu186 Cpu187 Cpu188 Cpu189 Cpu190 Cpu191 Cpu192 Cpu193 Cpu194 Cpu195 Cpu196 Cpu197 Cpu198 Cpu199 Cpu200 Cpu201 Cpu202 Cpu203 Cpu204 Cpu205 Cpu206 Cpu207 Cpu208 Cpu209 Cpu210 Cpu211 Cpu212 Cpu213 Cpu214 Cpu215 Cpu216 Cpu217 Cpu218 Cpu219 Cpu220 Cpu221 Cpu222 Cpu223 Cpu224 Cpu225 Cpu226 Cpu227 Cpu228 Cpu229 Cpu230 Cpu231 Cpu232 Cpu233 Cpu234 Cpu235 Cpu236 Cpu237 Cpu238 Cpu239 Cpu240 Cpu241 Cpu242 Cpu243 Cpu244 Cpu245 Cpu246 Cpu247 Cpu248 Cpu249 Cpu250 Cpu251 Cpu252 Cpu253 Cpu254 Cpu255 Cpu256 Cpu257 Cpu258 Cpu259 Cpu260 Cpu261 Cpu262 Cpu263 Cpu264 Cpu265 Cpu266 Cpu267 Cpu268 Cpu269 Cpu270 Cpu271' in line:
        inter_stack = 1
    elif 'KBRead RMerged  Reads SizeKB  KBWrite WMerged Writes SizeKB' in line:
        disk_stack = 1
    elif 'KBIn  PktIn SizeIn  MultI   CmpI  ErrsI  KBOut PktOut  SizeO   CmpO  ErrsO' in line:
        network_stack = 1

while True:
    line = f_2.readline()
    if not line: break
    tol = 0
    num = 0

    # 스택 반환
    if cpu_stack == 1:
        line = split(line)
        for i in range(1,22):
            tol = line.split(',')[i]
            tol = re.sub('\n','',tol)
            tol = int_num(tol)
            add.append(tol)
        cpu_stack = 0

    elif inter_stack == 1:
        line = split(line)
        for i in range(1,272):
            tol = line.split(',')[i]
            tol = int(tol)
            num = num + tol
        add.append(num)
        inter_stack = 0

    elif disk_stack == 1:
        line = split(line)
        for i in range(1,9):
            tol = line.split(',')[i]
            tol = int(tol)
            add.append(tol)
        disk_stack = 0

    elif network_stack == 1:
        line = split(line)
        for i in range(1,12):
            tol = line.split(',')[i]
            tol = int(tol)
            add.append(tol)
        write.writerow(add)
        add = []
        network_stack = 0

    # 스택작업
    if 'User  Nice   Sys  Wait   IRQ  Soft Steal Guest NiceG  Idle  CPUs  Intr  Ctxsw  Proc  RunQ   Run   Avg1  Avg5 Avg15 RunT BlkT' in line:
        cpu_stack = 1
    elif 'Cpu0   Cpu1   Cpu2   Cpu3   Cpu4   Cpu5   Cpu6   Cpu7   Cpu8   Cpu9  Cpu10  Cpu11  Cpu12  Cpu13  Cpu14  Cpu15  Cpu16  Cpu17  Cpu18  Cpu19  Cpu20  Cpu21  Cpu22  Cpu23  Cpu24  Cpu25  Cpu26  Cpu27  Cpu28  Cpu29  Cpu30  Cpu31  Cpu32  Cpu33  Cpu34  Cpu35  Cpu36  Cpu37  Cpu38  Cpu39  Cpu40  Cpu41  Cpu42  Cpu43  Cpu44  Cpu45  Cpu46  Cpu47  Cpu48  Cpu49  Cpu50  Cpu51  Cpu52  Cpu53  Cpu54  Cpu55  Cpu56  Cpu57  Cpu58  Cpu59  Cpu60  Cpu61  Cpu62  Cpu63  Cpu64  Cpu65  Cpu66  Cpu67  Cpu68  Cpu69  Cpu70  Cpu71  Cpu72  Cpu73  Cpu74  Cpu75  Cpu76  Cpu77  Cpu78  Cpu79  Cpu80  Cpu81  Cpu82  Cpu83  Cpu84  Cpu85  Cpu86  Cpu87  Cpu88  Cpu89  Cpu90  Cpu91  Cpu92  Cpu93  Cpu94  Cpu95  Cpu96  Cpu97  Cpu98  Cpu99 Cpu100 Cpu101 Cpu102 Cpu103 Cpu104 Cpu105 Cpu106 Cpu107 Cpu108 Cpu109 Cpu110 Cpu111 Cpu112 Cpu113 Cpu114 Cpu115 Cpu116 Cpu117 Cpu118 Cpu119 Cpu120 Cpu121 Cpu122 Cpu123 Cpu124 Cpu125 Cpu126 Cpu127 Cpu128 Cpu129 Cpu130 Cpu131 Cpu132 Cpu133 Cpu134 Cpu135 Cpu136 Cpu137 Cpu138 Cpu139 Cpu140 Cpu141 Cpu142 Cpu143 Cpu144 Cpu145 Cpu146 Cpu147 Cpu148 Cpu149 Cpu150 Cpu151 Cpu152 Cpu153 Cpu154 Cpu155 Cpu156 Cpu157 Cpu158 Cpu159 Cpu160 Cpu161 Cpu162 Cpu163 Cpu164 Cpu165 Cpu166 Cpu167 Cpu168 Cpu169 Cpu170 Cpu171 Cpu172 Cpu173 Cpu174 Cpu175 Cpu176 Cpu177 Cpu178 Cpu179 Cpu180 Cpu181 Cpu182 Cpu183 Cpu184 Cpu185 Cpu186 Cpu187 Cpu188 Cpu189 Cpu190 Cpu191 Cpu192 Cpu193 Cpu194 Cpu195 Cpu196 Cpu197 Cpu198 Cpu199 Cpu200 Cpu201 Cpu202 Cpu203 Cpu204 Cpu205 Cpu206 Cpu207 Cpu208 Cpu209 Cpu210 Cpu211 Cpu212 Cpu213 Cpu214 Cpu215 Cpu216 Cpu217 Cpu218 Cpu219 Cpu220 Cpu221 Cpu222 Cpu223 Cpu224 Cpu225 Cpu226 Cpu227 Cpu228 Cpu229 Cpu230 Cpu231 Cpu232 Cpu233 Cpu234 Cpu235 Cpu236 Cpu237 Cpu238 Cpu239 Cpu240 Cpu241 Cpu242 Cpu243 Cpu244 Cpu245 Cpu246 Cpu247 Cpu248 Cpu249 Cpu250 Cpu251 Cpu252 Cpu253 Cpu254 Cpu255 Cpu256 Cpu257 Cpu258 Cpu259 Cpu260 Cpu261 Cpu262 Cpu263 Cpu264 Cpu265 Cpu266 Cpu267 Cpu268 Cpu269 Cpu270 Cpu271' in line:
        inter_stack = 1
    elif 'KBRead RMerged  Reads SizeKB  KBWrite WMerged Writes SizeKB' in line:
        disk_stack = 1
    elif 'KBIn  PktIn SizeIn  MultI   CmpI  ErrsI  KBOut PktOut  SizeO   CmpO  ErrsO' in line:
        network_stack = 1

while True:
    line = f_3.readline()
    if not line: break
    tol = 0
    num = 0

    # 스택 반환
    if cpu_stack == 1:
        line = split(line)
        for i in range(1,22):
            tol = line.split(',')[i]
            tol = re.sub('\n','',tol)
            tol = int_num(tol)
            add.append(tol)
        cpu_stack = 0

    elif inter_stack == 1:
        line = split(line)
        for i in range(1,272):
            tol = line.split(',')[i]
            tol = int(tol)
            num = num + tol
        add.append(num)
        inter_stack = 0

    elif disk_stack == 1:
        line = split(line)
        for i in range(1,9):
            tol = line.split(',')[i]
            tol = int(tol)
            add.append(tol)
        disk_stack = 0

    elif network_stack == 1:
        line = split(line)
        for i in range(1,12):
            tol = line.split(',')[i]
            tol = int(tol)
            add.append(tol)
        write.writerow(add)
        add = []
        network_stack = 0

    # 스택작업
    if 'User  Nice   Sys  Wait   IRQ  Soft Steal Guest NiceG  Idle  CPUs  Intr  Ctxsw  Proc  RunQ   Run   Avg1  Avg5 Avg15 RunT BlkT' in line:
        cpu_stack = 1
    elif 'Cpu0   Cpu1   Cpu2   Cpu3   Cpu4   Cpu5   Cpu6   Cpu7   Cpu8   Cpu9  Cpu10  Cpu11  Cpu12  Cpu13  Cpu14  Cpu15  Cpu16  Cpu17  Cpu18  Cpu19  Cpu20  Cpu21  Cpu22  Cpu23  Cpu24  Cpu25  Cpu26  Cpu27  Cpu28  Cpu29  Cpu30  Cpu31  Cpu32  Cpu33  Cpu34  Cpu35  Cpu36  Cpu37  Cpu38  Cpu39  Cpu40  Cpu41  Cpu42  Cpu43  Cpu44  Cpu45  Cpu46  Cpu47  Cpu48  Cpu49  Cpu50  Cpu51  Cpu52  Cpu53  Cpu54  Cpu55  Cpu56  Cpu57  Cpu58  Cpu59  Cpu60  Cpu61  Cpu62  Cpu63  Cpu64  Cpu65  Cpu66  Cpu67  Cpu68  Cpu69  Cpu70  Cpu71  Cpu72  Cpu73  Cpu74  Cpu75  Cpu76  Cpu77  Cpu78  Cpu79  Cpu80  Cpu81  Cpu82  Cpu83  Cpu84  Cpu85  Cpu86  Cpu87  Cpu88  Cpu89  Cpu90  Cpu91  Cpu92  Cpu93  Cpu94  Cpu95  Cpu96  Cpu97  Cpu98  Cpu99 Cpu100 Cpu101 Cpu102 Cpu103 Cpu104 Cpu105 Cpu106 Cpu107 Cpu108 Cpu109 Cpu110 Cpu111 Cpu112 Cpu113 Cpu114 Cpu115 Cpu116 Cpu117 Cpu118 Cpu119 Cpu120 Cpu121 Cpu122 Cpu123 Cpu124 Cpu125 Cpu126 Cpu127 Cpu128 Cpu129 Cpu130 Cpu131 Cpu132 Cpu133 Cpu134 Cpu135 Cpu136 Cpu137 Cpu138 Cpu139 Cpu140 Cpu141 Cpu142 Cpu143 Cpu144 Cpu145 Cpu146 Cpu147 Cpu148 Cpu149 Cpu150 Cpu151 Cpu152 Cpu153 Cpu154 Cpu155 Cpu156 Cpu157 Cpu158 Cpu159 Cpu160 Cpu161 Cpu162 Cpu163 Cpu164 Cpu165 Cpu166 Cpu167 Cpu168 Cpu169 Cpu170 Cpu171 Cpu172 Cpu173 Cpu174 Cpu175 Cpu176 Cpu177 Cpu178 Cpu179 Cpu180 Cpu181 Cpu182 Cpu183 Cpu184 Cpu185 Cpu186 Cpu187 Cpu188 Cpu189 Cpu190 Cpu191 Cpu192 Cpu193 Cpu194 Cpu195 Cpu196 Cpu197 Cpu198 Cpu199 Cpu200 Cpu201 Cpu202 Cpu203 Cpu204 Cpu205 Cpu206 Cpu207 Cpu208 Cpu209 Cpu210 Cpu211 Cpu212 Cpu213 Cpu214 Cpu215 Cpu216 Cpu217 Cpu218 Cpu219 Cpu220 Cpu221 Cpu222 Cpu223 Cpu224 Cpu225 Cpu226 Cpu227 Cpu228 Cpu229 Cpu230 Cpu231 Cpu232 Cpu233 Cpu234 Cpu235 Cpu236 Cpu237 Cpu238 Cpu239 Cpu240 Cpu241 Cpu242 Cpu243 Cpu244 Cpu245 Cpu246 Cpu247 Cpu248 Cpu249 Cpu250 Cpu251 Cpu252 Cpu253 Cpu254 Cpu255 Cpu256 Cpu257 Cpu258 Cpu259 Cpu260 Cpu261 Cpu262 Cpu263 Cpu264 Cpu265 Cpu266 Cpu267 Cpu268 Cpu269 Cpu270 Cpu271' in line:
        inter_stack = 1
    elif 'KBRead RMerged  Reads SizeKB  KBWrite WMerged Writes SizeKB' in line:
        disk_stack = 1
    elif 'KBIn  PktIn SizeIn  MultI   CmpI  ErrsI  KBOut PktOut  SizeO   CmpO  ErrsO' in line:
        network_stack = 1

while True:
    line = f_4.readline()
    if not line: break
    tol = 0
    num = 0

    # 스택 반환
    if cpu_stack == 1:
        line = split(line)
        for i in range(1,22):
            tol = line.split(',')[i]
            tol = re.sub('\n','',tol)
            tol = int_num(tol)
            add.append(tol)
        cpu_stack = 0

    elif inter_stack == 1:
        line = split(line)
        for i in range(1,272):
            tol = line.split(',')[i]
            tol = int(tol)
            num = num + tol
        add.append(num)
        inter_stack = 0

    elif disk_stack == 1:
        line = split(line)
        for i in range(1,9):
            tol = line.split(',')[i]
            tol = int(tol)
            add.append(tol)
        disk_stack = 0

    elif network_stack == 1:
        line = split(line)
        for i in range(1,12):
            tol = line.split(',')[i]
            tol = int(tol)
            add.append(tol)
        write.writerow(add)
        add = []
        network_stack = 0

    # 스택작업
    if 'User  Nice   Sys  Wait   IRQ  Soft Steal Guest NiceG  Idle  CPUs  Intr  Ctxsw  Proc  RunQ   Run   Avg1  Avg5 Avg15 RunT BlkT' in line:
        cpu_stack = 1
    elif 'Cpu0   Cpu1   Cpu2   Cpu3   Cpu4   Cpu5   Cpu6   Cpu7   Cpu8   Cpu9  Cpu10  Cpu11  Cpu12  Cpu13  Cpu14  Cpu15  Cpu16  Cpu17  Cpu18  Cpu19  Cpu20  Cpu21  Cpu22  Cpu23  Cpu24  Cpu25  Cpu26  Cpu27  Cpu28  Cpu29  Cpu30  Cpu31  Cpu32  Cpu33  Cpu34  Cpu35  Cpu36  Cpu37  Cpu38  Cpu39  Cpu40  Cpu41  Cpu42  Cpu43  Cpu44  Cpu45  Cpu46  Cpu47  Cpu48  Cpu49  Cpu50  Cpu51  Cpu52  Cpu53  Cpu54  Cpu55  Cpu56  Cpu57  Cpu58  Cpu59  Cpu60  Cpu61  Cpu62  Cpu63  Cpu64  Cpu65  Cpu66  Cpu67  Cpu68  Cpu69  Cpu70  Cpu71  Cpu72  Cpu73  Cpu74  Cpu75  Cpu76  Cpu77  Cpu78  Cpu79  Cpu80  Cpu81  Cpu82  Cpu83  Cpu84  Cpu85  Cpu86  Cpu87  Cpu88  Cpu89  Cpu90  Cpu91  Cpu92  Cpu93  Cpu94  Cpu95  Cpu96  Cpu97  Cpu98  Cpu99 Cpu100 Cpu101 Cpu102 Cpu103 Cpu104 Cpu105 Cpu106 Cpu107 Cpu108 Cpu109 Cpu110 Cpu111 Cpu112 Cpu113 Cpu114 Cpu115 Cpu116 Cpu117 Cpu118 Cpu119 Cpu120 Cpu121 Cpu122 Cpu123 Cpu124 Cpu125 Cpu126 Cpu127 Cpu128 Cpu129 Cpu130 Cpu131 Cpu132 Cpu133 Cpu134 Cpu135 Cpu136 Cpu137 Cpu138 Cpu139 Cpu140 Cpu141 Cpu142 Cpu143 Cpu144 Cpu145 Cpu146 Cpu147 Cpu148 Cpu149 Cpu150 Cpu151 Cpu152 Cpu153 Cpu154 Cpu155 Cpu156 Cpu157 Cpu158 Cpu159 Cpu160 Cpu161 Cpu162 Cpu163 Cpu164 Cpu165 Cpu166 Cpu167 Cpu168 Cpu169 Cpu170 Cpu171 Cpu172 Cpu173 Cpu174 Cpu175 Cpu176 Cpu177 Cpu178 Cpu179 Cpu180 Cpu181 Cpu182 Cpu183 Cpu184 Cpu185 Cpu186 Cpu187 Cpu188 Cpu189 Cpu190 Cpu191 Cpu192 Cpu193 Cpu194 Cpu195 Cpu196 Cpu197 Cpu198 Cpu199 Cpu200 Cpu201 Cpu202 Cpu203 Cpu204 Cpu205 Cpu206 Cpu207 Cpu208 Cpu209 Cpu210 Cpu211 Cpu212 Cpu213 Cpu214 Cpu215 Cpu216 Cpu217 Cpu218 Cpu219 Cpu220 Cpu221 Cpu222 Cpu223 Cpu224 Cpu225 Cpu226 Cpu227 Cpu228 Cpu229 Cpu230 Cpu231 Cpu232 Cpu233 Cpu234 Cpu235 Cpu236 Cpu237 Cpu238 Cpu239 Cpu240 Cpu241 Cpu242 Cpu243 Cpu244 Cpu245 Cpu246 Cpu247 Cpu248 Cpu249 Cpu250 Cpu251 Cpu252 Cpu253 Cpu254 Cpu255 Cpu256 Cpu257 Cpu258 Cpu259 Cpu260 Cpu261 Cpu262 Cpu263 Cpu264 Cpu265 Cpu266 Cpu267 Cpu268 Cpu269 Cpu270 Cpu271' in line:
        inter_stack = 1
    elif 'KBRead RMerged  Reads SizeKB  KBWrite WMerged Writes SizeKB' in line:
        disk_stack = 1
    elif 'KBIn  PktIn SizeIn  MultI   CmpI  ErrsI  KBOut PktOut  SizeO   CmpO  ErrsO' in line:
        network_stack = 1

while True:
    line = f_5.readline()
    if not line: break
    tol = 0
    num = 0

    # 스택 반환
    if cpu_stack == 1:
        line = split(line)
        for i in range(1,22):
            tol = line.split(',')[i]
            tol = re.sub('\n','',tol)
            tol = int_num(tol)
            add.append(tol)
        cpu_stack = 0

    elif inter_stack == 1:
        line = split(line)
        for i in range(1,272):
            tol = line.split(',')[i]
            tol = int(tol)
            num = num + tol
        add.append(num)
        inter_stack = 0

    elif disk_stack == 1:
        line = split(line)
        for i in range(1,9):
            tol = line.split(',')[i]
            tol = int(tol)
            add.append(tol)
        disk_stack = 0

    elif network_stack == 1:
        line = split(line)
        for i in range(1,12):
            tol = line.split(',')[i]
            tol = int(tol)
            add.append(tol)
        write.writerow(add)
        add = []
        network_stack = 0

    # 스택작업
    if 'User  Nice   Sys  Wait   IRQ  Soft Steal Guest NiceG  Idle  CPUs  Intr  Ctxsw  Proc  RunQ   Run   Avg1  Avg5 Avg15 RunT BlkT' in line:
        cpu_stack = 1
    elif 'Cpu0   Cpu1   Cpu2   Cpu3   Cpu4   Cpu5   Cpu6   Cpu7   Cpu8   Cpu9  Cpu10  Cpu11  Cpu12  Cpu13  Cpu14  Cpu15  Cpu16  Cpu17  Cpu18  Cpu19  Cpu20  Cpu21  Cpu22  Cpu23  Cpu24  Cpu25  Cpu26  Cpu27  Cpu28  Cpu29  Cpu30  Cpu31  Cpu32  Cpu33  Cpu34  Cpu35  Cpu36  Cpu37  Cpu38  Cpu39  Cpu40  Cpu41  Cpu42  Cpu43  Cpu44  Cpu45  Cpu46  Cpu47  Cpu48  Cpu49  Cpu50  Cpu51  Cpu52  Cpu53  Cpu54  Cpu55  Cpu56  Cpu57  Cpu58  Cpu59  Cpu60  Cpu61  Cpu62  Cpu63  Cpu64  Cpu65  Cpu66  Cpu67  Cpu68  Cpu69  Cpu70  Cpu71  Cpu72  Cpu73  Cpu74  Cpu75  Cpu76  Cpu77  Cpu78  Cpu79  Cpu80  Cpu81  Cpu82  Cpu83  Cpu84  Cpu85  Cpu86  Cpu87  Cpu88  Cpu89  Cpu90  Cpu91  Cpu92  Cpu93  Cpu94  Cpu95  Cpu96  Cpu97  Cpu98  Cpu99 Cpu100 Cpu101 Cpu102 Cpu103 Cpu104 Cpu105 Cpu106 Cpu107 Cpu108 Cpu109 Cpu110 Cpu111 Cpu112 Cpu113 Cpu114 Cpu115 Cpu116 Cpu117 Cpu118 Cpu119 Cpu120 Cpu121 Cpu122 Cpu123 Cpu124 Cpu125 Cpu126 Cpu127 Cpu128 Cpu129 Cpu130 Cpu131 Cpu132 Cpu133 Cpu134 Cpu135 Cpu136 Cpu137 Cpu138 Cpu139 Cpu140 Cpu141 Cpu142 Cpu143 Cpu144 Cpu145 Cpu146 Cpu147 Cpu148 Cpu149 Cpu150 Cpu151 Cpu152 Cpu153 Cpu154 Cpu155 Cpu156 Cpu157 Cpu158 Cpu159 Cpu160 Cpu161 Cpu162 Cpu163 Cpu164 Cpu165 Cpu166 Cpu167 Cpu168 Cpu169 Cpu170 Cpu171 Cpu172 Cpu173 Cpu174 Cpu175 Cpu176 Cpu177 Cpu178 Cpu179 Cpu180 Cpu181 Cpu182 Cpu183 Cpu184 Cpu185 Cpu186 Cpu187 Cpu188 Cpu189 Cpu190 Cpu191 Cpu192 Cpu193 Cpu194 Cpu195 Cpu196 Cpu197 Cpu198 Cpu199 Cpu200 Cpu201 Cpu202 Cpu203 Cpu204 Cpu205 Cpu206 Cpu207 Cpu208 Cpu209 Cpu210 Cpu211 Cpu212 Cpu213 Cpu214 Cpu215 Cpu216 Cpu217 Cpu218 Cpu219 Cpu220 Cpu221 Cpu222 Cpu223 Cpu224 Cpu225 Cpu226 Cpu227 Cpu228 Cpu229 Cpu230 Cpu231 Cpu232 Cpu233 Cpu234 Cpu235 Cpu236 Cpu237 Cpu238 Cpu239 Cpu240 Cpu241 Cpu242 Cpu243 Cpu244 Cpu245 Cpu246 Cpu247 Cpu248 Cpu249 Cpu250 Cpu251 Cpu252 Cpu253 Cpu254 Cpu255 Cpu256 Cpu257 Cpu258 Cpu259 Cpu260 Cpu261 Cpu262 Cpu263 Cpu264 Cpu265 Cpu266 Cpu267 Cpu268 Cpu269 Cpu270 Cpu271' in line:
        inter_stack = 1
    elif 'KBRead RMerged  Reads SizeKB  KBWrite WMerged Writes SizeKB' in line:
        disk_stack = 1
    elif 'KBIn  PktIn SizeIn  MultI   CmpI  ErrsI  KBOut PktOut  SizeO   CmpO  ErrsO' in line:
        network_stack = 1
f.close()