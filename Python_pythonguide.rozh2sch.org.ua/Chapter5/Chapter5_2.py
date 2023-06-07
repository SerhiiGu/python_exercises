"""2. Cтворіть словник з трьома річками і регіонами, територією яких вони протікають. \
Одна з можливих пар «ключ: значення» - 'Amazon': 'South America'. \
Додайте ще дві пари «річка: регіон» у словник. \
Виведіть повідомлення із назвами річки і регіону - наприклад, «The Amazon runs through South America.» \
для усіх елементів словника, враховуючи те, що у повідомлення у відповідні місця \
підставляються назви річок і територій."""

rivers = {'Amazon' : 'South America', 'Dnipro' : 'Europe', 'Main' : 'Europe'}
for key in rivers:
   print ("River", key , "runs through", rivers[key])

print('')
for key in rivers:
    print(f'River {key} runs through {rivers[key]}')
    