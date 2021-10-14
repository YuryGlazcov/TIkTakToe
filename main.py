from AI import *
from conditions import *
from tkinter import *

root = Tk()
root.title('TicTacToe')
global game_run
game_run = True
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
        if game_run and cross_count < 99:
            computer_move()
            check_win('O')


def check_win(smb):
    for i in range(10):
        for j in range(6):
            check_line(*conditions_row(i, j), smb)
            check_line(*conditions_col(i, j), smb)
    for i in range(6):
        for j in range(6):
            check_line(*conditions_left_diagonal(i, j),
                       smb)
            check_line(*conditions_right_diagonal(i, j),
                       smb)


def check_line(a1, a2, a3, a4, a5, smb):
    if a1['text'] == smb and a2['text'] == smb and a3['text'] == smb and a4['text'] == smb and a5['text'] == smb:
        a1['background'] = a2['background'] = a3['background'] = a4['background'] = a5['background'] = 'blue'
        global game_run
        game_run = False


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
