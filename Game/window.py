import  colours
import pygame
pygame.init()

zero_point = (0, 0)
buy_button_outlook1 = (1000, 50, 110, 40)
buy_button_outlook2 = (1000, 100, 110, 40)
buy_button_outlook3 = (1000, 150, 110, 40)
buy_button_text = (1030, 30)
buy_button_text1 = (1030, 60)
buy_button_text2 = (1030, 110)
buy_button_text3 = (1030, 160)
money_text = (20, 10)
gameover_text = (300, 300)
score_text = (300, 600)

def UpdateWindow(win, player, curtime, frequency_of_update, gameover):
    background_image = pygame.image.load('images/bg3.jpg')
    win.blit(background_image, zero_point)
    # обновления состояний (-water и прочее)
    #GameOver = player.update
    if curtime % frequency_of_update == 0:
        player.update(win)
    gameover = player.is_over()
    if gameover == True:
        win.fill(colours.GOLDENROD1)
        f1 = pygame.font.Font(None, 100)
        text1 = f1.render('GAME OVER', 1, colours.CRIMSON)
        win.blit(text1, gameover_text)
        text2 = f1.render('YOUR SCORE ' + str(player.score), 1, colours.CRIMSON)
        win.blit(text2, score_text)
        pygame.display.update()
        return

    #рисуем все кактусы игрока
    player.draw(win)
    #рисуем общие кнопки и пишем тексты
    #SHOP
    f1 = pygame.font.Font(None, 30)
    text1 = f1.render('Shop:', 1, colours.BLACK)
    win.blit(text1, buy_button_text)
    buy_button1 = pygame.draw.rect(win, colours.SAPGREEN, buy_button_outlook1);
    buy_button2 = pygame.draw.rect(win, colours.SAPGREEN, buy_button_outlook2);
    buy_button3 = pygame.draw.rect(win, colours.SAPGREEN, buy_button_outlook3);
    text2 = f1.render('Rebutia (2$)', 1, colours.BLACK)
    win.blit(text2, buy_button_text1)
    text3 = f1.render('Hatiora  (4$)', 1, colours.BLACK)
    win.blit(text3, buy_button_text2)
    text4 = f1.render('Stapelia ($7)', 1, colours.BLACK)
    win.blit(text4, buy_button_text3)
    #Current money text
    text2 = f1.render('Money: ' + str(player.money), 1, colours.BLACK)
    win.blit(text2, money_text)

    pygame.display.update()