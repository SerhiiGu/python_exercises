""" 5.1-5.8
languages_programmers = {'Scala': 'Martin Odersky', 'JavaSript': 'Brendan Eich', \
'Python': 'Guido van Rossum', 'PHP': 'Rasmus Lerdorf', \
'Ruby': 'Yukihiro Matsumoto', 'C': 'Dennis Ritchie'}
print("Початковий словник:", languages_programmers)
others = {'C++': 'Bjarne Stroustrup', 'Swift': 'Chris Lattner'}
languages_programmers.update(others)
print("Словник після додавання елементів:", languages_programmers)
print("Наявність ключа 'Ruby' в словнику:", 'Ruby' in languages_programmers)
print("Значення за ключем 'РНР':", languages_programmers.get('PHP'))
print("Ітеративний список ключів:", languages_programmers.keys())
print("Список ключів:", list(languages_programmers.keys()))
print("Список значень:", list(languages_programmers.values()))
print("Список(кортеж) ключ-значення:", list(languages_programmers.items()))
"""

"""5.9
periodic_table = {'Hydrogen': 1, 'Helium': 2} 
print(periodic_table) 
carbon = periodic_table.setdefault('Ferrum', 26) 
print(periodic_table) 
print(carbon)

helium = periodic_table.setdefault('Helium', 101)
print(periodic_table)
print(helium)
"""

"""5.10
print(set('office'))
office = set('office')
numbers = {0, 1, 4, 5, 7, 9}
print(5 in numbers)
print('f' in office)
"""

