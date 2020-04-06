# Упражнение из списка заданий под номером 8
# Определить, является ли год, который ввел пользователь, високосным или не високосным.

a = int(input('Type in any year in 4-digit format.'))

if a % 4 == 0:
    if a % 100 == 0:
        if a % 400 == 0:
            print(f'{a} is actually a leap year.')
        else:
            print(f'{a} is not a leap year.')
    else:
        print(f'{a} is actually a leap year.')
else:
    print(f'{a} is not a leap year.')

