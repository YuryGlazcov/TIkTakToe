from conditions import *
import random

"""
 Функция can_win отвечает на проверку паттернов победы(кроме "вилки")
 Всего паттернов 6:
 -XXXX
 X-XXX
 XX-XX
 XXX-X
 XXXX-
 -XXX- Данный паттерн является отработкой выйгрышного паттерна -XXXX- где победа гарантирована
"""


def can_win(a1, a2, a3, a4, a5, smb):
    res = False
    if a1['text'] == ' ' and a2['text'] == smb and a3['text'] == smb and a4['text'] == smb and a5['text'] == ' ':
        a5['text'] = 'O'
        res = True
    if a1['text'] == ' ' and a2['text'] == smb and a3['text'] == smb and a4['text'] == smb and a5['text'] == smb:
        a1['text'] = 'O'
        res = True
    if a1['text'] == smb and a2['text'] == smb and a3['text'] == smb and a4['text'] == ' ' and a5['text'] == smb:
        a4['text'] = 'O'
        res = True
    if a1['text'] == smb and a2['text'] == smb and a3['text'] == ' ' and a4['text'] == smb and a5['text'] == smb:
        a3['text'] = 'O'
        res = True
    if a1['text'] == smb and a2['text'] == ' ' and a3['text'] == smb and a4['text'] == smb and a5['text'] == smb:
        a2['text'] = 'O'
        res = True
    if a1['text'] == smb and a2['text'] == smb and a3['text'] == smb and a4['text'] == smb and a5['text'] == ' ':
        a5['text'] = 'O'
        res = True

    if a1['text'] == ' ' and a2['text'] == smb and a3['text'] == smb and a4['text'] == smb and a5['text'] == ' ':
        a1['text'] = 'O'
        res = True

    return res


"""
Логика ходов компьютера проста - проводится проверка на обнаруженные паттерны
Если паттерны не найдены компьютер ходит рандомно в пределах игрового поля
"""


def computer_move():
    for smb in ['O', 'X']:
        for i in range(10):
            for j in range(6):
                if can_win(*conditions_row(i, j), smb):
                    return
                if can_win(*conditions_col(i, j), smb):
                    return

        for i in range(6):
            for j in range(6):
                if can_win(*conditions_left_diagonal(i, j),
                           smb):
                    return
                if can_win(*conditions_right_diagonal(i, j),
                           smb):
                    return

    while True:
        row = random.randint(0, 9)
        col = random.randint(0, 9)
        if field[row][col]['text'] == ' ':
            field[row][col]['text'] = 'O'
            break
