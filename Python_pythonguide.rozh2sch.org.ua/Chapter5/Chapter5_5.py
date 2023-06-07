"""5. Створіть кілька словників, імена яких - це клички домашніх тварин. \
У кожному словнику збережіть інформацію про вид домашнього улюбленця та ім’я власника. \
Збережіть словники в списку з ім’ям pets. \
Виведіть кілька повідомлень типу Alex is the owner of a pet - a dog"""

l1 = {'Max' : 'Barry', 'Teddy' : 'Sam'}
l2 = {'Rose' : 'Marie', 'Chip' : 'Yulia'}

pets = l1
pets.update(l2)
print(pets)
print(list(pets))
for key in pets:
    print(f'Pet {key} belongs to {pets[key]}')
