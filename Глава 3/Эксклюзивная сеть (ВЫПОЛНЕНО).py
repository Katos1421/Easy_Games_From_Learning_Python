# Программа "Эксклюзивная сеть"
# Попытка воссоздать что-то вроде Фейсбука или даже Вконтакте. По-крайней мере, попытка - не пытка :)
print('\tЭксклюзивная компьютерная сеть')
print('\tТолько для зарегистрированных пользователей')
security = 0
username = ""
while not username:
    username = input('Логин: ')
password = ""
while not password:
    password = input('Пароль: ')
if username == "D. Voronin" and password == "KatoS":
    print ('Добро пожаловать, Катос')
    security = 5
elif username == "S. Meier" and password == "Civilization":
    print ('Добро пожаловать, Сид')
    security = 3
elif username == "S. Miyamoto" and password == "Mariobros":
    print ('Доброго времени суток, Сигеру')
    security = 3
elif username == "W. Wright" and password == "thesims":
    print ('Как дела, Уилл?')
    security = 3
elif username == "guest" or password == "guest":
    print ('Добро пожаловать к нам в гости!')
    security = 1
else:
    print ('Войти в систему не удалось. Возможно, не такой уж вы и эксклюзивный гражданин...\n')
input('\n\nНажмите Enter, чтобы выйти')
