import Cardpile
import Constants
import random
import Card

class Deck(Cardpile.Cardpile):

    def __init__(self,deckname):
        super().__init__(deckname)

    def generateDeck(self):
        for suit in Constants.SUITS:
            for i in range(len(Constants.CARDNUMBERS)):
                card = Card.Card(suit,Constants.CARDNUMBERS[i],Constants.CARDVALUES[i])
                self._deck.append(card)

    def shuffleDeck(self):
        random.shuffle(self._deck)