"""7. Створіть багаторівневий словник subjects навчальних предметів. Використайте наступні рядки для ключів \
верхнього рівня: 'science', 'humanities' і 'public'. Зробіть так, щоб ключ 'science' був ім’ям іншого словника, \
який має ключі 'physics', 'computer science' і 'biology'. Зробіть так, щоб ключ 'physics' посилався на \
список рядків зі значеннями 'nuclear physics', 'optics' і 'thermodynamics'. Решта ключів повинні посилатися \
на порожні словники. Виведіть на екран ключі subjects['science'] і значення subjects['science']['physics']"""


physics = {'nuclear physics' : [], 'optics' : [], 'thermodynamics' : []}
print('Перший рівень:', physics)
science = {'physics' : physics, 'computer science' : [], 'biology' : []}
print('Другий рівень:', science)
subjects = {'science' : science, 'humanities' : [], 'public' : []}
print('Третій рівень:', subjects)

print("subjects['science'].keys()=", subjects['science'].keys())
print("subjects['science']['physics']=", list(subjects['science']['physics'].items()))
