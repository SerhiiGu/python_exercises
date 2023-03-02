

def lucky_ticket():
    count = 0
    for number in range(1001, 1011):
        lst = [int(x) for x in str(number)]
        while len(lst) < 6:
            lst.append(0)

        print(lst, type(lst), type(lst[3]))
    return ''


if __name__ == '__main__':

    lucky_ticket()