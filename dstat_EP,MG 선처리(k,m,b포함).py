import re
import csv

f = open("C:/Users/Slayer/Desktop/공유할것/dstat_MG_D_64.txt", 'r')

ff = open('C:/Users/Slayer/Desktop/공유할것/dstat_MG_D_64_변수제거 선처리.csv', 'wt',newline='', encoding='utf-8')

wr = csv.writer(ff)
"""
frist = csv.DictWriter(ff,['<-------------','_---------------total cpu usage----------------------->','','','','','<-----dsk/total----->','','<---paging stat--->','','<---------load stat--------->','','','<-------------memory stat---------------->','','','','<total network stat>','','<---------process stat-------->','','','<------i/o stat------>','','<---swap stat--->','','<-----system----->'])
frist.writeheader()
"""

csvout = csv.DictWriter(ff,['usr','sys', 'idl', 'wai', 'hiq', 'siq', 'disk_read', 'disk_writ', 'paging_in', 'out', 'one_m', 'five_m', 'fifteen_m', 'memory_used', 'buff', 'cach', 'memory_free', 'recv', 'send', 'run', 'blk', 'new', 'io_read', 'io_writ', 'swap_used', 'swap_free','int', 'csw'])
csvout.writeheader()


def split(text):
    cleaned_text = re.sub('\|', ' ', text)
    cleaned_text = re.sub('         ', ',', cleaned_text)
    cleaned_text = re.sub('        ', ',', cleaned_text)
    cleaned_text = re.sub('       ', ',', cleaned_text)
    cleaned_text = re.sub('      ', ',', cleaned_text)
    cleaned_text = re.sub('     ', ',', cleaned_text)
    cleaned_text = re.sub('    ', ',', cleaned_text)
    cleaned_text = re.sub('   ', ',', cleaned_text)
    cleaned_text = re.sub('  ', ',', cleaned_text)
    cleaned_text = re.sub(' ', ',', cleaned_text)
    cleaned_text = re.sub('\\n', ',', cleaned_text)
    return cleaned_text

def clean_text(text):
    cleaned_text = re.sub('k', '', text)
    cleaned_text = re.sub('B', '', cleaned_text)
    cleaned_text = re.sub('M', '', cleaned_text)
    cleaned_text = re.sub('G', '', cleaned_text)
    return cleaned_text
stack = 1

def K_text(text):
    count_k = 0
    count_b = 0
    count_k = text.count('k')
    count_b = text.count('B')
    if count_k == 0:
        pass
    else:
        text = re.sub('k', '', text)
        text = int(text)
        text = text*1000
    if count_b == 0:
        pass
    else:
        text = re.sub('B', '', text)
        text = int(text)
        text = text * 1000
    return text

def M_G(text):
    count_m = 0
    count_g = 0
    count_m = text.count("M")
    count_g = text.count("G")

    if count_m == 0:
        pass
    else:
        text = re.sub("M","",text)
        text = int(text)

    if count_g == 0:
        pass
    else:
        text = re.sub("G","",text)
        text = float(text)
        text = text*1000

    return text

#14~18,25,28~29*1000

while True:
    line = f.readline()
    if not line: break
    if (stack > 2):
        list_out = []
        a = []
        line = split(str(line))
        for i in range(1,31):
            b = line.split(',')[i]
            a.append(b)
        # 뒤에 붙은 k, M, B를 제거함
        a[14] = clean_text(a[14])
        a[17] = clean_text(a[17])
        a[18] = clean_text(a[18])
        a[25] = clean_text(a[25])

        a[6] = K_text(a[6])
        a[7] = K_text(a[7])
        a[13] = M_G(a[13])
        a[15] = M_G(a[15])
        a[16] = M_G(a[16])
        a[28] = K_text(a[28])
        a[29] = K_text(a[29])
        list_out.append({'usr':a[0],'sys':a[1], 'idl':a[2], 'wai':a[3], 'hiq':a[4], 'siq':a[5], 'disk_read':a[6], 'disk_writ':a[7], 'paging_in':a[8], 'out':a[9], 'one_m':a[10], 'five_m':a[11], 'fifteen_m':a[12], 'memory_used':a[13], 'buff':a[14], 'cach':a[15], 'memory_free':a[16], 'recv':a[17], 'send':a[18], 'run':a[19], 'blk':a[20], 'new':a[21], 'io_read':a[22], 'io_writ':a[23], 'swap_used':a[24], 'swap_free':a[25],'int':a[28], 'csw':a[29]})
        csvout.writerows(list_out)
    else:
        stack = stack + 1

f.close()
