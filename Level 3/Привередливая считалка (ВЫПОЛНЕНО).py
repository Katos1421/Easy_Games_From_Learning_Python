# Программа "Привередливая считалка"
# Демонстрирует работу операторов break и continue

count = 0
while True:
    count += 1
    # завершить цикл если счет пошел больше 10
    if count >= 10:
        break
    # пропустить 5
    if count == 5:
        continue
    print (count)
input('\n\nНажмите Enter, чтобы выйти')
