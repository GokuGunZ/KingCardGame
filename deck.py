import random
import pygame 


class Card(object):
    def __init__(self, suit, suitnum, value, path):
        self.suit = suit
        self.suitnum = suitnum
        self.value = value
        self.img = pygame.image.load(path)

    def show(self):
        valueScritto = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "Asso"]
        print ("{} di {}".format(valueScritto[self.value - 2], self.suit))
    


class Deck(object):
    def __init__(self):
        self.cards = []
        self.build()
    
    def build(self):
        listaval = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "jack", "queen", "king", "ace"]
        i=0
        for s in ["hearts", "spades", "diamonds","clubs" ]:
            for v in range(13):
                path = "img\cards\png\{}_of_{}.png".format(listaval[v], s)
                self.cards.append(Card(s,i%4, v+2, path))
            i+=1

    def show(self):
        for c in self.cards:
            c.show()
            

    #Aggiungere seed tempo alla funzione random
    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            rpos = random.randint(0, i)
            self.cards[i], self.cards[rpos] = self.cards[rpos], self.cards[i]

    def draw(self):
        return self.cards.pop()
