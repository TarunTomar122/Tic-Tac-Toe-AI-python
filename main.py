"""
    This is the ai implementation of tic-tac-toe game from scratch.We have used pygame for making GUI and then using minimax algorithm we have
    created a play function that will predict the best possible move at any given instant and will make the move.
    You just can't defeat this. It's always gonna result in draw or human loosing.

"""

import pygame
from ai import *

width = 600
height = 600

# initialise pygame
pygame.init()

# Title and Icon
pygame.display.set_caption("TicTacToe")
icon = pygame.image.load("./assets/icon.png")
pygame.display.set_icon(icon)

# create the screen
screen = pygame.display.set_mode((width, height))

# loading Sprites
box = pygame.image.load('./assets/sprites/sprite_box.png')
cross = pygame.image.load('./assets/sprites/sprite_x.png')
zero = pygame.image.load('./assets/sprites/sprite_o.png')

# Matrix
matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Create a function to convert the coordinates to px


def coor_to_px(coordinates):
    x, y = coordinates
    return (x * 200, y * 200)

# CreateMatrix function
# 1 is equivalent to cross and 2 to zero


def createMatrix():
    for x in range(3):
        for y in range(3):
            if matrix[y][x] == 0:
                screen.blit(box, coor_to_px((x, y)))
            elif matrix[y][x] == 1:
                screen.blit(cross, coor_to_px((x, y)))
            else:
                screen.blit(zero, coor_to_px((x, y)))

# Position to Coordinate


def pos_to_coord(x, y):
    x = (x/200) % 3
    y = (y/200) % 3
    return int(x), int(y)


player_move = True

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if player_move:
            temp = is_game_over(convert_matrix_to_list(
                matrix), unvisited_list(matrix))

            if temp:
                print(temp)
                running = False
                break

            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                x, y = pos_to_coord(x, y)
                if matrix[y][x] == 0:
                    matrix[y][x] = 1
                    player_move = False

    if player_move == False:
        temp = play(matrix)
        if type(temp) == type('sd'):
            print(temp)
            running = False
        elif temp:
            matrix = temp
        player_move = True

    createMatrix()
    pygame.display.update()
