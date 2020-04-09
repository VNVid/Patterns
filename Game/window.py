import pygame
pygame.init()

def UpdateWindow(win, player):
    background_image = pygame.image.load('images/bg3.jpg')
    win.blit(background_image, (0, 0))
    #рисуем все кактусы игрока
    pygame.display.update()