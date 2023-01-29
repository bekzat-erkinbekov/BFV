start = 1
finish = 100
c = 0
qwerty = []

while True:
    current = (start + finish) // 2
    isright = input(f"Ваше число: {current}?   Да, больше(>) меньше(<): ")
    c += 1
    qwerty.append(current)
    if isright == "Да":
        print("Игра завершена...")
        break
    elif isright == ">":
        start = current + 1
    elif isright == "<":
        finish = current - 1
    else:
        print("Пишите только '<','>'")
    with open("result.txt", "w") as file:
        file.write(f"Количество попыток: {c}\n")
        file.write(f"Список попыток: {qwerty}\n")
        file.write(f"Загаданное число: {current - 1}")
