class Cardpile:

    def __init__(self,deckname):
        self._deckname = deckname
        self._deck = []

    def getDeckName(self):
        return self._deckname
    
    def setDeckName(self,deckname):
        self._deckname = deckname

    def addCard(self,card):
        self._deck.append(card)
    
    def drawCard(self):
        return self._deck.pop(0)


