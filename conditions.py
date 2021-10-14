
field = []


def conditions_row(i, j):
    return field[i][j], field[i][j + 1], field[i][j + 2], field[i][j + 3], field[i][j + 4]


def conditions_col(i, j):
    return field[j][i], field[j + 1][i], field[j + 2][i], field[j + 3][i], field[j + 4][i]


def conditions_left_diagonal(i, j):
    return field[i][j], field[i + 1][j + 1], field[i + 2][j + 2], field[i + 3][j + 3], field[i + 4][j + 4]


def conditions_right_diagonal(i, j):
    return field[i][j + 4], field[i + 1][j + 3], field[i + 2][j + 2], field[i + 3][j + 1], field[i + 4][j]
