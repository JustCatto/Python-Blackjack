import Cardpile

class Hand(Cardpile.Cardpile):

    def __init__(self,handname):
        super().__init__(handname)
        self._finished = False

    def printHand(self):
        print(self._deckname+"'s Hand-")
        for card in self._deck:
            print(card.getcardNumber() + " Of " + card.getSuit(),end="\t")
        print("")

    def isFinished(self):
        return self._finished
    
    def setFinished(self,finished):
        self._finished = finished

    def getDeckScore(self):
        score = 0
        Aces = []
        for card in self._deck:
            if (card.getcardNumber() == "Ace"):
                Aces.append(card)
            else:
                score += card.getvalue()
        for ace in Aces:
            if score + 11 > 21:
                score += ace.getvalue()
            else:
                score += 11
        return score

