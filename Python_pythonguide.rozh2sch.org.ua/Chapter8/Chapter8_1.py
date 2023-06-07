"""1. Створіть новий файл numbers.txt у текстовому редакторі і запишіть у нього 10 чисел, кожне з нового рядка. \
Напишіть програму, яка зчитує ці числа з файла і обчислює їх суму, виводить цю суму на екран і, водночас, \
записує цю суму у інший файл з назвою sum_numbers.txt."""

import random

lst = []
for i in range(10):
       lst.append(random.randint(9, 99))
print(lst)

with open('c:\Merck\Python\Chapter8\\numbers.txt', 'wt') as file1:
    file1.write('\n'.join(str(item) for item in lst))

lst = []
with open('c:\Merck\Python\Chapter8\\numbers.txt', 'r') as file1:
    lines = file1.readlines()
    for line in lines:
        lst.append(int(line))
    print(lst)
    print(sum(lst))