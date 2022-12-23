import numpy as np
import random
import os
from .card import Carte

class Path_card(Carte):
    def __init__(self,typ):
        super().__init__(typ)

        #On tire au hasard une apparence a la carte selon son type
        if typ == 0 :
            #Carte chemin
            chemin=np.random.choice(np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13]))
            self.__vectapparence=Carte.matchemin[chemin]
            self.__vectrecto=Carte.matrecto[0]
            self.__path=Carte.matpath[chemin]
        if typ == 3:
            #Carte start
            self.__vectapparence=Carte.matchemin[14]
            self.__vectrecto=Carte.matrecto[0]
            self.__path=Carte.matpath[14]
        if typ == 4:
            #Carte gold
            self.__vectapparence=Carte.matchemin[15]
            self.__vectrecto=Carte.matrecto[1]
            self.__path=Carte.matpath[15]
        if typ == 5:
            #Carte pierre
            self.__vectapparence=Carte.matchemin[16]
            self.__vectrecto=Carte.matrecto[1]
            self.__path=Carte.matpath[16]

    def affiche(self,x):
        #On affiche la partie de la carte que l'on souhaite afficher
        if self.face==1:
            if x==0:
                print(Carte.tablechemin[self.__vectapparence[0]],end = "")
            if x==1:
                print(Carte.tablechemin[self.__vectapparence[1]],end = "")
            if x==2:
                print(Carte.tablechemin[self.__vectapparence[2]],end = "")

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
    @property
    def path(self) : return self.__path


        