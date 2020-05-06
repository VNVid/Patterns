import cactus
import colours


cactus_type_list = [cactus.Cactus1, cactus.Cactus2, cactus.Cactus3]


class PlayersCactuses(cactus.Cactus):
    def __init__(self):
        self._children = []

    def add(self, object):
        self._children.append(object)

    def remove(self, num):
        return self._children.pop(num)

    def numOfCactuses(self):
        return len(self._children)

    def water(self, num):
        self._children[num].water()

    def feed(self, num, a):
        self._children[num].feed(a)

    def updateAll(self):
        delete = []
        for i in range(len(self._children)):
            if not self._children[i].update():
                delete.append(i)
        return delete

    def drawAll(self, location, possiblelocations, win):
        for i in range(len(self._children)):
            x = possiblelocations[location[i]][0]
            y = possiblelocations[location[i]][1]
            self._children[i].draw(win, x, y)

    def get_sum_price(self):
        sum = 0
        for i in self._children:
            sum += i.price
        return sum


class Player:
    __instance = None

    # игрок может быть только 1 -> singleton
    # для создания вызываем  Player.getInstance()
    @classmethod
    def getInstance(cls):
        if not cls.__instance:
            cls.__instance = Player()
        return cls.__instance

    money = 10
    players_cactuses = PlayersCactuses()
    dict_number_index = dict({0:-1, 1:-1, 2:-1})
    score = 0
    mincost = 2
    number_of_space = 3
    location = [0] * number_of_space #хранится номер локации для i-ого кактуса, то есть сами координаты в possible locations[location[i]]
    emptyspace = [True] * number_of_space
    possiblelocations = [(220, 350), (450, 350), (660, 350)]
    cactus_cost = [2, 4, 7]

    def findEmptySpace(self):
        for i in range(self.number_of_space):
            if self.emptyspace[i]:
                return i

    def buyCommand(self, type_number):
        #если все места заняты, то нельзя купить
        if self.players_cactuses.numOfCactuses() == self.number_of_space \
                or self.money < self.cactus_cost[type_number]:
            return
        # покупаем новый кактус
        newcactus = cactus_type_list[type_number]()
        self.players_cactuses.add(newcactus)
        self.money -= newcactus.cost
        self.score += 1
        loc = self.findEmptySpace()
        self.dict_number_index[loc] = self.players_cactuses.numOfCactuses() - 1
        self.emptyspace[loc] = False
        self.location[self.players_cactuses.numOfCactuses() - 1] = loc

    def sellCommand(self, num):
        # продаем кактус
        index = self.dict_number_index[num]
        c = self.players_cactuses.remove(index)
        self.money += c.price
        self.emptyspace[index] = True
        # удаляем его

    def waterCommand(self, num):
        index = self.dict_number_index[num]
        self.players_cactuses.water(index)

    def feedCommand(self, num, a):
        if self.money < a:
            return
        self.money -= a
        index = self.dict_number_index[num]
        self.players_cactuses.feed(index, a)

    def update(self, win):
        # обновляем все кактусы
        for i in range(len(self.emptyspace)):
            self.emptyspace[i] = True
        delete = self.players_cactuses.updateAll()
        for i in range(len(delete) - 1, -1, -1):
            c = self.players_cactuses.remove(delete[i])
            self.emptyspace[delete[i]] = True
        for i in range(self.players_cactuses.numOfCactuses()):
            self.emptyspace[i] = False
            self.location[i] = i

    def is_over(self):
        # если игрок проиграл, сообщаем об этом
        if self.players_cactuses.numOfCactuses() == 0 and self.money < self.mincost \
                or self.players_cactuses.get_sum_price() + self.money < self.mincost:
            return True  # это будем подавать в GameOver
        return False

    def draw(self, win):
        self.players_cactuses.drawAll(self.location, self.possiblelocations, win)
        #рисуем кнопки на тех местах где emptyspace = False
