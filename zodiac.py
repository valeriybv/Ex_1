#Необходимо написать программу, которая будет запрашивать у пользователя месяц и дату рождения и выводить соответствующий знак зодиака
import datetime as dt

def get_zodiac (birth_date):
    if birth_date.month == 4:
       print("Овен") if birth_date.day < 20 else print("Телец")
    elif birth_date.month == 5:
        print("Телец") if birth_date.day < 21 else print("Близнецы")
    elif birth_date.month == 6:
        print("Близнецы") if birth_date.day < 21 else print("Рак")
    elif birth_date.month == 7:
        print("Рак") if birth_date.day < 22 else print("Лев")
    elif birth_date.month == 8:
        print("Лев") if birth_date.day < 23 else print("Дева")
    elif birth_date.month == 9:
        print("Дева") if birth_date.day < 22 else print("Весы")
    elif birth_date.month == 10:
        print("Весы") if birth_date.day < 23 else print("Скорпион")
    elif birth_date.month == 11:
        print("Скорпион") if birth_date.day < 22 else print("Стрелец")
    elif birth_date.month == 12:
        print("Стрелец") if birth_date.day < 21 else print("Козерог")
    elif birth_date.month == 1:
        print("Козерог") if birth_date.day < 20 else print("Водолей")
    elif birth_date.month == 2:
        print("Водолей") if birth_date.day < 18 else print("Рыбы")
    elif birth_date.month == 3:
        print("Рыбы") if birth_date.day < 20 else print("Овен")

date = dt.datetime.strptime(input("Введите строку день рождения в формате dd.mm.yyyy:\n"), '%d.%m.%Y').date()
get_zodiac(date)
