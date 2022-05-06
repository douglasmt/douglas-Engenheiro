from deck import Deck
from card import Card
import unittest

class CardTests(unittest.TestCase):
    def setUp(self):
        self.card = Card("Hearts", "A")

    def test_init(self):
        """cards should have a suit and a value"""
        self.assertEqual(self.card.suit, "Hearts")
        self.assertEqual(self.card.value, "A")

    def test_repr(self):
        """repr should return a string of the form 'VALUE OF SUIT'"""
        self.assertEqual(repr(self.card), "A of Hearts")
        
class DeckTests(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()
    
    def test_init(self):
        """cards should have a cards attribute, which is a list"""
        self.assertEqual(isinstance(self.deck.cards), list)
        self.assertEqual(len(self.deck.cards), 52)
    

    def test_repr(self):
        """repr should return a string the form 'Deck of ... cards' """
        self.assertEqual(repr(self.deck), "Deck of 52 cards")

    def test_count(self):
        """count should return a count of number of cards ..."""
        self.assertEqual(self.deck.count(),52)
        self.deck.cards.pop()
        self.assertEqual(self.deck.count(),51)

    def test_deal_sufficient_cards(self): # save 10 cards, check if they are 10
        """_deal should deal the number of cards specified, ..."""
        cards = self.deck._deal(10) # (num: Any) -> list
        self.assertEqual(len(cards), 10) # (first: Any, second: Any, msg: Any = ...)
        self.assertEqual(self.deck.count(), 42)

    def test_deal_insuficcient_cards(self):
        """_deal should deal the number of cards left in the table"""
        cards = self.deck._deal(100)
        self.assertEqual(len(cards), 52)
        self.assertEqual(self.deck.count(), 0)

    def test_deal_no_cards(self):
        """_deal should throw a ValueError if the deck is empty """
        self.deck._deal(self.deck.count())
        with self.assertRaises(ValueError):
            self.deck._deal(1)

    def test_deal_card(self):
        """_eal_card should deal a singl card from the deck"""
        card = self.deck.deal_card[-1] # takes the last card of the deck
        dealt_card = self.deck.deal_card()
        self.assertEqual(card, dealt_card) # compare if the last is equal the chosen one
        self.assertEqual(self.deck.count(), 51)

    def test_shuffle_full_deck(self):
        """shuffle should shuffle the deck if the deck is full"""
        cards = self.deck.deal_hand[:] # takes all cards of the deck
        self.deck.shuffle() # shuffle cards of the deck
        self.assertNotEqual(cards, self.deck.cards) # compares the shuffled cards with the original?
        self.assertEqual(self.deck.count(), 52) # confirming it's full

    def test_shuffle_not_full_deck(self):
        """shuffle should throw an ValueError of the deck"""
        self.deck._deal(1)                  # takes one card
        with self.assertRaises(ValueError): 
            self.deck.shuffle()             # shuffle cards of the deck


    if __name__ == "__main__":
        unittest.main()