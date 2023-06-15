#Вам нужно написать программу для подбора упаковок по размерам товара.
#Размеры (ширина, длина, высота) хранятся в переменных (в сантиметрах)
from decimal import Decimal

def get_box_class ():
    x, y, z = input("Введите 3 измерения:\n").split(sep=',')
    x = Decimal(x)
    y = Decimal(y)
    z = Decimal(z)
    if max(x, y, z) <= 15:
        return print("Коробка №1")
    elif max(x, y, z) >= 200:
        return print("Упаковка для лыж")
    for i in [x, y, z]:
        if i > 15 and i <50:
            return print ("Коробка №2")
    else:
        return print("Коробка №3")

get_box_class()