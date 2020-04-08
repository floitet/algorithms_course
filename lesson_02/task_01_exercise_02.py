# Задание №2 из списка заданий.
# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

a = int(input('Type in any natural number.'))

odd_digits = 0
even_digits = 0

while a:
    temp = a % 10
    if temp % 2 == 0:
        even_digits += 1
    else:
        odd_digits += 1
    a = a // 10

print(f'The amount of odd digits equals {odd_digits} \n'
      f'And the amount of even digits is {even_digits}.')

