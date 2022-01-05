import pygame
from pygame.locals import * 
from pygame.event import wait
from deck import *
from game import *
from init import *


deck = Deck()
King = Game("Pit","Dotti","Lella","Rob")
giocata=0
position=[0,0,0,0]
carteGiocate=[[],[],[],[],[],[],[],[],[],[],[],[],[]]
timerScomparsa=0
timerGiocata=0
primaCarta = None


Turno = init(deck, King)

#Inizializzare pygame
pygame.init()
clock = pygame.time.Clock()


#Mostra lo schermo
screen = pygame.display.set_mode((800,600))
#Impostazioni del gioco 
pygame.display.set_caption("King") 
icon = pygame.image.load("img\icon.png")
pygame.display.set_icon(icon)
font = pygame.font.SysFont("monospace", 16)


#funzione per mostrare la mano a video
def mostraMano(self,ypos,sel):
    xpos=400-len(self.Mano)*50/2
    for carta in range(len(self.Mano)):
        thisy=ypos
        if carta == sel :
            thisy-=35
        screen.blit(self.Mano[carta].img, (xpos,thisy))
        xpos+=50


def primaGiocata(Turno,giocata):
    if King.Primo == 0 :
        primaCarta=King.g1.Mano[position[0]]
        Turno=(Turno+1)%4
        return primaCarta, Turno
    position[King.Primo]=random.randint(0,len(King.allg[King.Primo].Mano)-1)
    primaCarta=King.allg[King.Primo].Mano[position[King.Primo]]
    carteGiocate[giocata].append(primaCarta)
    King.allg[Turno].Mano.pop(position[Turno])
    Turno=(Turno+1)%4
    return primaCarta, Turno, giocata
    

def altraGiocata(Turno, primaCarta, position):
    position[Turno]=random.randint(0,len(King.allg[Turno].Mano)-1)
    cartaGiocata=King.allg[Turno].Mano[position[Turno]]
    while King.checkSuit(position, primaCarta, Turno):
        position[Turno]=random.randint(0,len(King.allg[Turno].Mano)-1)
        cartaGiocata=King.allg[Turno].Mano[position[Turno]]
    carteGiocate[giocata].append(cartaGiocata)
    King.allg[Turno].Mano.pop(position[Turno])
    Turno=(Turno+1)%4
    return Turno


def checkVincitore(primaCarta, giocata, carteGiocate, Primo):
    cartaVincente = primaCarta
    newPrimo = Primo
    for i in [1,2,3]:
        if (cartaVincente.suit == carteGiocate[giocata][i].suit) & (cartaVincente.value < carteGiocate[giocata][i].value):
            cartaVincente = carteGiocate[giocata][i]
            newPrimo = (i + Primo) % 4 
    print("La mano è stata vinta da {} con la carta ".format(King.allg[newPrimo].Nome), end="") 
    cartaVincente.show()
    return newPrimo


def mostraGiocata(giocata):
    cordcarte=[(375,310),(425,230),(375,150),(325,230)]
    for i in range(len(carteGiocate[giocata])):
        screen.blit(carteGiocate[giocata][i].img, cordcarte[(King.Primo+i)%4])
          

def stampaUHD():
    pos=[(350,540),(600,300),(350,40),(100,300)]
    pos2=[(350,556),(600,316),(350,56),(100,316)]
    for i in range(4):
        label = font.render('{}'.format(King.allg[i].Nome), 1, (0,0,0), (160,160,160))
        label2 = font.render('Punti: {}'.format(King.allg[i].Punti), 1, (0,0,0), (160,160,160))
        screen.blit(label, pos[i])
        screen.blit(label2, pos2[i])


#Loop del gioco
running = True
while running:
    screen.fill((0,255,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        #Muoversi tra le carte
        if (event.type == pygame.KEYDOWN) & (len(carteGiocate[giocata]) < 4):
            if (event.key == pygame.K_LEFT) :
                if position[0] > 0:
                    position[0]-=1
                else:
                    position[0]=len(King.g1.Mano)-1
            elif (event.key == pygame.K_RIGHT) :
                if (position[0]<len(King.g1.Mano)-1) :
                    position[0]+=1
                else :
                    position[0]= 0


            elif (event.key == pygame.K_RETURN):
                if (Turno == 0):
                    if (King.Primo == 0):
                        primaCarta, Turno = primaGiocata(Turno, giocata)
                        carteGiocate[giocata].append(King.g1.Mano[position[0]])
                        King.g1.Mano.pop(position[0])
                        position[0]=0
                    else:
                        if King.checkSuit(position, primaCarta, 0):
                            print("Devi rispondere a seme")
                            continue
                        carteGiocate[giocata].append(King.g1.Mano[position[0]])
                        King.g1.Mano.pop(position[0])
                        position[0]=0
                        Turno += 1
                else :
                    print('Non è il tuo turno')
            elif (event.key == pygame.K_ESCAPE):
                pygame.quit()
                quit()


            #Premo un pulsante per far giocare quello dopo
            #Primo
            elif (event.key == pygame.K_p and len(carteGiocate[giocata]) == 0):
                if (Turno == 0 ):
                    print('è il tuo turno')
                    continue
                primaCarta, Turno, giocata = primaGiocata(Turno, giocata)
            #Altri
            elif (event.key == pygame.K_n):
                if (Turno == 0):
                    print('è il tuo turno')
                    continue
                if (primaCarta == None):
                    print('deve giocare il primo di mano')
                    continue
                Turno = altraGiocata(Turno, primaCarta, position)

            #Premere S per stampare cose
            elif (event.key == pygame.K_s):
                print(carteGiocate)
                print(giocata)

            #Premere T per stampare carta selezionata
            elif (event.key == pygame.K_t):
                King.allg[0].Mano[position[0]].show()


    #Andamento del gioco 
    if (Turno != 0):
        if timerGiocata>10:
            if (len(carteGiocate[giocata]) == 0):
                primaCarta, Turno, giocata = primaGiocata(Turno, giocata)
            elif (len(carteGiocate[giocata]) < 4):
                Turno = altraGiocata(Turno, primaCarta, position)
            timerGiocata = 0
        timerGiocata += 1

    #Check di fine turno
    if (len(carteGiocate[giocata])>3):
        if timerScomparsa>16 :
            King.Primo=checkVincitore(primaCarta,giocata, carteGiocate,King.Primo)
            King.allg[King.Primo].Punti+=1
            giocata+=1
            Turno=King.Primo
            timerScomparsa=0
            primaCarta=None
            King.contaSemi()
            King.punteggio()
        timerScomparsa+=1

    if (giocata == 13):  
        Turno = init(deck, King) 
        giocata=0
        position=[0,0,0,0]
        carteGiocate=[[],[],[],[],[],[],[],[],[],[],[],[],[]]
        timerScomparsa=0
        primaCarta = None
    
            
        

    mostraMano(King.g1,450,position[0])
    stampaUHD()

    # mostraMano(King.g2,50,position[0])
    # mostraMano(King.g3,100,position[0])
    # mostraMano(King.g4,150,position[0])

    mostraGiocata(giocata)
    pygame.display.update()
    clock.tick(10)