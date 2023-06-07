"""7. Обчисліть тривалість якоїсь події. Припустимо, учнівські канікули тривали кілька днів. 
На екран треба вивести у відформатованому вигляді 
(вирівнювання за лівим краєм, ширина поля: 10 знаків) загальну тривалість цієї події 
у годинах, хвилинах, секундах."""
days = int(9)
hours = days * 24
minutes = hours * 60
seconds = minutes * 60
print(str(days).ljust(10) + " days have:")
print(str(hours).ljust(10) + " hours")
print( str(minutes).ljust(10) + " minutes")
print(str(seconds).ljust(10) + " seconds")