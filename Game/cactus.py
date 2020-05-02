import colours
from abc import abstractmethod
import pygame
pygame.init()


button_width = 60
button_height = 30
space_len = 10
delta_x = 5
delta_y = 10
delta_x_for_sell = 70
delta_y_for_sell = 20
image_height = 350
price_y = 100
water_y = 50

def drawButtons(win, x, y):
    f1 = pygame.font.Font(None, 18)

    water_button = pygame.draw.rect(win, colours.AQUA, (x, y, button_width, button_height));
    text1 = f1.render('WATER', 1, colours.BLACK)
    win.blit(text1, (x + delta_x, y + delta_y))

    feed1_button = pygame.draw.rect(win, colours.SALMON1,
                                    (x + button_width + space_len, y,
                                     button_width, button_height));
    text2 = f1.render('FEED 2', 1, colours.BLACK)
    win.blit(text2, (x+button_width+space_len + delta_x, y + delta_y))

    feed2_button = pygame.draw.rect(win, colours.SALMON1,
                                    (x + (button_width + space_len)*2, y,
                                     button_width, button_height));
    text3 = f1.render('FEED 4', 1, colours.BLACK)
    win.blit(text3, (x + (button_width + space_len)*2 + delta_x, y + delta_y))

    sell_button = pygame.draw.rect(win, colours.SALMON1,
                                    (x + delta_x_for_sell, y + button_height + delta_y_for_sell,
                                     button_width, button_height));
    text4 = f1.render('SELL', 1, colours.BLACK)
    win.blit(text4, (x + delta_x_for_sell + delta_x, y + button_height + delta_y_for_sell + delta_y))

def print_price_water(win, x, y, price, water):
    f1 = pygame.font.Font(None, 30)
    text1 = f1.render('Price: ' + str(price), 1, colours.BLACK)
    win.blit(text1, (x, y - price_y))

    text2 = f1.render('Water: ' + str(water), 1, colours.BLACK)
    win.blit(text2, (x, y - water_y))


class Cactus:
    def __init__(self):
        self.minWater = 0
        self.curWater = 0
        self.sun = False
        self.strength = 0
        self.growingLevel = 0
        self.isFlowering = False
        self.price = 0
        self.cost = 0

    def water(self):
        self.curWater += 3

    def feed(self, a):
        self.strength += a

    @abstractmethod
    def update(self):
        pass

    @abstractmethod
    def draw(self, win, x, y):
        pass


class Cactus1(Cactus):
    def __init__(self):
        super().__init__()
        self.minWater = 2
        self.curWater = 12
        self.sun = False
        self.price = 0
        self.cost = 2

    def update(self):
        self.growingLevel += 1 + self.strength // 5
        if self.growingLevel == 10:
            self.isFlowering = True
        if self.growingLevel % 2 == 0:
            self.price += 2
        if self.isFlowering:
            self.price += 4
        self.strength %= 5
        self.curWater -= 1
        if self.curWater < self.minWater:
            return False # кактус завял
        else:
            return True # кактус пока жив

    def draw(self, win, x, y):
        if self.isFlowering:
            image = pygame.image.load('images/cactus_PNG23634.png')
        else:
            image = pygame.image.load('images/cactus_PNG23622.png')
        image.set_colorkey(colours.WHITE)
        win.blit(image, (x, y))
        drawButtons(win, x, y + image_height)
        print_price_water(win, x, y, self.price, self.curWater)


class Cactus2(Cactus):
    def __init__(self):
        super().__init__()
        self.minWater = 10
        self.curWater = 20
        self.sun = False
        self.price = 2
        self.cost = 4

    def update(self):
        self.growingLevel += 3 + self.strength // 5
        if self.growingLevel == 10:
            self.isFlowering = True
        if self.growingLevel % 2 == 0:
            self.price += 3
        if self.isFlowering:
            self.price += 5
        self.strength %= 5
        self.curWater -= 4
        if self.curWater < self.minWater:
            return False  # кактус завял
        else:
            return True  # кактус пока жив

    def draw(self, win, x, y):
        if self.isFlowering:
            image = pygame.image.load('images/cactus_PNG23610.png')
        else:
            image = pygame.image.load('images/cactus_PNG23625.png')
        image.set_colorkey(colours.WHITE)
        win.blit(image, (x, y))
        drawButtons(win, x, y + image_height)
        print_price_water(win, x, y, self.price, self.curWater)

class Cactus3(Cactus):
    def __init__(self):
        super().__init__()
        self.minWater = 6
        self.curWater = 20
        self.sun = True
        self.price = 2
        self.cost = 7

    def update(self):
        self.growingLevel += 2 + self.strength // 10
        if self.growingLevel == 30:
            self.isFlowering = True
        if self.growingLevel % 2 == 0:
            self.price += 2
        if self.isFlowering:
            self.price += 10
        self.strength %= 10
        self.curWater -= 3
        if self.curWater < self.minWater:
            return False  # кактус завял
        else:
            return True  # кактус пока жив

    def draw(self, win, x, y):
        if self.isFlowering:
            image = pygame.image.load('images/cactus_PNG23609.png')
        else:
            image = pygame.image.load('images/cactus_PNG23611.png')
        image.set_colorkey(colours.WHITE)
        win.blit(image, (x, y))
        drawButtons(win, x, y + image_height)
        print_price_water(win, x, y, self.price, self.curWater)