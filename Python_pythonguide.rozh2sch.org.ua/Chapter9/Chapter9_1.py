"""1. Запишіть програмно поточні дату й час як рядок у текстовий файл today.txt. \
Зчитайте текстовий файл today.txt і розмістіть дані у рядку today_string. \
Розберіть дату з рядка today_string на складові, використовуючи функції для роботи з датом й часом, \
і виведіть їх на екран у вигляді повідомлень з пояснюючим текстом"""


import os
import time, datetime

dt = datetime.datetime.now()
with open('C:\\Merck\\Python\\Chapter9\\today.txt','w') as f1:
    f1.write(str(dt))

with open('C:\\Merck\\Python\\Chapter9\\today.txt','r') as f1:
    today_string = f1.read()

format = '%Y-%m-%d %H:%M:%S.%f'
today_time = datetime.datetime.strptime(today_string, format)

print(type(today_time))
print(today_time)
print(today_time.month) # місяць
print(today_time.day) # день
print(today_time.hour) # години
print(today_time.minute) # хвилини
print(today_time.second) # секунди
print(today_time.microsecond) # частки секунди


os.remove('C:\\Merck\\Python\\Chapter9\\today.txt')