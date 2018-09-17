import csv

ff = open('C:/Users/Slayer/Desktop/공유할것/선처리_mg.csv', 'wt',newline='', encoding='utf-8')
wr = csv.writer(ff)

csvout = csv.DictWriter(ff,['usr', 'sys', 'idl_up', 'idl_down', 'idl_same', 'disk_read','disk_writ',\
                            'one_m_up', 'one_m_down', 'one_m_same', 'five_m_up', 'five_m_down', 'five_m_same', 'fifteen_m_up', 'fifteen_m_down', 'fifteen_m_same', \
                            'memory_used_up', 'memory_used_down', 'memory_used_same' , 'cash_up', 'cash_down', 'cash_same' , 'memory_free', \
                            'recv_up', 'recv_down', 'recv_same', 'send', 'run_up', 'run_down', 'run_same' , \
                            'new_up', 'new_down', 'new_same', 'io_read', 'io_wirt', 'int_up', 'int_down', 'int_same' , \
                            'csw_up', 'csw_down', 'csw_same',])
csvout.writeheader()
f_r = open('C:/Users/Slayer/Desktop/공유할것/dstat_EP_D_64_변수제거 선처리.csv', 'r', encoding='utf-8')
rdr = csv.reader(f_r)


stack = 0
for line in rdr:
    print(line)

ff.close()
f_r.close()