import numpy as np
import random
import os
from .card import Carte

class Path_card(Carte):
    """Cartes chemin du jeu SABOOTERS
    • Type 0 : Carte chemin
    • Type 3 : Carte start
    • Type 4 : Carte gold
    • Type 5 : Carte pierre"""

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
        else:
            print("Erreur: la valeur du type de carte est incorrecte")
            sys.exit()

    def affiche(self,x):
        #On affiche la partie de la carte que l'on souhaite afficher
        if self.face==1:
            if x==0:
                print(Carte.tablechemin[self.__vectapparence[0]],end = "")
            elif x==1:
                print(Carte.tablechemin[self.__vectapparence[1]],end = "")
            elif x==2:
                print(Carte.tablechemin[self.__vectapparence[2]],end = "")
            else:
                print("Erreur: la valeur d'affichage de la carte est incorrecte, veuilliez choisir une valeur entre 0 et 2")
                sys.exit()

        if self.face==0:
            if x==0:
                print(Carte.tablerecto[self.__vectrecto[0]],end = "")
            elif x==1:
                print(Carte.tablerecto[self.__vectrecto[1]],end = "")
            elif x==2:
                print(Carte.tablerecto[self.__vectrecto[2]],end = "")
            else:
                print("Erreur: la valeur d'affichage de la carte est incorrecte, veuilliez choisir une valeur entre 0 et 2")
                sys.exit()

    def __str__(self):
        st=Carte.tablechemin[self.__vectapparence[0]]+"\n"+Carte.tablechemin[self.__vectapparence[1]]+"\n"+Carte.tablechemin[self.__vectapparence[2]]
        return st

    def __eq__(self,other):

        if not isinstance ( other , Action_card ) :
            return False

        if ( self is other ) :
            return True

        if self.typ != other.typ or self.__vectapparence != other.vectapparence:
            return False

        return True

    @property
    def vectapparence(self) : return self.__vectapparence
    @property
    def vectrecto(self) : return self.__vectrecto
    @property
    def path(self) : return self.__path


        