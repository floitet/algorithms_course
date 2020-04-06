# Упражнение из списка заданий под номером 1.
# Получить сумму и произведение всех чисел
# трехзначного числа введенного пользователем

# вариант с извлечением цифр по индексу строки

# a = input('Type in one 3-digit number.')
# a1 = int(a[0])
# a2 = int(a[1])
# a3 = int(a[2])
# sum_digits = a1 + a2 + a3
# mul_digits = a1 * a2 * a3
# print(f'The summary of all digits in your number equals {sum_digits}. \n'
#       f'And the result of multiplying all digits in your number is {mul_digits}.')

# вариант с извлечением цифр через деление

a = int(input('Type in one 3-digit number.'))
a1 = a // 100
a2 = a % 100 // 10
a3 = a % 10
sum_digits = a1 + a2 + a3
mul_digits = a1 * a2 * a3
print(f'The summary of all digits in your number equals {sum_digits}. \n'
      f'And the result of multiplying all digits in your number is {mul_digits}.')

