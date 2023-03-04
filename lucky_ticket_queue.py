from datetime import datetime
from threading import Thread
from queue import Queue as qq  # Queue for threads
from multiprocessing import Process, Queue  # Queue for prosesses


def lucky_ticket(start, end, queue):
    count = 0
    for number in range(start, end):
        digit6 = "{:06d}".format(number)
        lst = [int(x) for x in digit6]
        if lst[0] + lst[1] + lst[2] == lst[3] + lst[4] + lst[5]:
            # print(f'{number} is a lucky ticket')
            count += 1
    print(f'Number of lucky tickets in range {start}-{end}: {count}')
    queue.put(count)
    return count


if __name__ == '__main__':
    qq = Queue()
    timestart = datetime.now()
    count = lucky_ticket(1, 999999, qq)
    timeend = datetime.now()
    print(f'Number of lucky tickets: {count}. \t Time in single thread: {timeend - timestart}')
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    qq = Queue()
    timestart = datetime.now()
    t1 = Thread(target=lucky_ticket, args=(1, 500000, qq))
    t2 = Thread(target=lucky_ticket, args=(500001, 999999, qq))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    result_list = []
    while not qq.empty():
        result_list.append(qq.get())
    print(result_list)
    timeend = datetime.now()
    data = sum(x for x in result_list)
    print(f'Number of lucky tickets: {data}. \t Time in two threads: {timeend - timestart}')
    # ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    queue = Queue()
    timestart = datetime.now()
    p1 = Process(target=lucky_ticket, args=(1, 500000, queue))
    p2 = Process(target=lucky_ticket, args=(500001, 999999, queue))
    p1.start()
    p2.start()
    p1.join()
    p2.join()

    result_list = []
    while not queue.empty():
        result_list.append(queue.get())
    print(result_list)
    timeend = datetime.now()
    data = sum(x for x in result_list)
    print(f'Number of lucky tickets: {data}. \t Time in two processes: {timeend - timestart}')
