# Упражнение из списка заданий под номером 9
# Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

a = int(input('Type in first number'))
b = int(input('Type in second number'))
c = int(input('Type in third number'))

if a > b:
    if a > c:
        if b > c:
            print(f'The middle value equals {b}')
        else:
            print(f'The middle value equals {c}')
    else:
        print(f'The middle value equals {a}')
else:
    if b > c:
        if a > c:
            print(f'The middle value equals {a}')
        else:
            print(f'The middle value equals {c}')
    else:
        print(f'The middle value equals {b}')

