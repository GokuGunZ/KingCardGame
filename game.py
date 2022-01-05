from deck import *
import random

LengthCard=50


class Game(object):
    def __init__(self, nome1, nome2, nome3, nome4):
        self.g1 = Player(nome1)
        self.g2 = Player(nome2)
        self.g3 = Player(nome3)
        self.g4 = Player(nome4)
        self.allg = (self.g1, self.g2, self.g3, self.g4)
        self.classifica = [self.g1, self.g2, self.g3, self.g4]
        self.Primo = random.randint(0, 3)
    
    def smazza(self):
        deck = Deck()
        deck.shuffle()
        lenghdek=52;
        for i in range(lenghdek):
            self.allg[i%4].Mano.append(deck.draw())

    def MostraMani(self):
        for giocatori in range(len(self.allg)):
            print("La mano di {} è :".format(self.allg[giocatori].Nome))
            for carte in range(len(self.allg[giocatori].Mano)):
                self.allg[giocatori].Mano[carte].show()
    
    def contaSemi(self):
        for i in range(4):
            self.allg[i].contaSeme()

    def punteggio(self):
        self.classifica.sort(key= lambda x: x.Punti, reverse=True)
        print("La classifica dei punti è")
        for giocatori in range(len(self.allg)):
            print("{} ha {} punti.".format(self.classifica[giocatori].Nome, self.classifica[giocatori].Punti))
    
    def stampaSemi(self):
        for i in range(4):
            print(self.allg[i].Semi)

    def checkSuit(self, position, primaCarta, ngioc):
        return (self.allg[ngioc].Mano[position[ngioc]].suitnum != primaCarta.suitnum) & (self.allg[ngioc].Semi[primaCarta.suitnum] != 0)


class Player(object):
    def __init__(self, name):
        self.Nome = name
        self.Mano = []
        self.Punti = 0
        self.Semi = [0,0,0,0]
    
    def ordinaMano(self):
        self.Mano.sort(key=lambda x: (x.suitnum, x.value))

    def contaSeme(self):
        self.Semi=[0,0,0,0]
        for carta in range(len(self.Mano)):
            self.Semi[self.Mano[carta].suitnum]+=1