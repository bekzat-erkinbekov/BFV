gls = "aueioyAYOIEUаеуыоэяиюУЕЫАРОЛЭЯИЮ"
sgl = "qwrtpsdfghjklxzcvbnmQWRTPSDFGHJKLXZCVBNMйцкнгшщзхъфвпрлджчсмтьбЙЦКНГШЩЗХЪФВПРЛДЖЧСМТЬБ"
while True:
    gls2 = 0
    sgl2 = 0
    word = input("Введите слово/Enter the word: ").lower()
    if word == "exit" or word == "выйти":
        print("Завершение...")
        break
    letter = len(word)
    for i in word:
        if i in gls:
            gls2+=1
        elif i in sgl:
            sgl2 +=1
    print("Cлово: ", word)
    print("Количество букв: ", len([i for i in word if i.isalpha()]))
    print("Гласных букв: ", gls2)
    print("Согласных букв: ", sgl2 )
    print(f"глассные/соглассные {round(gls2/len(word) * 100, 2)} % {round(sgl2/len(word) * 100, 2)}")
