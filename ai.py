# 0-1-2-3-4-5-6-7-8

import math

scores = {
    'tie': 0,
    'x': -1,
    'o': 1
}


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


def changeMatrix(matrix, best_move):
    i, j = best_move//3, best_move % 3
    matrix[i][j] = 2
    return matrix


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
            best_score = max(best_score,score)
        return best_score

    else:
        best_score = math.inf
        for i in remain:
            temp = remain.copy()
            temp.remove(i)
            matrix_list[i] = 'x'
            score = minimax(matrix_list, temp, True, depth+1)
            matrix_list[i] = ' '
            best_score = min(best_score,score)
        return best_score


def unvisited_list(matrix):
    lst = []
    for i in range(3):
        for j in range(3):
            if matrix[i][j] == 0:
                lst.append(3*i + j)
    return lst


def player(matrix):
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
