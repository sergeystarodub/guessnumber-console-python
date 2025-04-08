import random

def NumberPlayers():    # функция для задания количества игроков и их имен
    number = int(input("Введите количество игроков: "))
    
    # список для хранения имен игроков
    namelist = []

    # присваиваем игрокам имена
    for item in range(1, number + 1):
        playername = input("Введите имя игрока номер " + str(item) + ": ")
        # привожу имена к нижнему регистру для их дальнейшего сравнения
        playername = playername.lower()
        #namelist.append(playername)
        # цикл проверки есть ли одинаковые имена - нельзя использовать одинаковые имена

        while (True):

            if (playername in namelist):
                playername = input("Игрок с таким именем уже существует - введите другое имя игрока номер " + str(item) + ": ")
                playername = playername.lower()
            else:
                namelist.append(playername)
                break
    # цикл для замены строчных первых букв у имен на заглавные
    for n in range(len(namelist)):
       # здесь приходится применить str чтобы заработал capitalize - иначе синтаксис не подсвечивается а ПК зависает
       namelist[n] = str(namelist[n]).capitalize()
    # проверка-потом удалить
    #print(namelist)
    return namelist

# проверка
#print(NumberPlayers())

def RandomNumber():     # функция для случайного генерирования числа, которое нужно угадать-сложность задается диапазоном конечного числа
    while True:
        finalnumber = int(input("Введите конечное число. Вы сможете угадывать случайное число в диапазоне от 1 до введенного здесь числа. Чем больше число тем выше сложность: "))
        # проверка на ввод некорректного отрицательного значения
        if (finalnumber < 2):
            print("Введите корректное положительное значение или значение больше 1")
            continue
        else:
            break

    randnumber = random.randint(1, finalnumber)
    return randnumber

# проверка
#print(RandomNumber())

def main():
    # вводим количество игроков и их имена
    numplayer = NumberPlayers()
    # основной цикл игры - в конце будет спрашиваться хотят ли игрок(и) повторить игру или выйти
    while True:
    
        # список в котором будут храниться названные игроками числа
        numberlist = []
        # флажок, который будет сигнализировать об победе, чтобы выйти из цикла - если флаг равен 1 - выходим из цикла
        flag = 0

        # генерируем случайное число, которое надо угадать
        numrand = RandomNumber()
        # цикл чтобы игроки угадывали число непрерывно - пока не угадают
        while (flag == 0):
            # перебор игроков в списке их имен
            for player in numplayer:
                print(f'Угадывает число игрок {player}: ')
                # просьба ввести число
                guessednumber = int(input("Введите число: "))
                # цикл проверки содержится ли названное число в списке - было ли уже названо или нет
                while (guessednumber in numberlist):
                    print("Число уже было названо - введите число повторно.")
                    guessednumber = int(input("Введите число: "))

                # добавляем предполагаемое число в список, чтобы знать какие числа игроками были названы
                numberlist.append(guessednumber)
                if (guessednumber < numrand):
                    print("Названное число меньше угадываемого")
                elif (guessednumber > numrand):
                    print("Названное число больше угадываемого")
                elif (guessednumber == numrand):
                    print(f'Победа!!! Победил игрок {player} - было загадано число {numrand}')
                    # если flag равен 1 - Победа можно завершить цикл угадывания числа
                    flag = 1
                    break


        answer = input("Желаете повторить игру? y/n: ")
        if (answer == 'n'):
            break
        else:
            oldplayers = input("Хотите сыграть с прежним составом игроков? y/n: ")
            if (oldplayers == 'n'):
                # вводим количество игроков и их имена
                numplayer = NumberPlayers()
            else:
                # обнуляем список с названными числами игроков чтобы начать игру заново
                # может быть тут этот способ очистки списка излишен, так как при возврате к игровому циклу список заново инициализируется уже пустым - numberlist = []
                # Метод clear() доступен только в Python 3.3 и выше
                #numberlist.clear()
                continue

# вызов главной функции для запуска программы
main()
    











