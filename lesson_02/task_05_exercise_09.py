# Задание №9 из списка заданий.
# Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

print('This script will be asking you to insert natural numbers. \n'
      'When the input process is finished it will find the number with the highest sum of digits.\n'
      'It will output this number and its digit\'s sum.\n'
      'To finish input type in 0.')


max_digits_sum = 0
result_number = 0

while True:
    a = int(input('Type in any natural number. Zero to quit.'))
    if a == 0:
        break
    stable_a = a
    digits_sum = 0
    while a:
        temp = a % 10
        digits_sum = digits_sum + temp
        a = a // 10
    if digits_sum >= max_digits_sum:
        max_digits_sum = digits_sum
        result_number = stable_a

print(f'The number with highest sum of digits is {result_number}\n'
      f'And this sum equals {max_digits_sum}')




