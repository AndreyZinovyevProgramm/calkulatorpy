menu = int(input('1 - сложение, 2 - умножать, 3 - вычитать, 4 - деление: '))

def ggg(a,b):
    return a * b


def bb(a,b):
    return a / b


def hh(a,b):
    return a - b


def gg(a,b):
    return a + b

if (menu == 1):
    print('Вы выбрали сложение')
    x = int(input('Напишите 1 число:'))
    y = int(input('Напишите 2 число:'))
    print(gg(x,y))



if (menu == 2):
    print('Вы выбрали умножение')
    x = int(input('Напишите 1 число:'))
    y = int(input('Напишите 2 число:'))
    print(ggg(x,y))


if(menu == 3):
    print('Вы выбрали вычитание')
    x = int(input('Напишите 1 число:'))
    y = int(input('Напишите 2 число:'))
    print(hh(x,y))


if(menu == 4):
    print('Вы выбрали деление')
    x = int(input('Напишите 1 число:'))
    y = int(input('Напишите 2 число:'))
    print(bb(x,y))










if (menu > 4):
    print('Данного действия не существует') 


















