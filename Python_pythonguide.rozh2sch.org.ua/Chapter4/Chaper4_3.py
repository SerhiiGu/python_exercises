"""3. Дано список з такими елементами: 
cities = ['Budapest', 'Rome', 'Istanbul', 'Sydney', 'Kyiv', 'Hong Kong']. 
Сформуйте з елементів списку повідомлення, у якому перед останнім елементом буде вставлено 
слово and. Наприклад, у нашому випадку, повідомлення буде таким: 
Budapest, Rome, Istanbul, Sydney, Kyiv and Hong Kong. 
Програма має працювати з будь-якими списками, довжина яких є 6"""


cities = ['Budapest', 'Rome', 'Istanbul', 'Sydney', 'Kyiv', 'Hong Kong']
cities.insert(5, 'and')
print(cities)
print(' '.join(cities))