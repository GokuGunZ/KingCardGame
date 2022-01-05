
#raccoglie le giocate dei giocatori (g1 seleziona, altri casuali)
# #altreGiocate
# def raccoltaGiocate(primaGiocata):
#     semeComandante = primaGiocata.suitnum
#     King.contaSemi()
#     for giocatore in [1,2,3]:
#         tocca=(giocatore+King.Primo)%4
#         if tocca==0:    
#             carteGiocate[giocata].append(King.g1.Mano[position[0]])
#             continue
#         position[tocca]=random.randint(0,len(King.allg[tocca].Mano)-1)
#         cartaGiocata=King.allg[tocca].Mano[position[tocca]]
#         while (cartaGiocata.suitnum != semeComandante) & (King.allg[tocca].Semi[semeComandante] != 0):
#             position[tocca]=random.randint(0,len(King.allg[tocca].Mano)-1)
#             cartaGiocata=King.allg[tocca].Mano[position[tocca]]
#         King.allg[tocca].Mano.pop(position[tocca])
#         carteGiocate[giocata].append(cartaGiocata)
 