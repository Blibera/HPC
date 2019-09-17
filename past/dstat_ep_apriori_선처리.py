import csv

ff = open('C:/Users/Slayer/Desktop/공유할것/dstat선처리_ep.csv', 'wt',newline='', encoding='utf-8')
wr = csv.writer(ff)

csvout = csv.DictWriter(ff,['usr', 'sys', 'idl_up', 'idl_down', 'idl_same', 'disk_read','disk_writ',\
                            'one_m_up', 'one_m_down', 'one_m_same', 'five_m_up', 'five_m_down', 'five_m_same', 'fifteen_m_up', 'fifteen_m_down', 'fifteen_m_same', \
                            'memory_used_up', 'memory_used_down', 'memory_used_same' , 'cash_up', 'cash_down', 'cash_same' , 'memory_free', \
                            'recv_up', 'recv_down', 'send', 'run_up', 'run_down', 'run_same' , \
                            'new_up', 'new_down', 'io_read', 'io_wirt', 'int_up', 'int_down', 'int_same' , \
                            'csw_up', 'csw_down'])
csvout.writeheader()
f_r = open('C:/Users/Slayer/Desktop/공유할것/dstat_EP_D_64_변수제거 선처리.csv', 'r', encoding='utf-8')
rdr = csv.reader(f_r)

idl_before = 0
idl_now = 0
one_m_before = 0
one_m_now = 0
five_m_before = 0
five_m_now = 0
fifteen_m_before = 0
fifteen_m_now = 0
memory_used_before = 0
memory_used_now = 0
cash_before = 0
cash_now = 0
recv_before = 0
recv_now = 0
run_before = 0
run_now = 0
new_before = 0
new_now = 0
int_before = 0
int_now = 0
csw_before = 0
csw_now = 0
stack = 0
for line in rdr:
    recv_up = 0
    recv_down = 0
    new_up = 0
    new_down = 0
    csw_up = 0
    csw_down = 0

    idl_up = 0
    idl_down = 0
    idl_same = 0
    one_m_up = 0
    one_m_down = 0
    one_m_same = 0
    five_m_up = 0
    five_m_down = 0
    five_m_same = 0
    fifteen_m_up = 0
    fifteen_m_down = 0
    fifteen_m_same = 0
    memory_used_up = 0
    memory_used_down = 0
    memory_used_same = 0
    cash_up = 0
    cash_down = 0
    cash_same = 0
    run_up = 0
    run_down = 0
    run_same = 0
    int_up = 0
    int_down = 0
    int_same = 0

    recv_before = recv_now
    new_before = new_now
    csw_before = csw_now

    idl_before = idl_now
    one_m_before = one_m_now
    five_m_before = five_m_now
    fifteen_m_before = fifteen_m_now

    memory_used_before = memory_used_now
    cash_before = cash_now
    run_before = run_now
    int_before = int_now

    list_out = []

    if stack<2:
        stack = stack + 1
        recv_before = line[11]
        recv_now= line[11]
        new_before= line[14]
        new_now= line[14]
        csw_before= line[18]
        csw_now= line[18]

        idl_before = line[2]
        idl_now = line[2]
        one_m_before = line[5]
        one_m_now = line[5]
        five_m_before = line[6]
        five_m_now = line[6]
        fifteen_m_before = line[7]
        fifteen_m_now = line[7]

        memory_used_before = line[8]
        memory_used_now = line[8]
        cash_before = line[9]
        cash_now = line[9]
        run_before = line[13]
        run_now = line[13]
        int_before = line[17]
        int_now = line[17]


    else:
        recv_now = line[11]
        new_now = line[14]
        csw_now = line[18]
        idl_now = line[2]
        one_m_now = line[5]
        five_m_now = line[6]
        fifteen_m_now = line[7]
        memory_used_now = line[8]
        cash_now = line[9]
        run_now = line[13]
        int_now = line[17]

        # 현재값이 전보다 클 경우
        if recv_now > recv_before:
            recv_up = 1
        else:
            recv_down = 1
        # 현재값이 전보다 클 경우
        if new_now > new_before:
            new_up = 1
        else:
            new_down = 1

        if csw_now > csw_before:
            csw_up = 1
        else:
            csw_down = 1



        if idl_now > idl_before :
            idl_up = 1
        elif idl_now < idl_before :
            idl_down = 1
        else:
            idl_same = 1

        if one_m_now > one_m_before :
            one_m_up = 1
        elif one_m_now < one_m_before :
            one_mdown = 1
        else:
            one_m_same = 1

        if five_m_now > five_m_before :
            five_m_up = 1
        elif five_m_now < five_m_before :
            five_m_down = 1
        else:
            five_m_same = 1

        if fifteen_m_now > fifteen_m_before :
            fifteen_m_up = 1
        elif fifteen_m_now < fifteen_m_before :
            fifteen_m_down = 1
        else:
            fifteen_m_same = 1

        if memory_used_now > memory_used_before :
            memory_used_up = 1
        elif memory_used_now < memory_used_before :
            memory_used_down = 1
        else:
            memory_used_same = 1

        if cash_now > cash_before :
            cash_up = 1
        elif cash_now < cash_before :
            cash_down = 1
        else:
            cash_same = 1

        if run_now > run_before :
            run_up = 1
        elif run_now < run_before :
            run_down = 1
        else:
            run_same = 1

        if int_now > int_before :
            int_up = 1
        elif int_now < int_before :
            int_down = 1
        else:
            int_same = 1

        line[0] = int(line[0])
        line[1] = int(line[1])
        line[3] = int(line[3])
        line[4] = int(line[4])
        line[10] = int(line[10])
        line[12] = int(line[12])
        line[15] = int(line[15])
        line[16] = int(line[16])

        if line[0]>0:
            line[0] = 1
        else:
            line[0] = 0

        if line[1]>0:
            line[1] = 1
        else:
            line[1] = 0

        if line[3]>0:
            line[3] = 1
        else:
            line[3] = 0

        if line[4]>0:
            line[4] = 1
        else:
            line[4] = 0

        if line[10]>0:
            line[10] = 1
        else:
            line[10] = 0

        if line[12]>0:
            line[12] = 1
        else:
            line[12] = 0

        if line[15]>0:
            line[15] = 1
        else:
            line[15] = 0

        if line[16]>0:
            line[16] = 1
        else:
            line[16] = 0

        list_out.append({'usr': int(line[0]), 'sys': int(line[1]), 'disk_read': int(line[3]), 'disk_writ': int(line[4]), \
                         'memory_free': int(line[10]), 'send': int(line[12]), 'io_read': int(line[15]), 'io_wirt': int(line[16]),
                         'recv_up': int(recv_up), 'recv_down': int(recv_down), 'new_up': int(new_up), 'new_down': int(new_down), 'csw_up': int(csw_up), 'csw_down': int(csw_down),
                        'idl_up': int(idl_up),'idl_down': int(idl_down),'idl_same': int(idl_same), 'one_m_up': int(one_m_up),'one_m_down': int(one_m_down),'one_m_same': int(one_m_same), \
                         'five_m_up': int(five_m_up), 'five_m_down': int(five_m_down), 'five_m_same': int(five_m_same), 'fifteen_m_up': int(fifteen_m_up), 'fifteen_m_down': int(fifteen_m_down), 'fifteen_m_same': int(fifteen_m_same), \
                         'memory_used_up': int(memory_used_up), 'memory_used_down': int(memory_used_down), 'memory_used_same': int(memory_used_same), 'cash_up': int(cash_up), 'cash_down': int(cash_down), 'cash_same': int(cash_same), \
                         'run_up': int(run_up), 'run_down': int(run_down), 'run_same': int(run_same), 'int_up': int(int_up), 'int_down': int(int_down), 'int_same': int(int_same), \

                         })
        csvout.writerows(list_out)

ff.close()
f_r.close()