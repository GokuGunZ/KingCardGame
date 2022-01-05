# KingCardGame
A python version of the Card Game King implemented with pygame

To run the game just run the 'main.py' file.

It's still under development, for now I have made only the first sub-game.


The Card game is a Regional Variation of the game in this link https://it.wikipedia.org/wiki/King_(gioco)
This game is played by 4 players and it is formed by 12 sub-games; there are some base rules, valid for almost every sub-game, but each sub-game as different scoring model and some own rules.

Every sub-game have these base rules (exeption made for the last one):
Every sub-game is played with a Deck of French cards (52 Cards, from Ace to King, and with 4 suits: Clubs, Hearths, Diamonds, Spades), every player has 13 cards in their hand, so every sub-game has 13 Tricks (exeption made for the last one wich is not a trick-based sub-game). 
The first trick is started from one randomly-chosed player, the others are started by the one who won the previous trick. The suit of the first played card in each trick is the 'Dominant suit', everyone else must play, if they have any, a card of the same suit as the dominant one. The player who plays the highest card of the Dominant suit 'take' (win) that trick (obvious consequence is that you can't win the trick if you don't have any card of the Dominant suit). For the four trump-game you can win the trick by playing the highest trump, even if the Dominant suit is not the same as the Trump suit, but in order to play a different suit from the dominant one, you mustn't have any card of that suit, in your hand.

These are the scoring model for each Subgame:

1)Normal game - Each trick taken is +1 Point.

2)Inverse game - Each trick taken is -1 Point.

3)Last 3 - The last 3 tricks taken are -4 Points each.

4)All Q - Every 'Queen' Card you take is -3 Points.

5)All J - Every 'Jack' Card you take is -3 Points.

6)K of hearths - The one who take the K of hearths gets -13 Points.

7)All the hearths - Every hearths card you take is -1 Point.

8)Player 1 Trump - Player 1 can choose a suit that will be the Trump for that sub-game and they can do it both before or after watching their hand. Every trick taken is +1 Point for the other players and +1 for the choosing-Player if they have choosen after watching their hand, or +2 if they have choosen the suit before watching their hand (blinded).

9)Player 2 Trump - Player 2 can choose a suit, every trick taken is +1 for the other player, and +1 for P2 if non-blind, +2 if blind.

10)Player 3 Trump - Player 3 can choose a suit, every trick taken is +1 for the other player, and +1 for P3 if non-blind, +2 if blind.

11)Player 4 Trump - Player 4 can choose a suit, every trick taken is +1 for the other player, and +1 for P4 if non-blind, +2 if blind.

12)Domino - This game is an atypical sub-game, in which you have to use all your card before everyone else. The sub-game's goal is to make all the four straight flush, from A 
to K, on the table, by placing one card each per turn. The firsts cards you can play if there aren't any on the table are only the '7's; if there are card on the table, you can only continue the straights by adding a card (according to the suit) +1 or -1 from the one already on the table (ex. if on the table there is only the 7 of Clubs, the only cards you can play are 6 of Clubs, 8 of Clubs, or any other 7, if you don't have any of those card, you pass your turn without play any card. 
When someone dosn't have anymore cards in their hand, the sub-game is over and they're the winner of this sub-game. The winner gain 1 point for each card in the other player's hand, and everyone gets -1 Point for each card in their hand.

At the end of every sub-game, the one with more points win.
