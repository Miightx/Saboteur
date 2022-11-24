import numpy as np
import random 
from deck import Deck
from menu import Menu
from player import Player
from hand import Hand

from mapp import Carte
from mapp import Plateau






class SABOOTERS(object):
    def __init__(self):
        self.__menu=Menu()
        self.__deck=Deck()
        self.__pioche=[]
        self.__defausse=[]
        self.__joueurs=[]
        self.__plateau=Plateau()

    def initpartie(self):
        #initialisation du menu
        self.__menu.start_game()

        #initialisation des joueurs
        for i in range(0,self.__menu.number):
            self.__joueurs.append(Player(self.__menu.players_name[i], self.__menu.roles[i], self.__menu.number))


    def initmanche(self):
        #initialisation de la manche

        #On melange les cartes
        self.__deck.random_cartes()

        #On defini les positions des cartes "END"
        set_pos_gold=random.sample([[0,8],[2,8],[4,8]], 3)

        #repartition des cartes
        k=0
        for i in range(0,len(self.__deck.cartes)):
            #On place les cartes arrive/depart sur le plateau
            if self.__deck.cartes[i].typ == 3 or self.__deck.cartes[i].typ == 4 or self.__deck.cartes[i].typ == 5:
                if self.__deck.cartes[i].typ==3:
                    self.__plateau.add_carte(self.__deck.cartes[i],[2,0])
                else:
                    self.__plateau.add_carte(self.__deck.cartes[i],set_pos_gold[k])
                    k=k+1
            #On cree la pioche avec les cartes action et chemin
            else :
                self.__pioche.append(self.__deck.cartes[i])
        
        #Les joueurs piochent leurs cartes
        for i in range(self.__menu.number):
            for j in range(self.__joueurs[i].hand.hand_size):
                self.__joueurs[i].piocher_carte(self.__pioche)

    def tourjoueur(self,x):
        #affichage du plateau et de la main du joueur dont c'est la tour
        self.__plateau.affiche()
        print("It is{0} turn:".format(self.__joueurs[x].name))
        self.__joueurs[x].hand.affiche()


        #Le joueur choisi une action
        choix_action=self.__joueurs[x].choix_action(self.__plateau)
        

        #On rafraichi l'etat du jeu
        self.__plateau.affiche()
        print("It is {0} turn:".format(self.__joueurs[x].name))
        self.__joueurs[x].hand.affiche()

        if choix_action == 1:

            #On demande au joueur quel carte il veut jouer
            choix_carte=self.__joueurs[x].choix_carte_act(self.__plateau)
            
            #On demande au joueur ou il veut poser sa carte
            pos=self.__joueurs[x].choix_pos(self.__plateau)
              
            #La carte est placee sur le plateau et le joueur pioche une nouvelle carte
            self.__plateau.add_carte(choix_carte,pos)
            self.__joueurs[x].hand.remove_card(choix_carte)
            self.__joueurs[x].piocher_carte(self.__pioche)

        if choix_action == 2:

            #On demande au joueur quelle carte il veut se defausser
            choix_carte=self.__joueurs[x].choix_carte_rem(self.__plateau)

            #La carte est retire de la main du joueur et place dans la defausse et la joueur pioche une nouvelle carte
            self.__defausse.append(choix_carte)
            self.__joueurs[x].hand.remove_card(choix_carte)
            self.__joueurs[x].piocher_carte(self.__pioche)

    def tour_pour_rien(self):
        for i in range(3):
            self.tourjoueur(0)
        
jeu=SABOOTERS()
jeu.initpartie()

jeu.initmanche()
jeu.tour_pour_rien()
