import numpy as np
import random 

from .deck import Deck
from .menu import Menu
from .player import Player
from .hand import Hand
from .card import Carte
from .board import Plateau
from .human import Human






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
            self.__joueurs.append(Human(self.__menu.players_name[i], self.__menu.roles[i], self.__menu.number))


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



    def tour_pour_rien(self):
        for i in range(3):
            self.__joueurs[0].tourjoueur(self.__plateau, self.__pioche, self.__defausse)
        
# jeu=SABOOTERS()
# jeu.initpartie()

# jeu.initmanche()
# jeu.tour_pour_rien()
