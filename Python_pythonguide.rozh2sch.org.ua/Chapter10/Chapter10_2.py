"""2. Облік користувачів на сайті.
a. Створіть клас з ім’ям User. Створіть два атрибути first_name і last_name, а потім ще кілька атрибутів, \
    які зазвичай зберігаються у профілі користувача. Напишіть метод describe_user який виводить \
    повне ім’я користувача. Створіть ще один метод greeting_user() для виведення персонального вітання \
    для користувача. Створіть кілька примірників, які представляють різних користувачів. \
    Викличте обидва методи для кожного користувача.
b. Додайте атрибут login_attempts у клас User. Напишіть метод increment_login_attempts(), що збільшує значення \
    login_attempts на 1. Напишіть інший метод з ім’ям reset_login_attempts(), обнуляє значення login_attempts. \
    Створіть екземпляр класу User і викличте increment_login_attempts() кілька разів. \
    Виведіть значення login_attempts, щоб переконатися у тому, що значення було змінено правильно, \
    а потім викличте reset_login_attempts(). Знову виведіть login_attempts і переконайтеся у тому, \
    що значення обнулилося.
c. Адміністратор - користувач з повними адміністративними привілеями. Напишіть клас з ім’ям Admin, що успадковує \
    від класу User. Додайте атрибут privileges для зберігання списку рядків виду «Allowed to add message», \
    «Allowed to delete users», «Allowed to ban users» і т. д. Напишіть метод show_privileges() для виведення \
    набору привілеїв адміністратора. Створіть екземпляр Admin і викличте метод.
d. Напишіть клас Privileges. Клас повинен містити всього один атрибут privileges зі списком, який треба забрати \
    із класу Admin. Водночас, необхідно перемістити метод show_privileges() у клас Privileges із класу Admin. \
    Створіть екземпляр priv як атрибут класу Admin. Створіть новий екземпляр admin і використайте метод \
    для виведення списку привілеїв.
e. Збережіть клас User в одному модулі, а класи Privileges і Admin у іншому модулі. В окремому файлі створіть \
    екземпляр admin і викличте метод show_privileges(), щоб перевірити, що все працює правильно."""

import privadm

user1 = privadm.user.User('John', 'Smith')
user1.greeting_user()
user1.describe_user()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print('login_attempts after increase:', user1.login_attempts)
user1.reset_login_attempts()
print('login_attempts after reset:', user1.login_attempts)

admin = privadm.Admin('John', 'Doe', ['Allowed to delete users', 'Allowed to ban users'])
admin.describe_user()
admin.privileges.show_privileges()
