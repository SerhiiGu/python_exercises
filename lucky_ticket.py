# написати программу яка рахує кількість щасливих білетів
#
# білет містить 6 цифр
# білет є щасливим коли сума перших трьох цифр дорівнює сумі другої трійки цифр
# наприклад
# 101020 - щасливий бо
# 1+0+1 == 0 + 2 + 0
#
# 546021 - звичайний, бо
# 5+4+6 != 0 + 2 + 1
#
# передбачити що можуть бути і номера накшталт
# 000012
# 001099
#
# Бажано щоб функція могла підтримувати розпаралелювання (приймати на вхід початок і кінець діапазону для обрахунку)
#################################################

from datetime import datetime
from threading import Thread


def lucky_ticket(start, end):
    count = 0
    for number in range(start, end):
        digit6 = "{:06d}".format(number)
        lst = [int(x) for x in digit6]
        if lst[0]+lst[1]+lst[2] == lst[3]+lst[4]+lst[5]:
            # print(f'{number} is a lucky ticket')
            count += 1
    print(f'Number of lucky tickets in range {start}-{end}: {count}')
    global data
    data = data + count
    return count


if __name__ == '__main__':
    data = 0
    timestart = datetime.now()
    count = lucky_ticket(1, 999999)
    timeend = datetime.now()
    print(f'Number of lucky tickets: {count}. \t Time in single thread: {timeend - timestart}')

    # data = 0
    # timestart = datetime.now()
    # t1 = Thread(target=lucky_ticket, args=(1, 500000))
    # t2 = Thread(target=lucky_ticket, args=(500001, 999999))
    # t1.start()
    # t2.start()
    # t1.join()
    # t2.join()
    # timeend = datetime.now()
    # print(f'Number of lucky tickets: {data}. \t Time in two threads: {timeend - timestart}')

