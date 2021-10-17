from AI import *
from tkinter import *

global game_run
game_run = True     # Переменная отвечающая за проведение игры. При значении False ходы становятся недоступными.
cross_count = 0     # Счетчик крестиков


def new_game():  # Начало новой игры.
    for row in range(10):
        for col in range(10):
            field[row][col]['text'] = ' '
            field[row][col]['background'] = 'lightgray'
    global game_run
    game_run = True
    global cross_count
    cross_count = 0


def click(row, col):  # Отработка нажатий. При ничьей инициализирует новую игру
    if game_run and field[row][col]['text'] == ' ':
        field[row][col]['text'] = 'X'
        global cross_count
        cross_count += 1
        check_win('X')
        if game_run and cross_count < 51:
            computer_move()
            check_win('O')
        if cross_count == 51:
            new_game()


def check_win(smb):  # Проверка на победу
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


def check_line(a1, a2, a3, a4, a5, smb):  # В случае победной серии выделяется победная серия и игра завершается
    if a1['text'] == smb and a2['text'] == smb and a3['text'] == smb and a4['text'] == smb and a5['text'] == smb:
        a1['background'] = a2['background'] = a3['background'] = a4['background'] = a5['background'] = 'gold'
        global game_run
        game_run = False


def print_game():  # отрисовка игрового поля
    root = Tk()
    root.title('TicTacToe')
    for row in range(10):
        line = []
        for col in range(10):
            button = Button(root, text=' ', width=2, height=1,
                            font=('ComicSans', 20, 'italic'),
                            background='lightgray',
                            command=lambda row=row, col=col: click(row, col))
            button.grid(row=row, column=col, sticky='nsew')
            line.append(button)
        field.append(line)
    new_button = Button(root, text='Новая игра', background='pink', command=new_game)
    new_button.grid(row=10, column=0, columnspan=10, sticky='nsew')
    root.mainloop()


print_game()
