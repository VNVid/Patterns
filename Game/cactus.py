import pygame
pygame.init()

class Cactus:
    minWater = 0
    curWater = 0
    sun = False
    strength = 0
    growingLevel = 0
    isFlowering = False
    price = 0

    def water(self):
        self.curWater += 3
    def feed(self, a):
        self.strength += a


class Cactus1(Cactus):
    def __init__(self):
        minWater = 2
        curWater = 12
        sun = False
        price = 0

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
            image = pygame.image.load('images/cactus.jpeg')
        else:
            image = pygame.image.load('images/cactus.png')
        win.blit(image, (x, y))


class Cactus2(Cactus):
    def __init__(self):
        minWater = 10
        curWater = 20
        sun = False
        price = 2

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
        win.blit(image, (x, y))

class Cactus3(Cactus):
    def __init__(self):
        minWater = 6
        curWater = 20
        sun = True
        price = 2

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
        win.blit(image, (x, y))