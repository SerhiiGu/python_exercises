"""8. Створіть словник з ім’ям cities. Використайте назви трьох міст в якості ключів словника. \
Створіть словник з інформацією про кожне місто: включіть в нього країну, в якій розташоване місто, \
приблизну чисельність населення і один цікавий факт про місто. Ключі словника кожного міста повинні називатися \
country, population і fact. Виведіть назву кожного міста і всю збережену інформацію про нього."""

Tokyo = {'country' : 'Japan', 'population' : '30mil', 'fact' : 'biggest aglomeration it the world'}
Beijin = {'country' : 'China', 'population' : '20mil', 'fact' : 'Have closed city palace'}
Kyiv = {'country' : 'Ukraine', 'population' : '2.5mil', 'fact' : 'More 1000 years old'}
cities = { 'Tokyo' : Tokyo, 'Beijin' : Beijin, 'Kyiv' : Kyiv}

for key in cities:
    print('\nCity:', key, end='.  ')
    for key2 in cities[key]:
        print(cities[key][key2], end=' ')
    