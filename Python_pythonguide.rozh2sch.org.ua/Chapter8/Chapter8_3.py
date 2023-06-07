"""3. Створіть новий файл у текстовому редакторі і напишіть кілька рядків тексту у ньому про можливості Python. \
    Кожен рядок повинен починатися з фрази: In Python you can .... Збережіть файл з ім’ям learning_python.txt. \
    Напишіть програму, яка зчитує файл і виводить текст з перебором рядків об’єкта файла \
    і зі збереженням рядків у списку з подальшим виведенням списку поза блоком with."""

lines = []
with open('c:\Merck\Python\Chapter8\\learning_python.txt', 'r') as file1:
    lines = [line.rstrip() for line in file1.readlines()]

print(lines)
for line in lines:
    print(f'{str(line)}')