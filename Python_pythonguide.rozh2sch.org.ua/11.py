#import datetime
#today = datetime.datetime.now()
#x = str(today)  # Output: '2016-09-15 06:58:46.915000'
#y = repr(today) # Output: 'datetime.datetime(2016, 9, 15, 6, 58, 46, 915000)'
#print(x)
#print(y)

#y=[x + 1 for x in (1, 2, 3)]
#print(y)

#[print(x) for x in range(10)]

squares = [x * x for x in range(2, 10)]
print(squares)
print()

cubes = [x*x*x for x in range(2, 10)]
print(cubes)

#from random import randrange
#range = [randrange(10, 99) for _ in range(10)]
#print(range)