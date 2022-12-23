import numpy as np
import random
import os
from .card import Carte


class Action_card(Carte):
    def __init__(self,typ):
        super().__init__(typ)

        #On tire au hasard une apparence a la carte selon son type
        if typ == 1 :
            #Carte action_tools
            self.__vectapparence=Carte.mataction[np.random.choice(np.array([1,2,3,4,5,6,7,8,9,10,11,12]))]
            self.__vectrecto=Carte.matrecto[0]
        if typ == 2:
            #Carte map
            self.__vectapparence=Carte.mataction[13]
            self.__vectrecto=Carte.matrecto[0]
        if typ == 6:
            #Carte éboulement
            self.__vectapparence=Carte.mataction[0]
            self.__vectrecto=Carte.matrecto[0]

    def affiche(self,x):
        #On affiche la partie de la carte que l'on souhaite afficher
        if self.face==1:
            if self.typ == 1 or self.typ == 2:
                if x==0:
                    print(Carte.tableaction[self.__vectapparence[0]],end = "")
                if x==1:
                    print(Carte.tableaction[self.__vectapparence[1]],end = "")
                if x==2:
                    print(Carte.tableaction[self.__vectapparence[2]],end = "")
        if self.face==0:
            if x==0:
                print(Carte.tablerecto[self.__vectrecto[0]],end = "")
            if x==1:
                print(Carte.tablerecto[self.__vectrecto[1]],end = "")
            if x==2:
                print(Carte.tablerecto[self.__vectrecto[2]],end = "")

    @property
    def vectapparence(self) : return self.__vectapparence
    @property
    def vectrecto(self) : return self.__vectrecto
        
