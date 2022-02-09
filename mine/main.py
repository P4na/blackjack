import random
import os


#definizione dell'oggetto carta
class Carta:
    def __init__(self, seme, valore, valore_carta):
        # Seme della carta
        self.seme = seme

        # rappresentazione valore tipo asso = 1, re = 10
        self.valore = valore

        # punteggio valore carta
        self.valore_carta = valore_carta


# pulisce il terminale
def clear():
    os.system("clear")


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
        if carta.valore == '10':
            s = s + "\t|  {}            |".format(carta.valore)
        else:
            s = s + "\t|  {}             |".format(carta.valore)
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
        if carta.valore == '10':
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

        
                
def blackjack_game(deck):
    #carte sia per mazziere che giocatore
    carte_giocatore = []
    carte_mazziere = []

    #punteggio sia per mazziere che giocatore
    punteggio_giocatore = 0
    punteggio_mazziere = 0
    
    clear()

    while len(carte_giocatore) < 2:
        
        # prendere carta randomicamente
        carta_giocatore = random.choice(mazzo)
        carte_giocatore.append(carta_giocatore)
        mazzo.remove(carta_giocatore)
        
        #aggiorna punteggio giocatore
        punteggio_giocatore += carta_giocatore.valore_carta #non so se va
        
        #nel caso entrambe le  carte siano A, rendi un A = 1
        if len(carte_giocatore) == 2:
            if carte_giocatore[0].valore_carta == 11 and carte_giocatore[1] == 11:
                carte_giocatore[0].valore_carta = 1
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
        print("CARTE MAZZIERE: ")
        if len(carte_mazziere) == 1:
            print_cards(carte_mazziere, False)
            print("PUNTEGGIO MAZZIERE = ", punteggio_mazziere)
        else:
            print_cards(carte_mazziere[:-1], True)
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
                
        clear()
            
    #SECONDA FASE
    
    #stampa carte mazziere e giocatore
    print("CARTE MAZZIERE: ")
    print_cards(carte_mazziere[:-1], True)
    print("PUNTEGGIO MAZZIERE: ", punteggio_mazziere - carte_mazziere[-1].valore_carta)
    
    print()
    
    print("CARTE GIOCATORE: ")
    print_cards(carte_giocatore, False)
    print("PUNTEGGIO GIOCATORE: ", punteggio_giocatore)
    
    # decidere mosse giocatore
    while punteggio_giocatore < 21:
        choice = input("Scrivi C per una nuova carta o S per stare :")
        
        if len(choice) != 1 or (choice.upper() != "H" and choice.upper() != "S"):
            clear()
            print("Sbagliato, riprova!")
    
        #se giocatore vuole nuova carta
        if choice.upper() == "H":
            
            #dai nuova carta
            carta_giocatore = random.choice(mazzo)
            carte_giocatore.append(carta_giocatore)
            deck.remove(carta_giocatore)
            
            #aggiorna punteggio giocatore
            punteggio_giocatore += carta_giocatore.valore_carta
            
            # se il giocatore prene un asso 
            c = 0
            while punteggio_giocatore > 21 and c < len(carte_giocatore):
                if carte_giocatore[c].valore_carta == 11:
                    carte_giocatore[c].valore_carta = 1
                    punteggio_giocatore -= 10
                    c +=1
                else:
                    c += 1
            clear()
            
            print("CARTE MAZZIERE: ")
            print_cards(carte_mazziere[:-1], True)
            print("PUNTEGGIO MAZZIERE: ", punteggio_mazziere - carte_mazziere[-1].valore_carta)
            
            print()
                
            print("CARTE GIOCATORE: ")
            print_cards(carte_giocatore, False)
            print("Punteggio giocatore = ", punteggio_giocatore)
            
        # se il giocatore decide di restare
        if choice.upper() == "S":
            break
    
    clear()
    
    # mostra carta nascosta mazziere
    print("CARTE GIOCATORE: ")
    print_cards(carte_giocatore, False)
    print("Punteggio giocatore = ", punteggio_giocatore)
    
    print()
    print("il mazziere mostra la carta nascosta...")
    
    print("CARTE MAZZIERE: ")
    print_cards(carte_mazziere, False)
    print("PUNTEGGIO MAZZIERE: ", punteggio_mazziere)
        
    #controlla se giocatore ha blackjack
    if punteggio_giocatore == 21:
        print("HAI FATTO BLACKJACK!")
        quit()
        
    # se giocatore ha sballato
    if punteggio_giocatore > 21:
        print("Hai sballato! lol hai perso!!")
        quit()
        
    input()
        
    # Mosse del mazziere
    while punteggio_mazziere < 17:
        clear()
        
        print("il mazziere pesca una carta...")
        
        #carta al mazziere
        carta_mazziere = random.choice(mazzo)
        carte_mazziere.append(carta_mazziere)
        mazzo.remove(carta_mazziere)
        #aggiorno valore punteggio
        punteggio_mazziere += carta_mazziere.valore_carta
        
        #se una carta e' asso e si supera 21
        c = 0 
        while punteggio_mazziere > 21 and c < len(carte_mazziere):
            if carte_mazziere[c].valore_carta == 11:
                carte_mazziere[c].valore_carta = 1
                punteggio_mazziere -=10
                c +=1
            else:
                c +=1
                
        print("CARTE GIOCATORE: ")
        print_cards(carte_giocatore, False)
        print("PUNTEGGIO GIOCATORE = ", punteggio_giocatore)
        
        print()
        
        print("CARTE MAZZIERE: ")
        print_cards(carte_mazziere, False)
        print("PUNTEGGIO MAZZIERE =", punteggio_mazziere)
        
        input()
        
    # Dealer busts
    if punteggio_mazziere > 21:        
        print("IL MAZZIERE HA SBALLATO!!! HAI VINTO!!!") 
        quit()  
    
    # Dealer gets a blackjack
    if punteggio_mazziere == 21:
        print("IL MAZZIERE HA UN BLACKJACK!!! IL GIOCATORE HAPERSO ")
        quit()
    
    # TIE Game
    if punteggio_mazziere == punteggio_giocatore:
        print("PARITA'!!!!")

    # Player Wins
    elif punteggio_giocatore > punteggio_mazziere:
        print("VINCE IL GIOCATORE!!!")                 
    
    # Dealer Wins
    else:
        print("VINCE IL MAZZIERE!!!")       
                    
if __name__ == '__main__':
        
    semi = ["Spade", "Cuori", "Fiori", "Picche"]
    
    # The suit value 
    suits_values = {"Spade": "\u2664", "Cuori": "\u2661", "Fiori": "\u2667", "Picche": "\u2662"}
    
    carte = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    #A di base 11, se punteggio con A supera 21 A=1
    valore_carte = {"A": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10}
    
    mazzo = []
    
    #per selezionare seme
    for seme_carta in semi:

        #per selezionare numero
        for carta in carte:

            mazzo.append(Carta(suits_values[seme_carta], carta, valore_carte[carta]))
                
    blackjack_game(mazzo)