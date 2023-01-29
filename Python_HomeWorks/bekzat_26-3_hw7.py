ten = list(range(1, 11))
print(ten)
evens = list(filter(lambda i: i % 2 == 0, ten))
evens2 = list(map(lambda i: i ** 2, evens))


def func(lst: list):
    while True:
        try:
            index = input("Введите индекс: ").lower()

            if index == "exit" or index == "выход":
                print("Программа завершается: ")
                break
            print(lst[int(index)])
        except:
            print(f"Вводите только числа от 0 до {len(ten) - 1}")


func(ten)
