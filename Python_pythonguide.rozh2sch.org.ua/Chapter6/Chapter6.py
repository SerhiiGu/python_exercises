"""number = [number for number in range(1,66) if number %4 == 1]
print(number)

word = 'Antarctica'
letter_counts = {letter: word.count(letter) for letter in word}
print(letter_counts)
letter_counts = {letter: word.count(letter) for letter in set(word)}
print(letter_counts)

print(sum(range(1,51)))

months = [(1, 'January'), (9, 'September'), (7, 'July'), (4, 'March')]
print(sorted(months, key=lambda x: x[1]))
print(sorted(months))

short_list = [1, 2, 3]
position = 5
try:
    short_list[position]
except:
    print('Need a position between 0 and', len(short_list)-1, 'but got', position)


try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero!")


lst = [ num for num in range(3,61)]
print(lst)
i=1
while i<61-3:
    print(lst[i])
    i += 1
"""
