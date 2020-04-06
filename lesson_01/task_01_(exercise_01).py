# Упражнение из списка заданий под номером 1.
# Получить сумму и произведение всех цифр
# трехзначного числа введенного пользователем

a = int(input('Type in one 3-digit number.'))
a = abs(a)
a1 = a // 100
a2 = a % 100 // 10
a3 = a % 10
sum_digits = a1 + a2 + a3
mul_digits = a1 * a2 * a3
print(f'The summary of all digits in your number equals {sum_digits}. \n'
      f'And the result of multiplying all digits in your number is {mul_digits}.')

