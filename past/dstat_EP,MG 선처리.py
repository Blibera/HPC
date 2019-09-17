import re
import csv

f = open("C:/Users/Slayer/Desktop/공유할것/dstat_EP_D_64.txt", 'r')

ff = open('C:/Users/Slayer/Desktop/공유할것/dstat_EP_D_64_변수제거 안함t.csv', 'wt',newline='', encoding='utf-8')

wr = csv.writer(ff)
frist = csv.DictWriter(ff,['<-------------','_---------------total cpu usage----------------------->','','','','','<-----dsk/total----->','','<---paging stat--->','','<---------load stat--------->','','','<-------------memory stat---------------->','','','','<total network stat>','','<---------process stat-------->','','','<------i/o stat------>','','<---swap stat--->','','<-----system----->','','<-----system1----->'])
frist.writeheader()


csvout = csv.DictWriter(ff,['usr','sys', 'idl', 'wai', 'hiq', 'siq', 'disk_read', 'disk_writ', 'paging_in', 'out', 'one_m', 'five_m', 'fifteen_m', 'memory_used', 'buff', 'cach', 'memory_free', 'recv', 'send', 'run', 'blk', 'new', 'io_read', 'io_writ', 'swap_used', 'swap_free', 'day','time', 'int', 'csw'])
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

stack = 1

while True:
    line = f.readline()
    if not line: break
    j=0
    if (stack > 2):
        list_out = []
        a = []
        line = split(str(line))
        for i in range(1,31):
            b = line.split(',')[i]
            a.append(b)

        if j>29:
            a[j] = int(a[j])

        list_out.append(
            {'usr': a[0], 'sys': a[1], 'idl': a[2], 'wai': a[3], 'hiq': a[4], 'siq': a[5], 'disk_read': a[6],
             'disk_writ': a[7], 'paging_in': a[8], 'out': a[9], 'one_m': a[10], 'five_m': a[11], 'fifteen_m': a[12], 'memory_used': a[13],
             'buff': a[14], 'cach': a[15], 'memory_free': a[16], 'recv': a[17], 'send': a[18], 'run': a[19],
             'blk': a[20], 'new': a[21], 'io_read': a[22], 'io_writ': a[23], 'swap_used': a[24], 'swap_free': a[25],
             'day': a[26], 'time': a[27], 'int': a[28], 'csw': a[29]})
        csvout.writerows(list_out)
    else:
        stack = stack + 1

f.close()
