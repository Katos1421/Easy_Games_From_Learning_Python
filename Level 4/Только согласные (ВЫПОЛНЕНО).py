# Только согласные
# Демонстрирует, как создавать новые строки из исходных с помощью цикла for
message = input('Введитек текст: ')
new_message = ""
VOWELS = "aeiouyаеёиоуыэюя"
print()
for letter in message:
    if letter.lower() not in VOWELS:
        new_message += letter
        print('Создана новая строка: ', new_message)
print('Вот ваш текст с изъятыми гласными буквами:', new_message)
input('\nНажмите Enter, чтобы выйти')