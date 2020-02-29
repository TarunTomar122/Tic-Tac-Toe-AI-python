import pygame

width = 600
height = 600

# initialise pygame
pygame.init()

# Title and Icon
pygame.display.set_caption("TicTacToe")
icon = pygame.image.load("./assets/icon.png")
pygame.display.set_icon(icon)

# create the screen
screen = pygame.display.set_mode((width,height))

running = True

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((0,0,0))

    pygame.display.update()
