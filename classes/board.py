import numpy as np
import random
import os
from card import Carte


class Plateau(object):
    """Plateau du jeu SABOOTERS"""
    def __init__(self):
        #tableau binaire qui determine si une carte a ete posee 
        self.__cases_vides=np.zeros((5,9),int)
        #tableau compose des cartes present sur le plateau
        self.__cartes_posees=[]

    def add_carte(self,carte,pos):
        #On verifie si la carte posée est bien une carte
        if not isinstance ( carte , Carte ) :
            print("Erreur: uniquement des cartes peuvent être posee sur le plateau")
        
        #Les cartes d'arrivee sont placee face cache
        if carte.typ != 4 and carte.typ != 5:
            carte.face=1

        #On change l'état de la carte
        carte.etat=1

        #On défini la position de la carte
        carte.pos=pos

        #On ajoute la carte aux cartes du plateau
        self.__cartes_posees.append(carte)

        #On indique qu'une carte est posée à la position de la carte
        self.__cases_vides[carte.pos[0]][carte.pos[1]]=1
    
    #Fonction qui réinitialise le plateau
    def reset_plateau(self):
        self.__cases_vides=np.zeros((5,9),int)
        self.__cartes_posees=[]

    #Fonction qui affiche le plateau
    def affiche(self):
        #Fonction qui affiche le plateau de jeu 
        os.system("cls")  #efface le contenue de la console, valable que sur windows
   
            #affichage de la premiere ligne
        for i in range(0,10):
            if i==0 :
                print(" |",end = "")
            else:
                print(" ",i-1," ",end = "")
        print("")

            #affichage de la deuxieme ligne
        for i in range(0,10):
            if i==0 :
                print("-+",end = "")
            else:
                print("-----",end = "")
        print("")

        for i in range(0,5):
            for x in range(0,3):
                if x==1:
                    print(i,end = "")
                    print("|",end = "")
                else:
                    print(" |",end = "")
                for j in range(0,9):
                    if self.__cases_vides[i][j]==0:
                        print("     ",end = "")
                    else:
                        for k in range(len(self.__cartes_posees)):
                            if self.__cartes_posees[k].pos == [i,j]:
                                self.__cartes_posees[k].affiche(x)
                print("")

        #affichage de la derniere ligne
        for i in range(0,10):
            if i==0 :
                print("-+",end = "")
            else:
               print("-----",end = "")
        print("")

    @property
    def cartes_posees(self) : return self.__cartes_posees

    @property
    def cases_vides(self) : return self.__cases_vides

    @cartes_posees.setter
    def cartes_posees(self,cartes):
        self.__cartes_posees=cartes
