"""3. Створіть словник з чотирма назвами мов програмування (ключі) та іменами розробників цих мов (значення). \
Виведіть по черзі для усіх елементів словника повідомлення типу My favorite programming language is Python. \
It was created by Guido van Rossum.. Видаліть, на ваш вибір, одну пару «мова: розробник» із словника. \
Виведіть словник на екран."""

languages_programmers = {'PHP': 'Rasmus Lerdorf', 'Scala': 'Martin Odersky', 'JavaSript': 'Brendan Eich', \
'Python': 'Guido van Rossum', 'C': 'Dennis Ritchie', 'Ruby': 'Yukihiro Matsumoto'}

for key in languages_programmers:
    print(f'My fav lang is {key}. It was created by {languages_programmers[key]}')
print()
del languages_programmers['Scala']
for key in languages_programmers:
    print(f'My fav lang is {key}. It was created by {languages_programmers[key]}')
    