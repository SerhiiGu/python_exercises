"""2.Створіть об’єкт happy, що містить дату вашого народження. Використайте функції для роботи з датою і часом, \
щоб дізнатися відповіді на такі питання (виведення організуйте в окремий файл у вигляді, на зразок \
«запитання: відповідь», у окремих рядках):
a. "Яка дата вашого народження?"
b. "У який день тижня ви народилися?"
c. "Коли вам буде (або вже було) 13 330 днів від народження?"
"""

import datetime, time

happy = datetime.date(1985, 12, 11)

print('Дата народження: ', happy)
#
daysOftheWeek = ("ISO Week days start from 1", "Monday", "Tuesday", "Wednesday", "Thursday", \
    "Friday", "Saturday", "Sunday")
isoWeekDay = happy.isoweekday()
print('У який день тижня ви народилися? ', daysOftheWeek[isoWeekDay])
#
one_day = datetime.timedelta(days=1)
h13330 = happy + one_day * 13300
print('13330 днів від народження було: ', h13330)