from Giocatore import Papà
from Giocatore import Trappola
from Giocatore import Gatto
from Giocatore import Colla1
from Giocatore import Colla2
from colorama import Fore, Back, Style
#import os

class PrimoLivello:
    def __init__(self, g):
        self.larghezza = 8
        self.lunghezza = 8
        self.giocatore = g
        self.noci = [(1, 4), (4, 7), (6, 0)]
        self.punteggio = 0
        self.papà = Papà(1)

    def stampa(self):
        for i in range(0, self.lunghezza):
            for j in range(0, self.larghezza):
                if self.controlloNoci(self.giocatore.x, self.giocatore.y):
                    self.punteggio += 1
                    for el in self.noci:
                        if el[0] == self.giocatore.x and el[1] == self.giocatore.y:
                            self.noci.remove(el)
                            break
                if self.giocatore.x == self.papà.x and self.giocatore.y == self.papà.y:
                    for i in range(0, self.lunghezza):
                        for j in range(0, self.larghezza):
                            if i == self.papà.x and j == self.papà.y:
                                print("[X]", end="")
                            else:
                                print("[ ]", end="")
                        print()
                    print("Il Papà ti ha catturato!")
                    return "Sconfitta"
                elif self.giocatore.x == 6 and self.giocatore.y == 4 or self.giocatore.x == 6 and self.giocatore.y == 5:
                    print("Sei andato a sbattere contro il muro.")
                    return "Sconfitta"
                elif self.giocatore.x == 7 and self.giocatore.y == 5:
                    print("BRAVO SEI ARRIVATO ALLA TANA! \nHAI VINTO!!")
                    return "Vittoria"
                else:
                    if i == self.giocatore.x and j == self.giocatore.y:
                        print(Fore.RED + "[G]", end=Style.RESET_ALL)
                    elif i == self.papà.x and j == self.papà.y:
                        print(Fore.BLUE + "[p]", end=Style.RESET_ALL)
                    elif i == 7 and j == 5:
                        print("[T]", end="")
                    elif i == 6 and j == 4 or i == 6 and j == 5:
                        print("[/]", end="")
                    elif self.controlloNoci(i, j):
                        print("\033[0;33;40m" + "[§]", end=Style.RESET_ALL)
                    else:
                        print("[ ]", end="")
            print()

    def start(self):
        while True:
            risultato1 = self.stampa()
            if risultato1 != None:
                return risultato1
            print("Il tuo punteggio è di: {}".format(self.punteggio) + "/3")
            direzione = input("Inserisci il movimento: ")
            if direzione == "s":
                if self.giocatore.x + 1 < self.larghezza:
                    self.giocatore.muoviGiu()
                    self.papà.muoviPapà(1)
            elif direzione == "w":
                if self.giocatore.x > 0:
                    self.giocatore.muoviSu()
                    self.papà.muoviPapà(1)
            elif direzione == "d":
                if self.giocatore.y + 1 < self.lunghezza:
                    self.giocatore.muoviDestra()
                    self.papà.muoviPapà(1)
            elif direzione == "a":
                if self.giocatore.y > 0:
                    self.giocatore.muoviSinistra()
                    self.papà.muoviPapà(1)
        #os.system('cls')

    def controlloNoci(self, i, j):
        for el in self.noci:
            if i == el[0] and j == el[1]:
                return True
        return False


class SecondoLivello:
    def __init__(self, g):
        self.larghezza = 10
        self.lunghezza = 10
        self.giocatore = g
        self.noci = [(5, 1), (8, 3), (2, 5), (7, 8)]
        self.punteggio = 0
        self.papà2 = Papà(2)
        self.trappola2 = Trappola(2)

    def stampa(self):
        for i in range(0, self.lunghezza):
            for j in range(0, self.larghezza):
                if self.controlloNoci(self.giocatore.x, self.giocatore.y):
                    self.punteggio += 1
                    for el in self.noci:
                        if el[0] == self.giocatore.x and el[1] == self.giocatore.y:
                            self.noci.remove(el)
                            break
                if self.giocatore.x == self.papà2.x and self.giocatore.y == self.papà2.y:
                    for i in range(0, self.lunghezza):
                        for j in range(0, self.larghezza):
                            if i == self.papà2.x and j == self.papà2.y:
                                print("[X]", end="")
                            else:
                                print("[ ]", end="")
                        print()
                    print("Il Papà ti ha catturato!")
                    return "Sconfitta"
                if self.giocatore.x == self.trappola2.x and self.giocatore.y == self.trappola2.y:
                    for i in range(0, self.lunghezza):
                        for j in range(0, self.larghezza):
                            if i == self.trappola2.x and j == self.trappola2.y:
                                print("[X]", end="")
                            else:
                                print("[ ]", end="")
                        print()
                    print("La super trappola ti ha catturato!")
                    return "Sconfitta"
                elif self.giocatore.x == 1 and self.giocatore.y == 2 or self.giocatore.x == 3 and self.giocatore.y == 9 or self.giocatore.x == 6 and self.giocatore.y == 7:
                    print("Sei andato a sbattere contro l'albero.")
                    return "Sconfitta"
                elif self.giocatore.x == 8 and self.giocatore.y == 5 or self.giocatore.x == 8 and self.giocatore.y == 6 or self.giocatore.x == 9 and self.giocatore.y == 6:
                    print("Sei andato a sbattere contro il muro.")
                    return "Sconfitta"
                elif self.giocatore.x == 9 and self.giocatore.y == 5:
                    print("BRAVO SEI ARRIVATO ALLA TANA! \nHAI VINTO!")
                    return "Vittoria"
                else:
                    if i == self.giocatore.x and j == self.giocatore.y:
                        print(Fore.RED + "[G]", end=Style.RESET_ALL)
                    elif i == self.papà2.x and j == self.papà2.y:
                        print(Fore.BLUE + "[p]", end=Style.RESET_ALL)
                    elif i == self.trappola2.x and j == self.trappola2.y:
                        print("\033[0;36;40m" + "[t]", end=Style.RESET_ALL)
                    elif i == 9 and j == 5:
                        print("[T]", end="")
                    elif i == 8 and j == 5 or i == 8 and j == 6 or i == 9 and j == 6:
                        print("[/]", end="")
                    elif i == 1 and j == 2 or i == 6 and j == 7 or i == 3 and j == 9:
                        print("[*]", end="")
                    elif self.controlloNoci(i, j):
                        print("\033[0;33;40m" + "[§]", end=Style.RESET_ALL)
                    else:
                        print("[ ]", end="")
            print()

    def start(self):
        while True:
            risultato = self.stampa()
            if risultato != None:
                return risultato
            print("Il tuo punteggio è di: {}".format(self.punteggio) + "/4")
            direzione = input("Inserisci il movimento: ")
            if direzione == "s":
                if self.giocatore.x + 1 < self.larghezza:
                    self.giocatore.muoviGiu()
                    self.papà2.muoviPapà(2)
                    self.trappola2.muoviTrappola(2)
            elif direzione == "w":
                if self.giocatore.x > 0:
                    self.giocatore.muoviSu()
                    self.papà2.muoviPapà(2)
                    self.trappola2.muoviTrappola(2)
            elif direzione == "d":
                if self.giocatore.y + 1 < self.lunghezza:
                    self.giocatore.muoviDestra()
                    self.papà2.muoviPapà(2)
                    self.trappola2.muoviTrappola(2)
            elif direzione == "a":
                if self.giocatore.y > 0:
                    self.giocatore.muoviSinistra()
                    self.papà2.muoviPapà(2)
                    self.trappola2.muoviTrappola(2)
        #os.system('cls')

    def controlloNoci(self, i, j):
        for el in self.noci:
            if i == el[0] and j == el[1]:
                return True
        return False


class TerzoLivello:
    def __init__(self, g):
        self.larghezza = 12
        self.lunghezza = 12
        self.giocatore = g
        self.noci = [(2, 3), (5, 5), (7, 9), (9, 2), (10, 11)]
        self.punteggio = 0
        self.papà3 = Papà(3)
        self.trappola3 = Trappola(3)
        self.gatto3 = Gatto(3)

    def stampa(self):
        for i in range(0, self.lunghezza):
            for j in range(0, self.larghezza):
                if self.controlloNoci(self.giocatore.x, self.giocatore.y):
                    self.punteggio += 1
                    for el in self.noci:
                        if el[0] == self.giocatore.x and el[1] == self.giocatore.y:
                            self.noci.remove(el)
                            break
                if self.giocatore.x == self.papà3.x and self.giocatore.y ==  self.papà3.y:
                    for i in range(0, self.lunghezza):
                        for j in range(0, self.larghezza):
                            if i == self.papà3.x and j ==  self.papà3.y:
                                print("[X]", end="")
                            else:
                                print("[ ]", end="") 
                        print()
                    print("Il Papà ti ha catturato!")           
                    return "Sconfitta"
                if self.giocatore.x == self.trappola3.x and self.giocatore.y ==  self.trappola3.y:
                    for i in range(0, self.lunghezza):
                        for j in range(0, self.larghezza):
                            if i == self.trappola3.x and j ==  self.trappola3.y:
                                print("[X]", end="")
                            else:
                                print("[ ]", end="") 
                        print()
                    print("La super trappola ti ha catturato!")         
                    return "Sconfitta"
                if self.giocatore.x == self.gatto3.x and self.giocatore.y ==  self.gatto3.y:
                    for i in range(0, self.lunghezza):
                        for j in range(0, self.larghezza):
                            if i == self.gatto3.x and j ==  self.gatto3.y:
                                print("[X]", end="")
                            else:
                                print("[ ]", end="") 
                        print()
                    print("La Gina ti ha catturato!")           
                    return "Sconfitta"
                elif self.giocatore.x == 2 and self.giocatore.y == 2 or self.giocatore.x == 1 and self.giocatore.y == 3 or self.giocatore.x == 0 and self.giocatore.y == 10 or self.giocatore.x == 6 and self.giocatore.y == 0:
                    print("Sei andato a sbattere contro l'albero.")
                    return "Sconfitta"
                elif self.giocatore.x == 10 and self.giocatore.y == 4 or self.giocatore.x == 10 and self.giocatore.y == 5 or self.giocatore.x == 11 and self.giocatore.y == 4:
                    print("Sei andato a sbattere contro il muro.")  
                    return "Sconfitta"
                elif self.giocatore.x == 11 and self.giocatore.y == 5:
                    print("BRAVO SEI ARRIVATO ALLA TANA! \nHAI VINTO!")
                    return "Vittoria"
                else :
                    if i == self.giocatore.x and j == self.giocatore.y:
                        print(Fore.RED+"[G]", end=Style.RESET_ALL)
                    elif i == self.papà3.x and j == self.papà3.y:
                        print(Fore.BLUE + "[p]", end=Style.RESET_ALL)
                    elif i == self.trappola3.x and j == self.trappola3.y:
                        print("\033[0;36;40m" + "[t]", end=Style.RESET_ALL)
                    elif i == self.gatto3.x and j == self.gatto3.y:
                        print("\033[0;35;40m" + "[g]", end=Style.RESET_ALL)
                    elif i == 11 and j == 5:
                        print("[T]", end="")
                    elif i == 10 and j == 4 or i == 10 and j == 5 or i == 11 and j == 4:
                        print("[/]", end="")
                    elif i == 2 and j == 2 or i == 1 and j == 3 or i == 0 and j == 10 or i == 6 and j == 0:
                        print("[*]", end="")
                    elif self.controlloNoci(i, j):
                        print("\033[0;33;40m" + "[§]", end=Style.RESET_ALL)
                    else:
                        print("[ ]", end="")
            print()

    def start(self):
        while True:
            risultato = self.stampa()
            if risultato != None:
                return risultato
            print("Il tuo punteggio è di: {}".format(self.punteggio)+"/5")
            direzione = input("Inserisci il movimento: ")
            if direzione == "s":
                if self.giocatore.x + 1 < self.larghezza:
                    self.giocatore.muoviGiu()
                    self.papà3.muoviPapà(3)
                    self.trappola3.muoviTrappola(3)
                    self.gatto3.muoviGatto(3)
            elif direzione == "w":
                if self.giocatore.x > 0:
                    self.giocatore.muoviSu()
                    self.papà3.muoviPapà(3)
                    self.trappola3.muoviTrappola(3)
                    self.gatto3.muoviGatto(3)
            elif direzione == "d":
                if self.giocatore.y + 1 < self.lunghezza:
                    self.giocatore.muoviDestra()
                    self.papà3.muoviPapà(3)
                    self.trappola3.muoviTrappola(3)
                    self.gatto3.muoviGatto(3)
            elif direzione == "a":
                if self.giocatore.y > 0:
                    self.giocatore.muoviSinistra()
                    self.papà3.muoviPapà(3)
                    self.trappola3.muoviTrappola(3)
                    self.gatto3.muoviGatto(3)
            #os.system('cls')

    def controlloNoci(self, i, j):
        for el in self.noci:
            if i == el[0] and j == el[1]:
                return True
        return False


class QuartoLivello:
    def __init__(self, g):
        self.larghezza = 14
        self.lunghezza = 14
        self.giocatore = g
        self.noci = [(4, 1), (7, 6), (2, 10), (9, 11), (12, 2)]
        self.punteggio = 0
        self.papà4 = Papà(4)
        self.trappola4 = Trappola(4)
        self.gatto4 = Gatto(4)
        self.colla1 = Colla1()
        self.colla2 = Colla2()

    def stampa(self):
        for i in range(0, self.lunghezza):
            for j in range(0, self.larghezza):
                if self.controlloNoci(self.giocatore.x, self.giocatore.y):
                    self.punteggio += 1
                    for el in self.noci:
                        if el[0] == self.giocatore.x and el[1] == self.giocatore.y:
                            self.noci.remove(el)
                            break
                if self.giocatore.x == self.papà4.x and self.giocatore.y ==  self.papà4.y:
                    for i in range(0, self.lunghezza):
                        for j in range(0, self.larghezza):
                            if i == self.papà4.x and j ==  self.papà4.y:
                                print("[X]", end="")
                            else:
                                print("[ ]", end="") 
                        print()
                    print("Il Papà ti ha catturato!")           
                    return "Sconfitta"
                if self.giocatore.x == self.trappola4.x and self.giocatore.y ==  self.trappola4.y:
                    for i in range(0, self.lunghezza):
                        for j in range(0, self.larghezza):
                            if i == self.trappola4.x and j ==  self.trappola4.y:
                                print("[X]", end="")
                            else:
                                print("[ ]", end="") 
                        print()
                    print("La super trappola ti ha catturato!")         
                    return "Sconfitta"
                if self.giocatore.x == self.gatto4.x and self.giocatore.y ==  self.gatto4.y:
                    for i in range(0, self.lunghezza):
                        for j in range(0, self.larghezza):
                            if i == self.gatto4.x and j ==  self.gatto4.y:
                                print("[X]", end="")
                            else:
                                print("[ ]", end="") 
                        print()
                    print("La Gina ti ha catturato!")           
                    return "Sconfitta"
                if self.giocatore.x == self.colla1.x and self.giocatore.y ==  self.colla1.y or self.giocatore.x ==self.colla2.x and self.giocatore.y ==  self.colla2.y:
                    for i in range(0, self.lunghezza):
                        for j in range(0, self.larghezza):
                            if i == self.colla1.x and j == self.colla1.y or i == self.colla2.x and j == self.colla2.y:
                                print("[X]", end="")
                            else:
                                print("[ ]", end="") 
                        print()
                    print("Sei rimasto intrappolato nella colla!")          
                    return "Sconfitta"
                elif self.giocatore.x == 1 and self.giocatore.y == 2 or self.giocatore.x == 3 and self.giocatore.y == 13 or self.giocatore.x == 7 and self.giocatore.y == 1:
                    print("Sei andato a sbattere contro l'albero.")
                    return "Sconfitta"
                elif self.giocatore.x == 12 and self.giocatore.y == 8 or self.giocatore.x == 12 and self.giocatore.y == 9 or self.giocatore.x == 12 and self.giocatore.y == 10:
                    print("Sei andato a sbattere contro il muro.")  
                    return "Sconfitta"
                elif self.giocatore.x == 13 and self.giocatore.y == 9:
                    return "Vittoria"
                else :
                    if i == self.giocatore.x and j == self.giocatore.y:
                        print(Fore.RED+"[G]", end=Style.RESET_ALL)
                    elif i == self.papà4.x and j == self.papà4.y:
                        print(Fore.BLUE + "[p]", end=Style.RESET_ALL)
                    elif i == self.trappola4.x and j == self.trappola4.y:
                        print("\033[0;36;40m" + "[t]", end=Style.RESET_ALL)
                    elif i == self.gatto4.x and j == self.gatto4.y:
                        print("\033[0;35;40m" + "[g]", end=Style.RESET_ALL)
                    elif i == self.colla1.x and j == self.colla1.y or i == self.colla2.x and j == self.colla2.y:
                        print("\033[1;32;40m" + "[c]", end=Style.RESET_ALL)
                    elif i == 13 and j == 9:
                        print("[T]", end="")
                    elif i == 12 and j == 8 or i == 12 and j == 9 or i == 12 and j == 10:
                        print("[/]", end="")
                    elif i == 1 and j == 2 or i == 3 and j == 13 or i == 7 and j == 1:
                        print("[*]", end="")
                    elif self.controlloNoci(i, j):
                        print("\033[0;33;40m" + "[§]", end=Style.RESET_ALL)
                    else:
                        print("[ ]", end="")
            print()

    def start(self):
        while True:
            risultato = self.stampa()
            if risultato != None:
                return risultato
            print("Il tuo punteggio è di: {}".format(self.punteggio)+"/5")
            direzione = input("Inserisci il movimento: ")
            if direzione == "s":
                if self.giocatore.x + 1 < self.larghezza:
                    self.giocatore.muoviGiu()
                    self.papà4.muoviPapà(4)
                    self.trappola4.muoviTrappola(4)
                    self.gatto4.muoviGatto(4)
                    self.colla1.muoviColla1()
                    self.colla2.muoviColla2()
            elif direzione == "w":
                if self.giocatore.x > 0:
                    self.giocatore.muoviSu()
                    self.papà4.muoviPapà(4)
                    self.trappola4.muoviTrappola(4)
                    self.gatto4.muoviGatto(4)
                    self.colla1.muoviColla1()
                    self.colla2.muoviColla2()
            elif direzione == "d":
                if self.giocatore.y + 1 < self.lunghezza:
                    self.giocatore.muoviDestra()
                    self.papà4.muoviPapà(4)
                    self.trappola4.muoviTrappola(4)
                    self.gatto4.muoviGatto(4)
                    self.colla1.muoviColla1()
                    self.colla2.muoviColla2()
            elif direzione == "a":
                if self.giocatore.y > 0:
                    self.giocatore.muoviSinistra()
                    self.papà4.muoviPapà(4)
                    self.trappola4.muoviTrappola(4)
                    self.gatto4.muoviGatto(4)
                    self.colla1.muoviColla1()
                    self.colla2.muoviColla2()
            #os.system('cls')

    def controlloNoci(self, i, j):
        for el in self.noci:
            if i == el[0] and j == el[1]:
                return True
        return False