# Создайте программу для игры в ""Крестики-нолики"".

import random


def print_table(table):
    print('   1  2  3')
    count = 1
    for i in table:
        print(count, *i, sep='  ')
        count += 1


def check(table, flag):
    symbol = ''
    if flag:
        symbol = 'X'
    else:
        symbol = '0'
    x = [symbol, symbol, symbol]
    for i in table:
        if x == i:
            return True
    for i in [list(i) for i in zip(*table)]:
        if x == i:
            return True
    if [table[0][0], table[1][1], table[2][2]] == x or [table[0][2], table[1][1], table[2][0]] == x:
        return True
    return False


def input_cord(table):
    while True:
        try:
            inp = [x - 1 for x in list(map(int, input('Введите координаты через пробел: ').split()))]
            if table[inp[0]][inp[1]] != '*':
                print('Ошибка, это уже занятое поле. Повторите ввод.')
                continue
        except:
            print('Ошибка, некоректный ввод')
        else:
            return inp


def first_turn():
    f = random.randint(0, 1)
    if f == 0:
        return False
    else:
        return True


def turn(flag):
    if flag:
        print('Ходят крестики!')
    if not flag:
        print('Ходят нолики!')


def table_fill(table, inp, flag):
    if flag:
        table[inp[0]][inp[1]] = 'X'
    else:
        table[inp[0]][inp[1]] = '0'
    return table


table = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]
print_table(table)


# ---TURN---


flag = first_turn()
count = 0
win_check = False
while count <= 9:
    turn(flag)
    inp = input_cord(table)
    table = table_fill(table, inp, flag)
    print_table(table)
    win_check = check(table, flag)
    if win_check:
        break
    flag = not flag
    count += 1


# ---WIN---


if count > 9 and not win_check:
    print('Ничья. Попробуйте сыграть еще раз.')

if flag:
if flag:
    print('Ура, победили крестики!!!')
else:
    print('Ура, победили нолики!!!')