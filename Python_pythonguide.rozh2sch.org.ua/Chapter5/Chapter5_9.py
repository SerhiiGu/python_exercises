
"""9. Із словника teams необхідно вивести на екран статистику кількох команд Національної баскетбольної асоціації NBA. \
Створіть словник teams, дотримуючись наступних правил. Назви команд  - це ключі словника. \
Значення у словнику - це список, на зразок: [Всього ігор, Перемог, Нічиїх, Поразок, Всього очок]. \
Значення списку - це цілі числа, які обираються довільно. При виведенні даних, прослідкуйте, щоб формат виведення \
був таким: NEW YORK KNICKS 22 7 6 9 45. Інформація про кожну команду має міститися в окремому рядку. \
Зверніть увагу на те, що дані у словнику є невпорядкованими"""

teams = {'Lakers' : [ 22, 7, 6, 9, 25], 'Bulls' : [25, 9, 7, 9, 28], 'Rangers' : [21, 4, 6, 11, 18]}
for key in teams:
    print(key,  ' '.join(str(e) for e in teams[key]))