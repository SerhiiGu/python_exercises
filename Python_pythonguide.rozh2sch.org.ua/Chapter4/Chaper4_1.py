"""1. Збережіть назви мов світу (Ukrainian, French, Bulgarian, Norwegian, Latvian або інші) 
у списку. Простежте за тим, щоб елементи у списку не зберігались в алфавітному порядку.
 Застосуйте функції sorted(), reverse(), sort() до списку. Виведіть список на екран 
 до і після використання кожної із функцій."""

 
languages = ['Georgian', 'Estonian', 'Ukrainian', 'French' , 'Latvian']
print("Original", languages)
l2 = sorted(languages)
print("After sorted: ", l2, languages)
languages.sort()
print("After sort: ", languages)
languages.reverse()
print("After reverse: ", languages)
