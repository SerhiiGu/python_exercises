
"""6. Виведіть представлення букви, яку вводить користувач, у символах азбуки Морзе . \
Фрагмент словника має такий вигляд: \
morse = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', ...}. \
Передбачте у програмі обробку малих і великих букв"""

morse = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.'}

#phrase = input('Введіть фразу: ')
phrase = 'AcBcfFadEeF'
#print('Початкова фраза:', phrase)
phrase = phrase.upper()
#print('Оновлена фраза:', phrase)
mor2 = ''
for key in list(phrase):
    mor2 = mor2 + ' ' + morse[key]
print(mor2)