from tkinter import *
import random

root = Tk()
root.title('Criss-cross')
game_run = True
field = []
cross_count = 0


def new_game():
    for row in range(10):
        for col in range(10):
            field[row][col]['text'] = ' '
            field[row][col]['background'] = 'lavender'
    global game_run
    game_run = True
    global cross_count
    cross_count = 0


def click(row, col):
    if game_run and field[row][col]['text'] == ' ':
        field[row][col]['text'] = 'X'
        global cross_count
        cross_count += 1
        check_win('X')
        if game_run and cross_count < 100:
            computer_move()
            check_win('O')


def conditions_row(i, j):
    return field[i][j], field[i][j + 1], field[i][j + 2], field[i][j + 3], field[i][j + 4]


def conditions_col(i, j):
    return field[j][i], field[j + 1][i], field[j + 2][i], field[j + 3][i], field[j + 4][i]


def conditions_ldiag(i, j):
    return field[i][j], field[i + 1][j + 1], field[i + 2][j + 2], field[i + 3][j + 3], field[i + 4][j + 4]


def conditions_rdiag(i, j):
    return field[i][j + 4], field[i + 1][j + 3], field[i + 2][j + 2], field[i + 3][j + 1], field[i + 4][j]


def check_win(smb):
    for i in range(10):
        for j in range(6):
            check_line(*conditions_row(i, j), smb)
            check_line(*conditions_col(i, j), smb)
    for i in range(6):
        for j in range(6):
            check_line(*conditions_ldiag(i, j),
                       smb)
            check_line(*conditions_rdiag(i, j),
                       smb)


def check_line(a1, a2, a3, a4, a5, smb):
    if a1['text'] == smb and a2['text'] == smb and a3['text'] == smb and a4['text'] == smb and a5['text'] == smb:
        a1['background'] = a2['background'] = a3['background'] = a4['background'] = a5['background'] = 'pink'
        global game_run
        game_run = False


def can_win(a1, a2, a3, a4, a5, smb):
    res = False
    if a1['text'] == ' ' and a2['text'] == smb and a3['text'] == smb and a4['text'] == smb and a5['text'] == ' ':
        a5['text'] = 'O'
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
    if a1['text'] == ' ' and a2['text'] == smb and a3['text'] == smb and a4['text'] == smb and a5['text'] == ' ':
        a1['text'] = 'O'
        res = True
    if a1['text'] == ' ' and a2['text'] == smb and a3['text'] == smb and a4['text'] == smb and a5['text'] == smb:
        a1['text'] = 'O'
        res = True
    if a1['text'] == smb and a2['text'] == smb and a3['text'] == smb and a4['text'] == smb and a5['text'] == ' ':
        a5['text'] = 'O'
        res = True
    return res


def computer_move():
    for i in range(10):
        for j in range(6):
            if can_win(*conditions_row(i, j), 'O'):
                return
            if can_win(*conditions_col(i, j), 'O'):
                return
            if can_win(*conditions_row(i, j), 'X'):
                return
            if can_win(*conditions_col(i, j), 'X'):
                return

    for i in range(6):
        for j in range(6):
            if can_win(*conditions_ldiag(i, j),
                       'O'):
                return
            if can_win(*conditions_rdiag(i, j),
                       'O'):
                return
            if can_win(*conditions_ldiag(i, j),
                       'X'):
                return
            if can_win(*conditions_rdiag(i, j),
                       'X'):
                return

    while True:
        row = random.randint(0, 9)
        col = random.randint(0, 9)
        if field[row][col]['text'] == ' ':
            field[row][col]['text'] = 'O'
            break


for row in range(10):
    line = []
    for col in range(10):
        button = Button(root, text=' ', width=4, height=2,
                        font=('Verdana', 20, 'bold'),
                        background='lavender',
                        command=lambda row=row, col=col: click(row, col))
        button.grid(row=row, column=col, sticky='nsew')
        line.append(button)
    field.append(line)
new_button = Button(root, text='new game', command=new_game)
new_button.grid(row=10, column=0, columnspan=10, sticky='nsew')
root.mainloop()
