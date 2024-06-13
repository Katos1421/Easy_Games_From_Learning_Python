# Программа "Орел или решка"
# Подбрасываем монетку 100 раз, и смотрим сколько из этих раз выпал орёл, а сколько решка.

import random

print('Привет, добро пожаловать в программу "Орел или Решка"')
turns = 0
heads = 0
tails = 0

while turns != 100:
    what_is_it = random.randint (1, 2)
    turns += 1
    if what_is_it == 1:
        heads += 1
    else:
        tails += 1

print('Итак, всего тебе выпало', heads, 'решек, и', tails, 'орлов из 100 раз. Поздравляем!')
input('\nНажмите Enter, чтобы выйти')

