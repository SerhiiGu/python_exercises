"""9. Визначте відсоток малих і великих літер у тексті, що зберігається у файлі. \
Скористайтеся, як зразком вхідного текстового файла, файл \
The Count of Monte Cristo( https://www.gutenberg.org/files/1184/1184-0.txt )  із сайту \
Project Gutenberg’s( https://www.gutenberg.org/ ). Використайте функцію isalpha()"""

import time

upper = 0
lower = 0
all = 0

with open('c:\Merck\Python\Chapter8\\monte_cristo.txt', 'r', encoding='utf8') as file1:
    lines = file1.readlines()
    for line in lines:
        for symbol in list(line.strip()):
            symbol = str(symbol)
            all += 1
            if symbol.isupper():
                #print(f'{symbol} upper')
                upper += 1
            elif symbol.islower():
                #print(f'{symbol} lower')
                lower +=1

print('All symbols:   ', all )
print('Upper:         ', upper )
print('Lower:         ', lower )
print('Upper percent: ', '{0:.3f}%'.format(upper/all*100))
print('Lower percent: ', '{0:.3f}%'.format(lower/all*100))
