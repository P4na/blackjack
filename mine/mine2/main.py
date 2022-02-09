import random
import utility


class Carta:
    def __init__(self, seme, valore, valore_carta):
        self.seme = seme
        self.valore = valore
        self.valore_carta = valore_carta


def prima_mazziere():
    pass


def blackjack_game(mazzo):
    # carte sia per mazziere che giocatore
    carte_giocatore = []
    carte_mazziere = []

    # punteggio sia per mazziere che giocatore
    punteggio_giocatore = 0
    punteggio_mazziere = 0

    while len(carte_giocatore) < 2:

        # prendere carta randomicamente
        carta_giocatore = random.choice(mazzo)
        carte_giocatore.append(carta_giocatore)
        mazzo.remove(carta_giocatore)

        # aggiorna punteggio giocatore
        punteggio_giocatore += carta_giocatore.valore_carta  # non so se va

        # nel caso entrambe le  carte siano A, rendi un A = 1
        if len(carte_giocatore) == 2:
            if carte_giocatore[0].valore_carta == 11 and carte_giocatore[1] == 11:
                carte_giocatore[0].valore_carta = 1
                punteggio_giocatore -= 10

        # stampa punteggio e carte
        print("PUNTEGGIO  GIOCATORE: ")
        utility.stampa_carte(carte_giocatore, False)
        print("PUNTEGGIO GIOCATORE =  ", punteggio_giocatore)

        input()

        # carta a mazziere randomica
        carta_mazziere = random.choice(mazzo)
        carte_mazziere.append(carta_mazziere)
        mazzo.remove(carta_mazziere)

        # aggiorna punteggio mazziere
        punteggio_mazziere += carta_mazziere.valore_carta

        # stampa carte e punteggio mazziere, mantieni la seconda carta nascosta insieme al punteggio
        print("CARTE MAZZIERE: ")
        if len(carte_mazziere) == 1:
            utility.stampa_carte(carte_mazziere, False)
            print("PUNTEGGIO MAZZIERE = ", punteggio_mazziere)
        else:
            utility.stampa_carte(carte_mazziere[:-1], True)
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

    # stampa carte mazziere e giocatore
    print("CARTE MAZZIERE: ")
    utility.stampa_carte(carte_mazziere[:-1], True)
    print("PUNTEGGIO MAZZIERE: ", punteggio_mazziere - carte_mazziere[-1].valore_carta)

    print()

    print("CARTE GIOCATORE: ")
    utility.stampa_carte(carte_giocatore, False)
    print("PUNTEGGIO GIOCATORE: ", punteggio_giocatore)

    # decidere mosse giocatore
    while punteggio_giocatore < 21:
        choice = input("Scrivi C per una nuova carta o S per stare :")

        if len(choice) != 1 or (choice.upper() != "C" and choice.upper() != "S"):
            print("Sbagliato, riprova!")

        # se giocatore vuole nuova carta
        if choice.upper() == "C":

            # dai nuova carta
            carta_giocatore = random.choice(mazzo)
            carte_giocatore.append(carta_giocatore)
            mazzo.remove(carta_giocatore)

            # aggiorna punteggio giocatore
            punteggio_giocatore += carta_giocatore.valore_carta

            # se il giocatore prene un asso
            c = 0
            while punteggio_giocatore > 21 and c < len(carte_giocatore):
                if carte_giocatore[c].valore_carta == 11:
                    carte_giocatore[c].valore_carta = 1
                    punteggio_giocatore -= 10
                    c += 1
                else:
                    c += 1

            print("CARTE MAZZIERE: ")
            utility.stampa_carte(carte_mazziere[:-1], True)
            print("PUNTEGGIO MAZZIERE: ", punteggio_mazziere - carte_mazziere[-1].valore_carta)

            print()

            print("CARTE GIOCATORE: ")
            utility.stampa_carte(carte_giocatore, False)
            print("Punteggio giocatore = ", punteggio_giocatore)

        # se il giocatore decide di restare
        if choice.upper() == "S":
            break

    # mostra carta nascosta mazziere
    print("CARTE GIOCATORE: ")
    utility.stampa_carte(carte_giocatore, False)
    print("Punteggio giocatore = ", punteggio_giocatore)

    print()
    print("il mazziere mostra la carta nascosta...")

    print("CARTE MAZZIERE: ")
    utility.stampa_carte(carte_mazziere, False)
    print("PUNTEGGIO MAZZIERE: ", punteggio_mazziere)

    # controlla se giocatore ha blackjack
    if punteggio_giocatore == 21:
        print("HAI FATTO BLACKJACK!")
        quit()

    # se giocatore ha sballato
    if punteggio_giocatore > 21:
        print("Hai sballato! lol hai perso!!")
        quit()

    input()

    while punteggio_mazziere < 17:

        print("il mazziere pesca una carta...")

        # carta al mazziere
        carta_mazziere = random.choice(mazzo)
        carte_mazziere.append(carta_mazziere)
        mazzo.remove(carta_mazziere)
        # aggiorno valore punteggio
        punteggio_mazziere += carta_mazziere.valore_carta

        # se una carta e' asso e si supera 21
        c = 0
        while punteggio_mazziere > 21 and c < len(carte_mazziere):
            if carte_mazziere[c].valore_carta == 11:
                carte_mazziere[c].valore_carta = 1
                punteggio_mazziere -= 10
                c += 1
            else:
                c += 1

        print("CARTE GIOCATORE: ")
        utility.stampa_carte(carte_giocatore, False)
        print("PUNTEGGIO GIOCATORE = ", punteggio_giocatore)

        print()

        print("CARTE MAZZIERE: ")
        utility.stampa_carte(carte_mazziere, False)
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

    valori_seme = {"Spade": "\u2664", "Cuori": "\u2661", "Fiori": "\u2667", "Picche": "\u2662"}

    carte = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

    valore_carte = {"A": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10,
                    "K": 10}

    mazzo = []

    for seme_carta in semi:
        for carta in carte:
            mazzo.append(Carta(valori_seme[seme_carta], carta, valore_carte[carta]))

    blackjack_game(mazzo)
