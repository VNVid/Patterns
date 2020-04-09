import pygame
pygame.init()

# imports of my files
from window import UpdateWindow
from player import Player

# окно игры
win = pygame.display.set_mode((1160, 1000))
pygame.display.set_caption("Game")

#Player
player = Player.getInstance()

# main loop
run = True
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    UpdateWindow(win, player)


pygame.quit()
