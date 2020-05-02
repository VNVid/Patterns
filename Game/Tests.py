import unittest
import pygame
import Game, window, cactus, player, colours


class Test(unittest.TestCase):
    def setUp(self):
        self.player = player.Player()

    def tearDown(self):
        pygame.quit()

    def test_buy_cactus0(self):
        self.player.buyCommand(0)
        self.assertTrue(self.player.money == 8)

    def test_buy_cactus1(self):
        self.player.buyCommand(1)
        self.assertTrue(self.player.money == 6)

    def test_buy_cactus2(self):
        self.player.buyCommand(1)
        self.assertTrue(self.player.money == 6)

    def test_money_check(self):
        self.player.buyCommand(2)
        self.player.buyCommand(2)
        self.player.buyCommand(2)
        self.assertTrue(self.player.money >= 0)

    def test_add(self):
        self.PlayersCactuses = player.PlayersCactuses()
        newcactus = cactus.Cactus1()
        self.PlayersCactuses.add(newcactus)
        self.assertTrue(self.PlayersCactuses.numOfCactuses() == 1)

    def test_sum_price(self):
        self.PlayersCactuses = player.PlayersCactuses()
        newcactus1 = cactus.Cactus1()
        newcactus2 = cactus.Cactus2()
        self.PlayersCactuses.add(newcactus1)
        self.PlayersCactuses.add(newcactus2)
        self.assertTrue(self.PlayersCactuses.get_sum_price() == 2)

    def test_add(self):
        self.PlayersCactuses = player.PlayersCactuses()
        newcactus = cactus.Cactus1()
        self.PlayersCactuses.add(newcactus)
        self.assertTrue(self.PlayersCactuses.numOfCactuses() == 1)


if __name__ == '__main__':
    unittest.main()