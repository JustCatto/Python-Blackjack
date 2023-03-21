import Deck
import Hand


class Blackjack():
    
    def __init__(self):
        self._playerList = []

    def game(self,playerNum):
        self._startGame(playerNum)
        gameend = False
        while gameend == False:
            gameend = True
            for player in self._playerList:
                if player.isFinished() == False:
                    print("It is player-",player.getDeckName(),"'s Turn.")
                    print("Deck value-",player.getDeckScore())
                    player.printHand()
                    if (self._getDrawDecision() == True):
                        player.addCard(self._deck.drawCard())
                        gameend = False
                    else:
                        player.setFinished(True)
        self._printWinners(self._getWinners())

    def _printWinners(self,winners):
        if len(winners) == 0:
            print("No one won!")
        elif len(winners) == 1:
            print(winners[0].getDeckName())
        else:
            for winner in winners:
                print(winner.getDeckName()+",",end=" ")
            print("All won!")

    def _getWinners(self):
        winners = []
        min = 99
        for currentPlayer in self._playerList:
            if currentPlayer.getDeckScore() <= 21:
                diff = 21-currentPlayer.getDeckScore()
                if min > diff:
                    min = diff
                    winners = []
                    winners.append(currentPlayer)
                elif min == diff:
                    winners.append(currentPlayer)
        return winners


    def _getDrawDecision(self):
        valid = False
        while valid == False:
            decision = input("Please input if you will draw or stick. [D/S]\n-->").lower()
            if decision == "d":
                return True
            elif decision == "s":
                return False
            else:
                print("Please enter either D or S.\n")

    def _startGame(self,playerNum):
        self._initPlayers(playerNum)
        self._initDeck()
        self._drawStartingCards()

    def _drawStartingCards(self):
        for player in self._playerList:
            player.addCard(self._deck.drawCard())

    def _initPlayers(self,playerNum):
        for playerNum in range(playerNum):
            self._playerList.append(Hand.Hand("P"+str(playerNum)))

    def _initDeck(self):
        self._deck = Deck.Deck("Deck")
        self._deck.generateDeck()
        self._deck.shuffleDeck()
