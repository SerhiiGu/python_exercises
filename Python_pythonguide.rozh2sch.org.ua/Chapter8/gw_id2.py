import csv
from itertools import chain

with open('c:\Merck\Python\Chapter8\csv\gw_id_have2.csv', 'rt') as file1:
    list_have = csv.reader(file1)
    have = [lst for lst in list_have]
    #print(have)

with open('c:\Merck\Python\Chapter8\csv\gw_id_lst.csv', 'rt') as file2:
    list_lst = csv.reader(file2)
    lst = [lst for lst in list_lst]
    lst = list(map(str, chain.from_iterable(lst)))
    #print(lst)

for i in have:
    k = str.upper(i[1])
    for j in lst:
        if k == j :
            #print(f'Equal: {i} {j}')
            print(i, j)