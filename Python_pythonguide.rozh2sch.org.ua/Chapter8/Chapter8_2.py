"""2. Реалізуйте програму, яка зчитує ціле число, що вводиться з командного рядка, \
і записує у текстовий файл інформацію, щодо парності або непарності числа."""

num = input("Введіть число: ")
with open('c:\Merck\Python\Chapter8\\chapter8_2.txt', 'at') as file1:
    if int(num) % 2:
        file1.write(f'{num}: непарне\n')
    else:
        file1.write(f'{num}: парне\n')