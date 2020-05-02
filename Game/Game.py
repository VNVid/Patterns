import pygame
pygame.init()

# imports of my files
from window import UpdateWindow
import player

# окно игры
win = pygame.display.set_mode((1160, 800))
win.fill((255, 255, 255))
pygame.display.set_caption("Game")

#Player
player = player.Player.getInstance()

# main loop
frequency_of_update = 30
curtime = 0
gameover = False
run = True
while run:
    pygame.time.delay(10)

    curtime += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Достать текущую позицию мыши.
            player_position = pygame.mouse.get_pos()
            x = player_position[0]
            y = player_position[1]

            empty = player.emptyspace

            #BUY BUTTONS
            if 1000 < x and x < 1110:
                if 50 < y and y < 90:
                    player.buyCommand(0)
                elif 100 < y and y < 140:
                    player.buyCommand(1)
                elif 150 < y and y < 190:
                    player.buyCommand(2)
            #FIRST POSITION
            if not empty[0]:
                if 710 < y and y < 740:
                    if 220 < x and x < 280:
                        player.waterCommand(0)
                    elif 290 < x and x < 350:
                        player.feedCommand(0, 2)
                    elif 360 < x and x < 420:
                        player.feedCommand(0, 4)
                elif 760 < y and y < 790 and 290 < x and x < 350:
                    player.sellCommand(0)
            #SECOND POSITION
            if not empty[1]:
                if 710 < y and y < 740:
                    if 450 < x and x < 510:
                        player.waterCommand(1)
                    elif 520 < x and x < 580:
                        player.feedCommand(1, 2)
                    elif 590 < x and x < 650:
                        player.feedCommand(1, 4)
                elif 760 < y and y < 790 and 520 < x and x < 580:
                    player.sellCommand(1)
            #THIRD POSITION
            if not empty[2]:
                if 710 < y and y < 740:
                    if 660 < x and x < 720:
                        player.waterCommand(2)
                    elif 730 < x and x < 790:
                        player.feedCommand(2, 2)
                    elif 800 < x and x < 860:
                        player.feedCommand(2, 4)
                elif 760 < y and y < 790 and 730 < x and x < 790:
                    player.sellCommand(2)

    UpdateWindow(win, player, curtime, frequency_of_update, gameover)


pygame.quit()

