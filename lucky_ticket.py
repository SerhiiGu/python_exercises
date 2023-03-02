

def lucky_ticket(start, end):
    count = 0
    for number in range(start, end):
        lst = [int(x) for x in str(number)]
        while len(lst) < 6:
            lst.append(0)
        if lst[0]+lst[1]+lst[2] == lst[3]+lst[4]+lst[5]:
            # print(f'{number} is a lucky ticket')
            count += 1
    print(f'Number of lucky tickets: {count}')


if __name__ == '__main__':
    lucky_ticket(1, 999999)
