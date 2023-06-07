"""10. Ви створюєте пригодницьку гру і використовуєте для зберігання предметів гравця словник, у якому ключі - \
це назви предметів, значення - кількість одиниць кожної із речей. Наприклад, словник може виглядати так: \
things = {'key': 3, 'mace': 1, 'gold coin': 24, 'lantern': 1, 'stone': 10}. Виведіть повідомлення про \
усі речі гравця у такому вигляді:"""


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


things = {'key': 3, 'mace': 1, 'gold coin': 24, 'lantern': 1, 'stone': 10}
print('Equipment:')
for e in things:
    print(f'{bcolors.OKGREEN}{things[e]}{bcolors.ENDC} {e}')
total = sum(things.values())
print(f'Total numbers of things: {total}')