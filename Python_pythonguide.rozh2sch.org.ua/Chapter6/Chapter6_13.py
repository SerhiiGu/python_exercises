
"""13. Створіть таблицю множення. Розмірність таблиці (кількість рядків і стовпців) вводиться з клавіатури."""

x = input('Введіть кількість рядків(число): ')
if not x.isnumeric():
    print('Це не число!')
    exit()
y = input('Введіть кількість стовпців(число): ')
if not y.isnumeric():
    print('Це не число!')
    exit()

for i in range(1, int(x)+1):
     for j in range(i, i*int(y)+1, i):
         print(j, end='\t')
     print()