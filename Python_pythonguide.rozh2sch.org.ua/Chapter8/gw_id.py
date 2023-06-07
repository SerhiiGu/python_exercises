import csv
from itertools import chain

with open('c:\Merck\Python\Chapter8\csv\gw_id_have.csv', 'rt') as file1:
    list_have = csv.reader(file1)
    have = [lst for lst in list_have]
    have = list(map(str.upper, chain.from_iterable(have)))
    #print(have)

with open('c:\Merck\Python\Chapter8\csv\gw_id_lst.csv', 'rt') as file2:
    list_lst = csv.reader(file2)
    lst = [lst for lst in list_lst]
    lst = list(map(str, chain.from_iterable(lst)))
    #print(lst)

for i in have:
    for j in lst:
        #print(i, j)
        if j in i:
            print(f'Equal: {i} {j}')