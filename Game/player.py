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
    numOfCactuses = 0

    # еще храним кактусы

    def buy(self, cost):
        #покупаем новый кактус
        self.money -= cost
        print("")

    def sell(self, c):
        # продаем кактус
        # передаем кактус
        self.money += c.price
        # удаляем его
        print("")

    def update(self):
        # обновляем все кактусы
        # если игрок проиграл, сообщаем об этом
        print("")
