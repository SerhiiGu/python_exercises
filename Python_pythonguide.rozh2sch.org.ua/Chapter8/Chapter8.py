#import locale
#print(locale.getpreferredencoding())

#data = open('c:\Merck\Python\Chapter8\Chapter8.py', 'rt', encoding='cp1251').read()
#print(data)

#bdata = bytes(range(0, 256))
#frecord = open('c:\Merck\Python\Chapter8\Bfile', 'wb')
#frecord.write(bdata)
#frecord.close()

"""
import csv
programmers = [
    {'language': 'Python', 'developer': 'Guido van Rossum'},
    {'language': 'Scala', 'developer': 'Martin Odersky'},
    {'language': 'PHP', 'developer': 'Rasmus Lerdorf'},
    {'language': 'Ruby', 'developer': 'Yukihiro Matsumoto'},
    {'language': 'C', 'developer': 'Dennis Ritchie'},
]
with open('c:\Merck\Python\Chapter8\programmers.csv', 'wt', newline='') as frecord:
    crecord = csv.DictWriter(frecord, ['language', 'developer'])
    crecord.writeheader()
    crecord.writerows(programmers)
"""

"""
import csv
import pprint
with open('c:\Merck\Python\Chapter8\programmers.csv', 'rt') as freading:
    creading = csv.DictReader(freading)
    programmers = [{'language': row['language'], 'developer': row['developer']} for row in creading]
pprint.pprint(programmers)
"""

"""
import sqlite3 
conn = sqlite3.connect('c:\Merck\Python\Chapter8\ishop.db') 
curs = conn.cursor() 
#curs.execute('''CREATE TABLE computers (id INT PRIMARY KEY, name VARCHAR(20), count INT, price FLOAT)''') 
#curs.execute('INSERT INTO computers VALUES(1, "PC", 5, 7570.50)')
#curs.execute('INSERT INTO computers VALUES(2, "Notebook", 8, 11430.30)')
#ins = 'INSERT INTO computers (id, name, count, price) VALUES(?, ?, ?, ?)'
#curs.execute(ins, (3, 'TabletPC', 4, 3970.20))
#curs.execute(ins, (4, 'Console', 2, 16780.90))
curs.execute('SELECT * FROM computers ORDER BY count')
conn.commit() 
rows = curs.fetchall()
for row in rows:
    print(row)
curs.close() 
conn.close() 
"""

#with open('c:\Merck\Python\Chapter8\\tests.txt', 'wt') as fl:
#    test1 = 'Test variable to write to file'
#    fl.write(test1)

#import csv
#with open('c:\\Merck\\Python\\Chapter8\\csv\\painters.csv', 'rt') as fl:
#    painters = csv.DictReader(fl)
#    for row in painters:
#        print(row)

"""
import csv
imdb = [
    {
        'title': 'Lord of the Rings: Two towers',
        'year': 2002,
        'rating': 8.7},
    {
        'title': 'Matrix',
        'year': 1999,
        'rating': 8.7},
    {
        'title': 'Interstellar',
        'year': 2014,
        'rating': 8.5},
    {
        'title': 'Back to the Future',
        'year': 1985,
        'rating': 8.5},
    {
        'title': 'Logan: Wolverine',
        'year': 2017,
        'rating': 8.1}
]

with open('c:\\Merck\\Python\\Chapter8\\csv\\imdb.csv', 'wt', newline='') as imdbfile:
    record=csv.DictWriter(imdbfile, ['title','year','rating'])
    record.writeheader()
    record.writerows(imdb)
"""

