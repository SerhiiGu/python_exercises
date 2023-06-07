"""1. Використайте регулярні вирази для пошуку рядків у тексті. \
Текст, у якому відбуватиметься пошук, можна скопіювати із сайту \
Project Gutenberg’s  і зберегти у файл. Імпортуйте модуль re, щоб \
використовувати функції регулярних виразів у Python. Вивести на екран \
усі слова, які починаються з літери «с», чотирилітерні слова, які \
починаються з літери c, слова, які закінчуються на букву r, слова, \
які містять чотири літери time поспіль."""

import re

with open('c:\\Merck\\Python\\Chapter11\\gutt.txt','r') as f1:
    text = f1.read()

result = re.findall(r'\b[sS]\w+\b', text)
print(len(result))

result = re.findall(r'\b[sS]\w{3}\b', text)
print(len(result))

result = re.findall(r'\b\w+[rR]\b', text)
print(len(result))

result = re.findall(r'\btime\w{0,99}\b', text)
print(result)