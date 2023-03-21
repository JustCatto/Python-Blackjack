
class Card:

    def __init__(self,suit,cardnumber,value):
        self._suit = suit
        self._cardNumber = cardnumber
        self._value = value

    def getSuit(self):
        return self._suit

    def getcardNumber(self):
        return self._cardNumber
    
    def getvalue(self):
        return self._value
    
    