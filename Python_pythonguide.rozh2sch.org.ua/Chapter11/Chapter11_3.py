"""3. Запишіть у текстовий файл з ім’ям validate.txt інформацію про \
ширину і висоту зображення, отримані із GIF-файла. \
Скористайтеся відомостями із попереднього завдання."""

import binascii

with open("c:\\Merck\\Python\\Chapter11\\an1.gif", 'rb') as f1:
    if f1.read(6) == b"GIF89a":
        f1.seek(7)
        width = binascii.hexlify(f1.read(2))
        #f1.seek(9)
        height = binascii.hexlify(f1.read(2))
    else:
        print('Incorrect GIF header')

print(int(width, 16), int(height, 16))