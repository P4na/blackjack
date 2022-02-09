import random

def stampa_carte(carte, hidden):
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


def pesca_mostra(carte_persona, punteggio_giocatore, mazzo, num_carte):
    while len(carte_persona) < num_carte:
        # prendere carta randomicamente
        carta_giocatore = random.choice(mazzo)
        carte_persona.append(carta_giocatore)
        mazzo.remove(carta_giocatore)
        # aggiorna punteggio giocatore
        punteggio_giocatore += carta_giocatore.valore_carta  # non so se va

        # stampa punteggio e carte
        print("PUNTEGGIO  GIOCATORE: ")
        stampa_carte(carte_persona, False)
        print("PUNTEGGIO GIOCATORE =  ", punteggio_giocatore)

        input()

    # nel caso entrambe le  carte siano A, rendi un A = 1
    if len(carte_persona) == num_carte:
        if carte_persona[0].valore_carta == 11 and carte_persona[1] == 11:
            carte_persona[0].valore_carta = 1
            punteggio_giocatore -= 10

