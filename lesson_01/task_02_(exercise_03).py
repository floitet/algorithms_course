# Упражнение 3 из списка заданий
# Вывести уравнение прямой вида y = kx + b
# по координатам двух точек, которые ввел пользователь

x1 = float(input('Type in first dot\'s axis "x" coordinate'))
y1 = float(input('Type in first dot\'s axis "y" coordinate'))
x2 = float(input('Type in second dot\'s axis "x" coordinate'))
y2 = float(input('Type in second dot\'s axis "y" coordinate'))

k = (y1 - y2) / (x1 - x2)
b = y2 - k * x2

print(f'The equation of the straight line connecting these two dots is:\n'
      f'y = {k}x + {b}')
