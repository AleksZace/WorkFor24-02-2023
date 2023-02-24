import random

class Thing:
    def __init__(self,guess,bet):
        self.__guess = guess
        self.__value = random.randint(1,30)
        self.__bet = bet
    def getGuess(self):
        return self.__guess
    def getValue(self):
        return self.__value
    def getBet(self):
        return self.__bet 
    def getScore(self):
        guess1 = self.getGuess()
        value1 = self.getValue()
        if guess1 == value1:
            y = 2*self.getBet()
            if guess1%2 == 0:
                y*=2
            if guess1%10 == 0:
                y*=3
            if guess1<5:
                y*=2
        else:
            y = 0
        return y
thingy = Thing(1,200)
print(thingy.getScore())