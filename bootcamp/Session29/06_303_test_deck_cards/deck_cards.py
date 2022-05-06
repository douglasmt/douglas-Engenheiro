from itertools import count
from random import shuffle
#from re import S


class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return "{} of {}".format(self.value, self.suit)

class Deck:
    def __init__(self) -> None:
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        
        # Each instance of Deck  should have a cards attribute with 
        # all 52 possible instances of Card .
        self.cards = [Card(suit, value) for suit in suits for value in values]
        '''
        for suit in suits:
            for value in values:
                Card(suit, value) 
        '''

    def __repr__(self):
        return "Deck of {} cards".format(self.count())


    def count(self):
        return len(self.cards)

    def _deal(self, num):        
        count = self.count()
        actual = min([count, num]) # takes the least between (count, num)
        if count == 0: # if the cards are over, it raises ValueError:
            # print("\n END OF THE GAME!")
            raise ValueError("All cards have been dealt")
        
        cards = self.cards[-actual:] 
        # returns from "actual value"
        # print(f"\nCards variable in _deal: {cards}")
        print("\nCards variable in _deal: {}".format(cards))
        self.cards = self.cards[:-actual] # returns from first to "actual" value

        return cards

    def deal_card(self):
        # Deck  should have an instance method called deal_card  
        # which uses the _deal  method to deal a single card from the deck.        
        return self._deal(1)[0]
    
    def deal_hand(self,num):
        # Deck  should have an instance method called deal_hand  
        # which accepts a number and uses the _deal  method to deal 
        # a list of cards from the deck.
        return self._deal(num)

    def shuffle(self):
        if self.count() > 52:
            raise ValueError("Only full decks can be shuffled")
        shuffle(self.cards)
        return self

d = Deck()      # create a set with a deck of cards
d.shuffle()     # shuffle the order of the cards
print("\ncards available: \n {} ".format(d._deal))
card = d.deal_card()    # play with a card
print(f"\nPlaying the card: {card} ")

hand = d.deal_hand(50)    # return a list of cards
print(f"\nPlaying the hand(50): {hand} ")

card2 = d.deal_card()    # return a list of cards
print(f"\nPlaying the card 2: {card2} ")

#print(f"\nCards : {d.cards} and quantity: {d.count()} ")

card2 = d.deal_card()    # return a list of cards
print("\ncards available: \n {} ".format(d._deal))
print(f"\nPlaying the card 2: {card2} ")
