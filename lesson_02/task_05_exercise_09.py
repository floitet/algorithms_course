
max_digits_sum = 0
result_number = 0

while True:
    a = int(input('Type in any natural number'))
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




