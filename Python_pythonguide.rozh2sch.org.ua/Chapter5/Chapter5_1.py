"""1 Словники Python можуть використовуватися для моделювання «справжнього» словника (назвемо його глосарієм). \
Оберіть кілька термінів з програмування (або із іншої області), які ви знаєте на цей момент. \
Використайте ці слова як ключі глосарію, а їх визначення - як значення. \
Виведіть кожне слово і його визначення у спеціально відформатованому вигляді. \
Наприклад, ви можете вивести слово, потім двокрапка і визначення; або ж слово в одному рядку, \
а його визначення - з відступом в наступному рядку. Використовуйте символ нового рядка (\n) \
для вставки порожніх рядків між парами «слово: визначення» і символ табуляції \
для встановлення відступів (\t) у вихідних даних."""


glossary = {'CPU' : 'CPU means ‘Central Processing Unit’. This is the place of computer data handling.',\
'RAM' : 'RAM stands for “Random Access Memory” or “Ready Access Memory”. \
It is a temporary notepad where your computer sends information to disk, \
or to the storage place of instructions from other input devices', \
'HDD' : 'Your computers hard disk drive is like an audio CD that you possess at home \
– except your computer can read and write to it.', \
'Software' : '‘Software’ is the term which refers to the instructions needed to make a computer work'}


for key in glossary:
    print(key, ':\t', glossary[key], '\n' )