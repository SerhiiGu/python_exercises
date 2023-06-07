"""8. Завантажте текстову версію книги The Life and Adventures of Robinson Crusoe By Daniel Defoe  \
із сайту Project Gutenberg’s( https://www.gutenberg.org/files/521/521-0.txt ). \
Витягніть із тексту заголовки усіх розділів, які мають вигляд, на зразок: CHAPTER I—START IN LIFE. \
Запишіть знайдені назви у новий файл chapters.txt"""

lst = []
with open('c:\Merck\Python\Chapter8\\daniel_defoe.txt', 'r', encoding='utf8') as file1:
    lines = file1.readlines()
    for line in lines:
        if 'CHAPTER' in line:
            lst.append(line.strip())

with open('c:\Merck\Python\Chapter8\\chapters.txt', 'w', encoding='utf8') as file1:
    file1.write('\n'.join(str(item) for item in lst))