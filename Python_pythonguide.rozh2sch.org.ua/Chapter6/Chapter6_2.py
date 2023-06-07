"""2. Визначте назву геометричної фігури за введеною кількістю її сторін. \
Програма повинна підтримувати фігури від 3 до 6 сторін. Якщо введена кількість сторін поза межами \
цього діапазону, програма повинна відображати відповідне повідомлення. """

while True:
    i = input('Введіть к-ть сторін(q для виходу):')
    if i == 'q': 
        exit()
    elif not i.isnumeric():
        print('Not number!')
    elif i == '3':
        print('Triangle')
    elif i == '4':
        print('Square')
    elif i == '5':
        print('5-angle')
    elif i == '6':
        print('6-angle')
    else:
        print('Not in range! Must be in range 3-6')