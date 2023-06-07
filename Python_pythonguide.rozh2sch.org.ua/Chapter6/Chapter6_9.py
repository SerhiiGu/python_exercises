"""9. Напишіть простий калькулятор, який зчитує три рядки, які вводить користувач: \
перше число, друге число і операцію, після чого застосовує операцію до введених числах \
(«перше число» «операція» «друге число») і виводить результат на екран. \
Підтримувані операції: +, -, /, *, mod, pow, div, де mod - це взяття залишку від ділення, \
pow - піднесення до степеня, div - цілочисельне ділення. \
У випадку ділення на 0, необхідно використати обробник винятку, який має вивести повідомлення Division by zero!"""

x = int(input('Перше число: '))
y = int(input('Друге число: '))
op = input('Операція: ')

match op:
    case '+':
        print(f'{x}+{y}={x + y}')
    case '-':
        print(f'{x}-{y}={x-y}')
    case '*':
        print(f'{x}*{y}={x*y}')
    case '/':
        if y == 0:
            print('Division by zero!')
        else:
            print(f'{x}/{y}={x/y}')
    case deafult:
        print('Unknown operation')