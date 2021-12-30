import unittest
from models.card import Card
from models.card_game import *

class TestCardGame(unittest.TestCase):
    def setUp(self):
        # card1 = Card('heart', 7)
        # card2 = Card('diamond', 1)

        self.card = Card('clubs', 5)
        self.cardgame = CardGame()

    def test_can_check_ace_True(self):
        card = Card("spades", 1)
        self.assertEqual(True, self.cardgame.check_for_ace(card))

    def test_can_check_ace_False(self):
        card = Card("Hearts", 5)
        self.assertEqual(False, self.cardgame.check_for_ace(card))



    
        
   