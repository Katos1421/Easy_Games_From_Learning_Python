# Кости
# Демонстрирует работу случайных (псевдослучайных чисел).
import random
# создание случайного числа из диапазона 1-6
dice1 = random.randint(1,6)
dice2 = random.randrange(6) + 1
total = dice1 + dice2
print("При вашем броске выпало", dice1, "и", dice2, "очков, в сумме", total)
input("\nPress Enter to quit")
