import csv

f_bdev = open("C:/Users/Slayer/Desktop/공유할것/NPB_log_knl02_64/NPB_EP_log/sar_bdev/(평균)sar_bdev_2018-08-02.csv", 'r')
f_file = open("C:/Users/Slayer/Desktop/공유할것/NPB_log_knl02_64/NPB_EP_log/sar_file/(평균)sar_file_2018-08-02.csv", 'r')
f_io = open("C:/Users/Slayer/Desktop/공유할것/NPB_log_knl02_64/NPB_EP_log/sar_io/(평균)sar_io_2018-08-02.csv", 'r')
f_mem = open("C:/Users/Slayer/Desktop/공유할것/NPB_log_knl02_64/NPB_EP_log/sar_mem/(평균)sar_mem_2018-08-02.csv", 'r')
f_memutil = open("C:/Users/Slayer/Desktop/공유할것/NPB_log_knl02_64/NPB_EP_log/sar_memutil/(평균)sar_memutil_2018-08-02.csv", 'r')
f_pg = open("C:/Users/Slayer/Desktop/공유할것/NPB_log_knl02_64/NPB_EP_log/sar_pg/(평균)sar_pg_2018-08-02.csv", 'r')
f_pow = open("C:/Users/Slayer/Desktop/공유할것/NPB_log_knl02_64/NPB_EP_log/sar_pow/(평균)sar_pow_2018-08-02.csv", 'r')
f_que = open("C:/Users/Slayer/Desktop/공유할것/NPB_log_knl02_64/NPB_EP_log/sar_que/(평균)sar_que_2018-08-02.csv", 'r')
f_swap = open("C:/Users/Slayer/Desktop/공유할것/NPB_log_knl02_64/NPB_EP_log/sar_swap/(평균)sar_swap_2018-08-02.csv", 'r')
f_swch = open("C:/Users/Slayer/Desktop/공유할것/NPB_log_knl02_64/NPB_EP_log/sar_swch/(평균)sar_swch_2018-08-02.csv", 'r')

f_sar = open("C:/Users/Slayer/Desktop/공유할것/NPB_log_knl02_64/NPB_EP_log/sar.csv", 'w',
             newline='')
write = csv.writer(f_sar)

stack = 0
add = []

while True:
    add = []
    line_bdev = f_bdev.readline()
    line_file = f_file.readline()
    line_io = f_io.readline()
    line_mem = f_mem.readline()
    line_memutil = f_memutil.readline()
    line_pg = f_pg.readline()
    line_pow = f_pow.readline()
    line_que = f_que.readline()
    line_swap = f_swap.readline()
    line_swch = f_swch.readline()

    if not line_bdev: break

    count = line_pow.count(',')

    if stack == 0 :
        for i in range(0,41):
            tol = line_bdev.split(',')[i]
            tol = tol.strip()
            add.append(tol)

        for i in range(1,5):
            tol = line_file.split(',')[i]
            tol = tol.strip()
            add.append(tol)

        for i in range(1,6):
            tol = line_io.split(',')[i]
            tol = tol.strip()
            add.append(tol)

        for i in range(1,4):
            tol = line_mem.split(',')[i]
            tol = tol.strip()
            add.append(tol)

        for i in range(1, 11):
            tol = line_memutil.split(',')[i]
            tol = tol.strip()
            add.append(tol)

        for i in range(1,10):
            tol = line_pg.split(',')[i]
            tol = tol.strip()
            add.append(tol)

        for i in range(0, 58):
            tol = line_pow.split(',')[i]
            tol = tol.strip()
            add.append(tol)

        for i in range(1,7):
            tol = line_que.split(',')[i]
            tol = tol.strip()
            add.append(tol)

        for i in range(1, 6):
            tol = line_swap.split(',')[i]
            tol = tol.strip()
            add.append(tol)

        for i in range(1,3):
            tol = line_swch.split(',')[i]
            tol = tol.strip()
            add.append(tol)

        write.writerow(add)
        stack = stack + 1
    else:
        for i in range(0,41):
            tol = line_bdev.split(',')[i]
            tol = tol.strip()
            add.append(tol)

        for i in range(1,5):
            tol = line_file.split(',')[i]
            tol = tol.strip()
            add.append(tol)

        for i in range(1,6):
            tol = line_io.split(',')[i]
            tol = tol.strip()
            add.append(tol)

        for i in range(1,4):
            tol = line_mem.split(',')[i]
            tol = tol.strip()
            add.append(tol)

        for i in range(1, 11):
            tol = line_memutil.split(',')[i]
            tol = tol.strip()
            add.append(tol)

        for i in range(1,10):
            tol = line_pg.split(',')[i]
            tol = tol.strip()
            add.append(tol)

        for i in range(0, 58):
            tol = line_pow.split(',')[i]
            tol = tol.strip()
            add.append(tol)

        for i in range(1,7):
            tol = line_que.split(',')[i]
            tol = tol.strip()
            add.append(tol)

        for i in range(1, 6):
            tol = line_swap.split(',')[i]
            tol = tol.strip()
            add.append(tol)

        for i in range(1,3):
            tol = line_swch.split(',')[i]
            tol = tol.strip()
            add.append(tol)

        write.writerow(add)

f_sar.close()