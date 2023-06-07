with open('list_compare_old', 'r') as f:
    l_old = [line.strip() for line in f.readlines()]

with open('list_compare_new', 'r') as f:
    l_new = [line.strip() for line in f.readlines()]

# s = set(l_old)
# temp3 = [x for x in l_new if x not in s]
# print(len(temp3), temp3)

diff = list(set(l_new)-set(l_old))
# print(len(diff), diff)
print(' '.join(diff))
