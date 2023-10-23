# Написать игру в “Крестики-нолики”. Можете использовать
# любые парадигмы, которые посчитаете наиболее
# подходящими. Можете реализовать доску как угодно - как
# одномерный массив или двумерный массив (массив массивов).
# Можете использовать как правила, так и хардкод, на своё
# усмотрение. Главное, чтобы в игру можно было поиграть через
# терминал с вашего компьютера.

from random import randrange

print('\nИгра "Крестики-нолики", нужно вводить две цифры через пробел, от 1 до 3\n\
        Поле:\n\
        -------------\n\
        |1 1|1 2|1 3|\n\
        -------------\n\
        |2 1|2 2|2 3|\n\
        -------------\n\
        |3 1|3 2|3 3|\n\
        -------------\n')

name = []
symbol = ['O', 'X']
array = [''] * 3
for i in range(3):
    array[i] = [' '] * 3

name.append(input('Введите имя первого игрока - '))
name.append(input('Введите имя второго игрока - '))

gamer = randrange(2)
choice_symbol = randrange(2)
print(f'\nНачинает игрок {name[gamer]} и ходит "{symbol[choice_symbol]}"\n')
cell = 9

def fun(f):
    if f == 1:
        f = 0
    else:
        f += 1
    return f

def gamers(gamer):
    while True:
        x, y = map(int,input(f'Ход игрока {name[gamer]} - ').split())
        if x < 1 or y < 1 or y > 3 or x > 3:
            print('Такой клетки нет!')
        elif array[x - 1][y - 1] in 'XO':
                print('Эта клетка уже занята!')
        else:
            motion = array[x - 1][y - 1] = symbol[choice_symbol]
            return motion

while cell > 0:
    if gamer == 0:
        gamers(gamer)
    if gamer == 1:
        gamers(gamer)
    print('-------------')
    for i in range(3):
        print(f'| {array[i][0]} | {array[i][1]} | {array[i][2]} |')
        print('-------------')
    for i in range(3):
        if (array[i][0] == array[i][1] == array[i][2] == 'X') \
            or (array[i][0] == array[i][1] == array[i][2] == 'O') \
            or (array[0][i] == array[1][i] == array[2][i] == 'X') \
            or (array[0][i] == array[1][i] == array[2][i] == 'O'):
            print(f'Выиграл игрок {name[gamer]}')
            quit()
    if (array[0][0] == array[1][1] == array[2][2] == 'X') \
        or (array[0][0] == array[1][1] == array[2][2] == 'O') \
        or (array[2][0] == array[1][1] == array[0][2] == 'X') \
        or (array[2][0] == array[1][1] == array[0][2] == 'O'):
        print(f'Выиграл игрок {name[gamer]}')
        quit()
    
    if cell == 1:
        print(f'Победила дружба!')
        quit()

    gamer = fun(gamer)
    choice_symbol = fun(choice_symbol)
    cell -= 1
    