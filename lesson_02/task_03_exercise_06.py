# Задание №6 из списка заданий.
# В программе генерируется случайное целое число от 0 до 100.
# Пользователь должен его отгадать не более чем за 10 попыток.
# После каждой неудачной попытки должно сообщаться, больше или меньше введенное пользователем число, чем то,
# что загадано.
# Если за 10 попыток число не отгадано, вывести правильный ответ.

from random import randint

print('Computer will pick one number from 0 to 100.\n'
      'You\'re gonna need to make the right guess. \n'
      'You\'re gonna have 10 attempts.')

start = 0
end = 100

rand_comp = randint(0, 100)

i = 0
while i < 10:
    user_guess = int(input('Your guess. Pick from 0 to 100.'))
    if user_guess != rand_comp:
        if user_guess > rand_comp:
            print('Go lower.')
        else:
            print('Go higher.')
        i += 1
    else:
        i = 11

if i == 10:
    print(f'You exceeded 10 attempts given.\n Computer\'s number was {rand_comp}.')
else:
    print(f'Congrats! Your guess is correct! \n Computer\'s number is {rand_comp}.')




