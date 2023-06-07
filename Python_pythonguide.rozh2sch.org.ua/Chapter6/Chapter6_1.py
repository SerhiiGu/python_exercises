"""1. Виведіть вітальне повідомлення для кожного користувача після його входу на сайт. \
Cтворіть список з кількох імен користувачів, включаючи ім’я 'Admin'. Перебираючи елементи списку, \
виведіть повідомлення для кожного користувача. Для користувача з ім’ям 'Admin' виведіть особливе повідомлення - \
наприклад: Hello Admin, I hope you’re well.. У інших випадках виводиться універсальне привітання - наприклад: \
Hello Alex, thank you for logging in again.. Додайте команду if, яка перевірить, що список користувачів не порожній. \
Якщо список порожній, виведіть повідомлення: We need to find some users!. \
Видаліть зі списку всі імена користувачів і переконайтеся у тому, що програма виводить правильне повідомлення"""

lst = ['Adam','Max','Kyle','Kate','Admin','Bob']
lst2 = []
if not lst2:
    print('List is empty! We need to find some users!')

for name in lst:
    if (name == 'Admin'):
        print(f'Hello {name}, thank you for logging in again.')
    else:
        print(f'Hello {name}, I hope you’re well...')

