"""9. Виконайте розкладання чотирицифрового цілого числа і виведіть на екран суму цифр у числі. 
Наприклад, якщо обрали число 6259, то програма повинна вивести на екран повідомлення: 
6 + 2 + 5 + 9 = 22. Використайте функцію format() для відображення результату або f-рядки."""

a = str(6201)
summ = str(sum(map(int, a)))
print(' + '.join(a) + ' = ' + str(summ))