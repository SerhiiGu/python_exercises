"""10. Використайте модуль sqlite3, щоб створити базу даних SQLite під назвою imdb.db і таблицю ratings, \
що містить наступні поля: id (INTEGER PRIMARY KEY), title (VARCHAR(20)), year (INT), rating (FLOAT). \
Зчитайте дані з файла imdb.csv і додайте їх у таблицю ratings. Зчитайте і виведіть на екран усі значення \
таблиці ratings у алфавітному порядку за полем title. Зчитайте і виведіть на екран усі записи таблиці ratings \
з ретингом більшим за 8.70"""

import csv
import sqlite3
import pprint
"""
with open('c:\\Merck\\Python\\Chapter8\\csv\\imdb.csv', 'r') as imdbfile:
    record=csv.reader(imdbfile)
    next(record, None)
    dict = [ i for i in record ]

conn = sqlite3.connect('c:\\Merck\\Python\\Chapter8\\imdb.db')
curs = conn.cursor()
curs.execute('''CREATE TABLE ratings (id INT PRIMARY KEY, title VARCHAR(20), year INT, rating FOLAT)''')
conn.commit()
ins = 'INSERT into ratings (title, year, rating) VALUES(?, ?, ?)'
for line in dict:
    print(line[0],line[1],line[2])
    curs.execute(ins, (line[0],line[1],line[2]))
conn.commit()
"""
conn = sqlite3.connect('c:\\Merck\\Python\\Chapter8\\imdb.db')
curs = conn.cursor()
curs.execute('''SELECT title, year, rating FROM ratings ORDER by title ASC''')
rows = curs.fetchall()
pprint.pprint(rows)

curs.execute('''SELECT title, year, rating FROM ratings WHERE rating >"8.68" ''')
rows = curs.fetchall()
pprint.pprint(rows)

curs.close()
conn.close()
