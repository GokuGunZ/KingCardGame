from game import *
from deck import *


deck = Deck()
King = Game("Pit","Dotti","Lella","Rob")



def init(deck, King):
    deck.shuffle()
    King.smazza()
    King.contaSemi()
    King.g1.ordinaMano()
    Turno= King.Primo
    return Turno