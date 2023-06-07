"""4. Функція replace() може використовуватися для заміни будь-якого слова у рядку іншим словом. \
    Прочитайте кожен рядок зі створеного у попередньому завданні файла learning_python.txt \
    і замініть слово Python назвою іншої мови, наприклад C при виведенні на екран."""

lines = []
with open('c:\Merck\Python\Chapter8\\learning_python.txt', 'r') as file1:
    lines = [line.rstrip() for line in file1.readlines()]

print(lines)
for line in lines:
    print(str(line.replace('Python', 'Ruby')))
