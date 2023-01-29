day = int(input("Введите день рождение: "))
month = int(input("Введите месяц рождение: "))
otvet = "Ваш знак зодиака "
if (month == 3) and (day >= 21) and (day <= 31) or (month == 4) and (day >= 1) and (day <= 20):
    print(otvet + " Овен")
elif (month == 4) and (day >= 21) and (day <= 31) or (month == 5) and (day >= 1) and (day <= 21):
    print(otvet + " Телец")
elif (month == 5) and (day >= 21) and (day <= 31) or (month == 6) and (day >= 1) and (day <= 20):
    print(otvet + " Близнецы")
elif (month == 6) and (day >= 21) and (day <= 31) or (month == 7) and (day >= 1) and (day <= 20):
    print(otvet + " Рак")
elif (month == 7) and (day >= 21) and (day <= 31) or (month == 8) and (day >= 1) and (day <= 20):
    print(otvet + " Лев")
elif (month == 8) and (day >= 21) and (day <= 31) or (month == 9) and (day >= 1) and (day <= 20):
    print(otvet + " Дева")
elif (month == 9) and (day >= 21) and (day <= 31) or (month == 10) and (day >= 1) and (day <= 20):
    print(otvet + " Весы")
elif (month == 10) and (day >= 21) and (day <= 31) or (month == 11) and (day >= 1) and (day <= 20):
    print(otvet + " Скорпион")
elif (month == 11) and (day >= 21) and (day <= 31) or (month == 12) and (day >= 1) and (day <= 20):
    print(otvet + " Стрелец")
elif (month == 12) and (day >= 21) and (day <= 31) or (month == 1) and (day >= 1) and (day <= 20):
    print(otvet + " Козерог")
elif (month == 1) and (day >= 21) and (day <= 31) or (month == 2) and (day >= 1) and (day <= 20):
    print(otvet + " Водолей")
elif (month == 2) and (day >= 21) and (day <= 31) or (month == 3) and (day >= 1) and (day <= 20):
    print(otvet + " Рыбы")
else:
    print("Введите правильное значение!")