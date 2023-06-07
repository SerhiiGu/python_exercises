"""5. Поміркуйте над тим, яку інформацію можна було б зберігати у списку. 
Наприклад, створіть список професій, видів спорту, членів родини, назви океанів тощо, 
а потім викличте кожну функцію для роботи зі списками, 
яка була згадана у цьому розділі, хоча б один раз."""

l1 = [ 'SSD' ,'HDD' , 'CPU', 'RAM', 'MB']
print('Original: ', l1)
l2 = l1.copy()
print('Copied list by "copy": ', l2)
l3 = list(l1)
print('Copied by function "list": ', l3)
l4 = l1[:]
print('Copied by concatenation: ', l4)
print('List lenght: ', len(l1))
print('String to list: ', list('mercury'))
l5 = '3 f 6 4 fsadf 324a'
l5 = l5.split(' ')
print('List with split: ', l5)
print('Join list to string: ', ''.join(l5))
print('Join original list to string: ', ''.join(l1))
print('Index of CPU in list: ', l1.index('CPU'))
l1[3] = 'KBD'
print('List with new 4rd element: ', l1)
print('2-3 element in list: ', l1[1:3])
print('Odd elements in list: ', l1[::2])
print('Reverse list: ', l1[::-1])
l1.append('RAM')
print('List wits appended last element: ', l1)
l1.insert(1, 'DVD')
print('List with new 2nd element: ', l1)
l1.extend(l2)
print('List after extend: ', l1)
del l1[0]
print('List after deleting 1st element: ', l1)
l1.remove('HDD')
print('List after deleting first "HDD" element', l1)
x1 = l1.pop(4)
print('Pop element: ', x1, ' and list after pop: ', l1)
print('SSD in list?', 'SSD' in l1)
print('Mouse in list?', 'MS' in l1)
print('Mouse not in list?', 'MS' not in l1)
print('Count of CPU in list:', l1.count('CPU'))
l2 = sorted(l1)
print('Sorted list(copy): ', l2)
print('Before sort list(in list)', l3)
l3.sort()
print('After sort list(in list): ', l3)
l3.reverse()
print('Reversed list: ', l3)
