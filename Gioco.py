import Giocatore
from Livelli import PrimoLivello
from Livelli import SecondoLivello
from Livelli import TerzoLivello
from Livelli import QuartoLivello
from colorama import init
from colorama import Fore, Back, Style

init()
print('\033[1;31;40m' + "                                                                 THE DORMOUSE BUSTERS"+Style.RESET_ALL)
print("")
print("Ciao, sono Gaspare, il capo ghiro della colonia della Villetta. \nTu sei quello nuovo vero?")
print("La nostra grande famiglia ti da il benvenuto e ti accoglie a braccia aperte.")
print("Però per entrare ufficialmente nella colonia devi passare alcune prove per dimostrarci che sei degno di entrare nella nostra famiglia.")
print("")

nome = ""
while nome == "":
    nome = input("Come ti chiami giovanotto? ")
print("")
print(nome, "in queste 4 sfide dovrai affrontare le insidie che pullulano il nostro territorio, scappare dai pericoli più temuti da noi ghiri \ne arrivare alla tana sano e salvo tanto meglio con le noci.")
print("Sei pronto per iniziare? \n1.Certo non vedo l'ora! \n2.Non penso di voler faticare cosi tanto.")
risp = input()
while risp != "1" and risp != "2":
    print(
        "Non mi rispondi? Sei pronto per iniziare? \n1.Certo non vedo l'ora! \n2.Non penso di voler faticare cosi tanto.")
    risp = input()
if risp == "1":
    print("Bene. ", nome, "allora iniziamo! \n""")
    print("In questa avventura troverei il temuto papà Pietro! Sono anni che cerca di studiare tutti i modi possibili e inimmaginabili per cacciarci. Ma non è ancora riuscito nel suo intento.")
    print("Inoltre devi stare attento al muro del fienile perchè per arrivare alla tana sano e salvo devi evitarlo.")
    print("Ah giusto che sbadato tu non conosci il posto ne gli elementi di cui ti sto parlando!")
    print("Il papà Pietro è " + Fore.BLUE + "[p]" + Style.RESET_ALL + ", i muri del fienile è [/] e le noci che devi raccogliere da portare nella tana sono " + "\033[0;33;40m" + "[§]" + Style.RESET_ALL + "." + "\nAdesso dovresti essere pronto per iniziare. \nBuona fortuna", nome, ".")
    print("")

    g = Giocatore.Giocatore(nome)
    while True:
        lvl1 = PrimoLivello(g)
        risultato1 = lvl1.start()
        risposta = ""

        if risultato1 == "Vittoria":
            print("Hai fatto un punteggio di: {}".format(lvl1.punteggio) + "/3")
            risposta = input("Premi invio per il secondo livello, r per ricominciare, altro per uscire.")
        elif risultato1 == "Sconfitta":
            print("Hai perso!!")
            risposta = input("Premi invio per ricominciare, un altro tasto per uscire.")

        if risultato1 == "Vittoria" and risposta == "":
            g.x = 0
            g.y = 0
            print("")
            print("La prima sfida è andata, ma era solo per scaldarsi. \nPerchè questa volta non sarà cosi semplice.")
            print("Nel bosco oltre al papà Pietro " + Fore.BLUE + "[p]" + Style.RESET_ALL + " potresti incontrare, cosa che non ti auguro, " + "\033[0;36;40m" + "[t]" + Style.RESET_ALL + " ovvero la super trappola, una fedele alleata del papà Pietro. In fine ti conisglio \ndi stare attento, oltre che ai [/], ai [*], noci altissimi che svettano tra i castani nel bosco.")
            while True:
                lvl2 = SecondoLivello(g)
                risultato2 = lvl2.start()
                risposta = ""

                if risultato2 == "Vittoria":
                    print("Bravo, hai vinto!")
                    print("Hai fatto un punteggio di: {}".format(lvl2.punteggio) + "/4")
                    risposta = input("Premi invio per il terzo livello, r per ricominciare, altro per uscire.")
                elif risultato2 == "Sconfitta":
                    print("Hai perso!!")
                    risposta = input("Premi invio per ricominciare, un altro tasto per uscire.")
                
                if risultato2 == "Vittoria" and risposta == "":
                    g.x = 0
                    g.y = 0
                    print("")
                    print("Sei più in gamba di quello che credessi ",nome ,", ma vediamo come te la cavi contro la gatta Gina.")
                    print("La ""\033[0;35;40m" + "[g]" + Style.RESET_ALL + " è la tanto amata e coccolata Gina, la gatta della Villetta.")
                    print("Tanto amata dalla famiglia Tondelli perchè oltre ad essere una bella gattina mette a dura prova la nostra colonia; pensa che nell'ultimo mesetto ha catturato \nben 6 membri della nostra colonia!")
                    print("Insomma lei, il " + Fore.BLUE + "[p]" + Style.RESET_ALL +" e la " + "\033[0;36;40m" + "[t]" + Style.RESET_ALL + " formano un trio acchiappa-ghiri da paura. \nIn bocca al lupo e mi raccomamdo presta attenzione.")
                    while True:    
                        lvl3 = TerzoLivello(g)
                        risultato3 = lvl3.start()
                        risposta = ""
                        if risultato3 == "Vittoria":
                            print("Bravo, hai vinto!")
                            print("Hai fatto un punteggio di: {}".format(lvl3.punteggio) + "/5")
                            risposta = input("Premi invio per il quarto livello, r per ricominciare, altro per uscire.")
                        elif risultato3 == "Sconfitta":
                            print("Hai perso!!")
                            risposta = input("Premi invio per ricominciare, un altro tasto per uscire.")

                        if risultato3 == "Vittoria" and risposta == "":
                            g.x = 0
                            g.y = 0
                            print("")
                            print(nome, "sei arrivato alla tua ultima sfida. Se supererai questa prova farai ufficialmente parte della nostra colonia.")
                            print("In questa prova troverai ben 4 nemici che cercheranno di catturarti e impedirti di arrivare alla tana: il " + Fore.BLUE + "[p]" + Style.RESET_ALL +", la " + "\033[0;36;40m" + "[t]" + Style.RESET_ALL + ", la " + "\033[0;35;40m" + "[g]" + Style.RESET_ALL + " e l'ultimo ma non meno importante: la " + "\033[1;32;40m" + "[c]" + Style.RESET_ALL + ", la colla per ghiri, che si espande come una macchia di olio. Attento non metterci le zampe sopra se no è finita!")
                            while True:
                                lvl4 = QuartoLivello(g)
                                risultato4 = lvl4.start()
                                risposta = ""
                                if risultato4 == "Vittoria":
                                    print("BRAVO, HAI VINTO!")
                                    print("Hai fatto un punteggio di: {}".format(lvl4.punteggio) + "/5")
                                    print("Complimenti ",nome, "hai superato tutte le sfide dando tutto il meglio di te.")
                                    print("Benvenuto nella colonia. Ti presenterò tutti i membri ma direi che per oggi hai già fatto abbastanza.")
                                    print("Ora vado che ho altri ghiri impazienti di entrare nella colonia. \nCi si vede in giro", nome)
                                    risposta = input("Premi r per ricominciare e invio per uscire.")
                                elif risultato4 == "Sconfitta":
                                    print("Hai perso!!")
                                    risposta = input("Premi invio per ricominciare, un altro tasto per uscire.")
                                if risultato4 == "Vittoria" and risposta == "r":
                                    g.x = 0
                                    g.y = 0
                                    continue
                                elif risultato4 == "Sconfitta" and risposta == "":
                                    g.x = 0
                                    g.y = 0
                                    continue
                                elif risultato4 == "Vittoria" and risposta == "" or risultato4 == "Sconfitta" and risposta != "":
                                    break
                            break      
                        elif risultato3 == "Vittoria" and risposta == "r":
                            g.x = 0
                            g.y = 0
                            continue
                        elif risultato3 == "Sconfitta" and risposta == "":
                            g.x = 0
                            g.y = 0
                            continue
                        else:
                            print("Alla prossima", nome, "è stato un piacere conoscerti.")
                            break
                    break
                elif risultato2 == "Vittoria" and risposta == "r":
                    g.x = 0
                    g.y = 0
                    continue
                elif risultato2 == "Sconfitta" and risposta == "":
                    g.x = 0
                    g.y = 0
                    continue
                else:
                    print("Alla prossima ",nome, "è stato un piacere conoscerti.")
                    break
            break
        elif risultato1 == "Vittoria" and risposta == "r":
            g.x = 0
            g.y = 0
            continue
        elif risultato1 == "Sconfitta" and risposta == "":
            g.x = 0
            g.y = 0
            continue
        else:
            print("Alla prossima ",nome, "è stato un piacere conoscerti.")
            break

else:
    print("Allora dovrai cercarti un altra colonia. E' stato un piacere conoscerti. A presto", nome)

input("Fine del gioco.")