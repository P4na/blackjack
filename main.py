
# The Card Class definition
# Function to print the cards
from random import random


def print_cards(carte, hidden):
         
    s = ""
    for carta in carte:
        s = s + "\t ________________"
    if hidden:
        s += "\t ________________"
    print(s)
 
 
    s = ""
    for carta in carte:
        s = s + "\t|                |"
    if hidden:
        s += "\t|                |"    
    print(s)
 
    s = ""
    for carta in carte:
        if carta.value == '10':
            s = s + "\t|  {}            |".format(carta.value)
        else:
            s = s + "\t|  {}             |".format(carta.value)  
    if hidden:
        s += "\t|                |"    
    print(s)
 
    s = ""
    for carta in carte:
        s = s + "\t|                |"
    if hidden:
        s += "\t|      * *       |"
    print(s)    
 
    s = ""
    for carta in carte:
        s = s + "\t|                |"
    if hidden:
        s += "\t|    *     *     |"
    print(s)    
 
    s = ""
    for carta in carte:
        s = s + "\t|                |"
    if hidden:
        s += "\t|   *       *    |"
    print(s)    
 
    s = ""
    for carta in carte:
        s = s + "\t|                |"
    if hidden:
        s += "\t|   *       *    |"
    print(s)    
 
    s = ""
    for carta in carte:
        s = s + "\t|       {}        |".format(carta.seme)
    if hidden:
        s += "\t|          *     |"
    print(s)    
 
    s = ""
    for carta in carte:
        s = s + "\t|                |"
    if hidden:
        s += "\t|         *      |"
    print(s)    
 
    s = ""
    for carta in carte:
        s = s + "\t|                |"
    if hidden:
        s += "\t|        *       |"
    print(s)
 
    s = ""
    for carta in carte:
        s = s + "\t|                |"
    if hidden:
        s += "\t|                |"
    print(s)
 
    s = ""
    for carta in carte:
        s = s + "\t|                |"
    if hidden:
        s += "\t|                |"
    print(s)    
 
    s = ""
    for carta in carte:
        if carta.value == '10':
            s = s + "\t|            {}  |".format(carta.valore)
        else:
            s = s + "\t|            {}   |".format(carta.valore)
    if hidden:
        s += "\t|        *       |"        
    print(s)    
         
    s = ""
    for card in carte:
        s = s + "\t|________________|"
    if hidden:
        s += "\t|________________|"
    print(s)        
 
    print()

class Carta:
    def __init__(self, seme, valore, valore_carta):
        # Seme della carta
        self.seme = seme
 
        # The suit value 
        suits_values = {"Spades":"\u2664", "Hearts":"\u2661", "Clubs": "\u2667", "Diamonds": "\u2662"}
 
        
        # rappresentazione valore tipo asso = 1, re = 10
        self.valore = valore
 
        # punteggio valore carta
        self.valore_carta = valore_carta
        
        semi = ["spade","cuori","fiori","picche"]
        
        carte = ["A","1","2","3","4","5","6","7","8","9","10","J","Q","K"]
        #A di base 11, se punteggio con A supera 21 A=1
        valore_carte = {"A":11, "2":2, "3":3, "4":4, 5:"5", "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}
        
        mazzo = []
        
        #per selezionare seme
        for seme in semi:
            #per selezionare numero
            for carta in carte:
                mazzo.append(Carta(suits_values[seme], carta, valore_carta[carta]))
                
        def blackjack_game(deck):

            global valore_carte

            #carte sia per mazziere che giocatore
            carte_giocatore = []
            carte_mazziere = []

            #punteggio sia per mazziere che giocatore
            punteggio_giocatore = 0
            punteggio_mazziere = 0

            while len(carte_giocatore) < 2:
                
                # prendere carta randomicamente
                carta_giocatore = random.choice(mazzo)
                carte_giocatore.append(carta_giocatore)
                mazzo.remove(carta_giocatore)
                
                #aggiorna punteggio giocatore
                punteggio_giocatore += punteggio_giocatore.valore_carta #non so se va
                
                #nel caso entrambe le  carte siano A, rendi un A = 1
                if len(carte_giocatore) == 2:
                    if carte_giocatore[0]-valore_carta == 11 and carte_giocatore[1] == 11:
                        carte_giocatore[0] == 1
                        punteggio_giocatore -= 10
                        
                #stampa punteggio e carte
                print("PUNTEGGIO  GIOCATORE: ")
                print_cards(carte_giocatore, False)
                print("PUNTEGGIO GIOCATORE =  ", punteggio_giocatore)
                
                input()
                
                #carta a mazziere randomica
                carta_mazziere = random.choice(mazzo)
                carte_mazziere.append(carta_mazziere)
                mazzo.remove(carta_mazziere)
                
                #aggiorna punteggio mazziere
                punteggio_mazziere += carta_mazziere.valore_carta

                #stampa carte e punteggio mazziere, mantieni la seconda carta nascosta insieme al punteggio
                if len(carte_mazziere) == 1:
                    print_cards(carte_mazziere, False)
                    print("PUNTEGGIO MAZZIERE= ", punteggio_mazziere - carte_mazziere[-1].valore_carta)
                    
                # nel caso entrambe le carte sono Assi, rendi secondo asso di valore 1
                if len(carte_mazziere) == 2:
                    if carte_mazziere[0].valore_carta == 11 and carte_mazziere[1].valore_carta == 11:
                        carte_mazziere[1].valore_carta = 1
                        punteggio_giocatore -= 10
                
                input()
                
            if punteggio_giocatore == 21:
                print("IL GIOCATORE HA FATTO BLACKJACK!\nIL GIOCATORE HA VINTO!")
                quit()
                
            #clear()
            
            #SECONDA FASE
            
            #stampa carte mazziere e giocatore
            print("CARTE MAZZIERE: ")
            print_cards(carte_mazziere[:-1], True)
            print("PUNTEGGIO MAZZIERE: ", punteggio_mazziere - carte_mazziere[-1].valore_carta)
            
            print()
            
            print("CARTE GIOCATORE: ")
            print_cards(carte_giocatore, False)
            print("PUNTEGGIO GIOCATORE: ", punteggio_giocatore)
            
            #Se giocatore vuole restare            
            
            


