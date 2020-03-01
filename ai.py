"""
    We are converting the normal matrix into a flatten one dimensional list with the positions marked as 0-1-2-3-4-5-6-7-8.
    This way it is easier for us to implement check whether the game is over or someone has won.
    We are storing the positions that are free to move on in another list that is being created by one separate function.
"""


import math

# Defining Scores for any game ending situation
scores = {
    'tie': 0,
    'x': -1,
    'o': 1
}

# A function that will change the game matrix into that one dimensional flat list


def convert_matrix_to_list(matrix):
    lst = []
    for i in range(3):
        for j in range(3):
            if matrix[i][j] == 0:
                lst.append(' ')
            if matrix[i][j] == 1:
                lst.append('x')
            if matrix[i][j] == 2:
                lst.append('o')
    return lst


# This function will manipulate the matrix to play a certain "best" move
def changeMatrix(matrix, best_move):
    i, j = best_move//3, best_move % 3
    matrix[i][j] = 2
    return matrix

# This game will keep an eye on the game state and will check if game is over or someone has won.


def is_game_over(matrix_list, remain):
    player_symbol = ['x', 'o']
    winning_positions = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [
        0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for pos in winning_positions:
        if matrix_list[pos[0]] != ' ':
            if matrix_list[pos[0]] == matrix_list[pos[1]] and matrix_list[pos[1]] == matrix_list[pos[2]]:
                return matrix_list[pos[0]]
    if len(remain) == 0:
        return 'tie'
    else:
        return False

# This function is the main minimax algorithm itself


def minimax(matrix_list, remain, is_ai, depth):
    if is_game_over(matrix_list, remain):
        winner = is_game_over(matrix_list, remain)
        return scores[winner]
    if is_ai:
        best_score = -math.inf
        for i in remain:
            temp = remain.copy()
            temp.remove(i)
            matrix_list[i] = 'o'
            score = minimax(matrix_list, temp, False, depth+1)
            matrix_list[i] = ' '
            best_score = max(best_score, score)
        return best_score

    else:
        best_score = math.inf
        for i in remain:
            temp = remain.copy()
            temp.remove(i)
            matrix_list[i] = 'x'
            score = minimax(matrix_list, temp, True, depth+1)
            matrix_list[i] = ' '
            best_score = min(best_score, score)
        return best_score

# This function will return the list of unvisited places in the matrix


def unvisited_list(matrix):
    lst = []
    for i in range(3):
        for j in range(3):
            if matrix[i][j] == 0:
                lst.append(3*i + j)
    return lst

# This is the driver function that will implement all the above function to play the move of 'AI'


def play(matrix):
    remain = unvisited_list(matrix)
    matrix_list = convert_matrix_to_list(matrix)

    if is_game_over(matrix_list, remain):
        return is_game_over(matrix_list, remain)

    best_score = -math.inf
    best_move = ''
    for i in remain:
        temp = remain.copy()
        temp.remove(i)
        matrix_list[i] = 'o'
        score = minimax(matrix_list, temp, is_ai=False, depth=0)
        matrix_list[i] = ' '
        if score > best_score:
            best_move = i
            best_score = score
    return changeMatrix(matrix, best_move)
