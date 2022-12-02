import numpy as np
import random
import os
from card import Carte


class Plateau(object):
    """Plateau du jeu SABOOTERS"""
    def __init__(self):
        #tableau binaire qui determine si une carte a ete posee 
        self.__cases_vides=np.zeros((20,20),int)
        #tableau compose des cartes present sur le plateau
        self.__cartes_posees=[]
        self.__dimensions=[[0,5],[0,9]]

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

        #On réajuste la dimention du plateau par rapport à la position de la nouvelle carte posée
        if pos[0] < self.__dimensions[0][0]:
            self.__dimensions[0][0]=pos[0]

        if pos[0] > self.__dimensions[0][1]:
            self.__dimensions[0][1]=pos[0]

        if pos[1] < self.__dimensions[1][0]:
            self.__dimensions[1][0]=pos[1]

        if pos[1] > self.__dimensions[1][1]:
            self.__dimensions[1][1]=pos[1]

        #On indique qu'une carte est posée à la position de la carte
        self.__cases_vides[carte.pos[0]+10][carte.pos[1]+10]=1
        print(self.__cases_vides)
    
    #Fonction qui réinitialise le plateau
    def reset_plateau(self):
        self.__cases_vides=np.zeros((50,100),int)
        self.__cartes_posees=[]
        self.__dimensions=[[0,5],[0,9]]

    #Fonction qui affiche le plateau
    def affiche(self):
        #Fonction qui affiche le plateau de jeu 
        os.system("cls")  #efface le contenue de la console, valable que sur windows


   
            #affichage de la premiere ligne
        for j in range(self.__dimensions[1][0],self.__dimensions[1][1]+1):
            if j==self.__dimensions[1][0] :
                print(" |",end = "")
            else:
                print(" ",j-1," ",end = "")
        print("")

            #affichage de la deuxieme ligne
        for j in range(self.__dimensions[1][0],self.__dimensions[1][1]+1):
            if j==self.__dimensions[1][0] :
                print("-+",end = "")
            else:
                print("-----",end = "")
        print("")

        for i in range(self.__dimensions[0][0],self.__dimensions[0][1]+1):
            for x in range(0,3):
                if x==1:
                    print(i,end = "")
                    print("|",end = "")
                else:
                    print(" |",end = "")
                for j in range(self.__dimensions[1][0],self.__dimensions[1][1]):
                    if self.__cases_vides[i+10][j+10]==0:
                        print("     ",end = "")
                    else:
                        for k in range(len(self.__cartes_posees)):
                            if self.__cartes_posees[k].pos == [i,j]:
                                self.__cartes_posees[k].affiche(x)
                print("")

        #affichage de la derniere ligne
        for j in range(self.__dimensions[1][0],self.__dimensions[1][1]+1):
            if j==0 :
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


