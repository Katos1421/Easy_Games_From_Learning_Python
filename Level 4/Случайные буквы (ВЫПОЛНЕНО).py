# Программа "Случайные буквы"
# Демонстрирует работу индексации строк

import random
word = (input('Введите ваше слово для индексации: '))
print('В переменной', word, 'хранится слово: ', word, '\n')
lenght = len(word)

indices = random.sample(range(lenght), lenght)
for position in indices:
    print(f'word[{position}]\t{word[position]}')

input('\n\nНажмите Enter, чтобы выйти')
