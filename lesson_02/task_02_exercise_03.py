# Задание №3 из списка заданий.
# Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
# Например, если введено число 3486, надо вывести 6843.

a = int(input('Input any natural number.'))

result = ''

while a:
    temp = str(a % 10)
    result += temp
    a = a // 10

int(result)
print(f'Your number taken backwards turns into: {result}.')
