import numpy as np
import random
from .card import Carte




class Deck(object):
    #On cree les cartes du deck
    def __init__(self):
        self.__cartes=[]
        self.__cartes.append(Carte(3))
        self.__cartes.append(Carte(4))
        for i in range(2):
            self.__cartes.append(Carte(5))
        for i in range(40):
            self.__cartes.append(Carte(0))
        for i in range(26):
            self.__cartes.append(Carte(1))
        self.__cartes.append(Carte(2))

    #fonction qui permet de melanger les cartes
    def random_cartes(self):
        self.__cartes=random.sample(self.__cartes, len(self.__cartes))

    # def affiche(self):
    #     for i in range(0,len(self.__cartes)):
    #         self.__cartes[i].face=1

    #     for i in range(0,8):
    #         for x in range(0,3):
    #             for j in range(0,8):
    #                 self.__cartes[j+(i-1)*8].affiche(x)
    #             print("")
    #     for i in range(0,len(self.__cartes)):
    #         self.__cartes[i].face=0

    @property
    def cartes(self) : return self.__cartes

    # @cartes.setter
    # def cartes(self,cartes):
    #     self.__cartes=cartes