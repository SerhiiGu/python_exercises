"""12. Чи є рядок «паліндромом»? Рядок є паліндромом, якщо він однаково читається зліва направо та справа наліво. \
Наприклад, слова Level, Noon, Anna є паліндромами, незалежно від регістру літер. Рядки, які треба перевірити, \
вводяться користувачем. Введення даних можна перервати, якщо ввести слово escape. Програма повинна вивести \
результат перевірки у вигляді повідомлення is a palindrome або is not a palindrome """

while True:
    word = input('Введіть слово(esc для виходу): ')
    if word == 'esc': 
        exit()
    word = word.lower()
    if str(word) == str(word)[::-1] :
        print("Palindrome")
    else:
        print("Not Palindrome")