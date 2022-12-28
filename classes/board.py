import numpy as np
import random
import os
import sys
from .card import Carte
from .path_card import Path_card

class Plateau(object):
    """Plateau du jeu SABOOTERS"""
    def __init__(self):
        #tableau binaire qui determine si une carte a ete posee 
        self.__pathmap=np.ones((30,30,5),int)
        for i in range(len(self.__pathmap)):
            for j in range(len(self.__pathmap[0])):
                self.__pathmap[i][j][0]=0
        #tableau compose des cartes present sur le plateau
        self.__cartes_posees=[]
        self.__dimensions=[[0,5],[0,9]]
        self.__pos_gold=[]
        self.__pos_start=[]
        self.__pos_stone=[]
        self.__gold_found=0
        #Variable qui permet d'afficher à quelle manche le jeu est
        self.no_manche=0

    def add_carte(self,carte,pos,init_game=0): #Le paramètre init_game permet de dire si on initialise la partie
        #On verifie si la carte posée est bien une carte
        if not isinstance ( carte , Path_card ) :
            print("Erreur: uniquement des cartes peuvent être posee sur le plateau")
            sys.exit()

        if pos[0]<-10 or pos[0]>10 or pos[1]<-10 or pos[1]>10:
            print("Erreur: La position de la carte va au dela de la taille maximale du plateau")
            sys.exit()

        if self.__pathmap[pos[0]+15][pos[1]+15][0]==1 :
            print("Erreur: une carte est déja positionnée à l'emplacement désiré")
            sys.exit()

        #Les cartes d'arrivee sont placee face cache
        if carte.typ != 4 and carte.typ != 5:
            carte.face=1

        #Le plateau garde en memoire la position de la carte gold
        if carte.typ == 4 :
            self.__pos_gold=pos
        
        #Le plateau garde en memoire la position des cartes stone
        if carte.typ == 5 :
            self.__pos_stone.append(pos)

        #Le plateau garde en memoire la position de la carte start
        if carte.typ == 3 :
            self.__pos_start=pos

        #On change l'état de la carte
        #carte.etat=1

        #On défini la position de la carte
        carte.pos=pos

        #On ajoute la carte aux cartes du plateau
        self.__cartes_posees.append(carte)

        #On réajuste la dimention du plateau par rapport à la position de la nouvelle carte posée
        if pos[0] < self.__dimensions[0][0]:
            self.__dimensions[0][0]=pos[0]

        if pos[0]+1 > self.__dimensions[0][1]:
            self.__dimensions[0][1]=pos[0]+1

        if pos[1] < self.__dimensions[1][0]:
            self.__dimensions[1][0]=pos[1]

        if pos[1]+1 > self.__dimensions[1][1]:
            self.__dimensions[1][1]=pos[1]+1

        #On indique qu'une carte est posée à la position de la carte
        self.__pathmap[carte.pos[0]+15][carte.pos[1]+15]=carte.path

        if init_game==0:
            #On verifie si la carte a été posé à coté d'une carte END
            if ((pos[0]==self.__pos_gold[0]+1 or pos[0]==self.__pos_gold[0]-1) and pos[1]==self.__pos_gold[1]) or ((pos[1]==self.__pos_gold[1]+1 or pos[1]==self.__pos_gold[1]-1) and pos[0]==self.__pos_gold[0]):
                for i in range(len(self.__cartes_posees)):
                    if self.__cartes_posees[i].pos==self.__pos_gold:
                        self.__cartes_posees[i].face==1
                        self.__gold_found=1
                        

            for j in range(len(self.__pos_stone)):
                if pos[0]==self.__pos_stone[j][0]+1 or pos[0]==self.__pos_stone[j][0]-1 or pos[1]==self.__pos_stone[j][1]+1 or pos[1]==self.__pos_stone[j][1]-1:
                    for i in range(len(self.__cartes_posees)):
                        if self.__cartes_posees[i].pos==self.__pos_stone[j]:
                            self.__cartes_posees[i].face==1

    # def remove_card(self,carte):
    #     if not isinstance ( carte , Path_card ) :
    #         print("Erreur: uniquement des cartes peuvent être retiré du plateau")
    #         sys.exit()

    def collapse(self,pos):
        etat=False
        for carte in self.__cartes_posees:
            if carte.pos==pos:
                etat=True
                self.__cartes_posees.remove(carte)
                break
        if etat==True:
            self.__pathmap[pos[0]][pos[1]]=[0,1,1,1]
        return etat





 
    
    #Fonction qui réinitialise le plateau
    def reset_plateau(self):
        self.__pathmap=np.ones((30,30,5),int)
        for i in range(len(self.__pathmap)):
            for j in range(len(self.__pathmap[0])):
                self.__pathmap[i][j][0]=0
        self.__cartes_posees=[]
        self.__dimensions=[[0,5],[0,9]]
        self.__pos_gold=[]
        self.__pos_stone=[]

    #Fonction qui affiche le plateau
    def affiche(self):
        #Fonction qui affiche le plateau de jeu 
        #os.system("cls")  #efface le contenue de la console, valable que sur windows


   
            #affichage de la premiere ligne
        for j in range(self.__dimensions[1][0],self.__dimensions[1][1]+1):
            if j==self.__dimensions[1][0] :
                print("  |",end = "")
            else:
                if (j-1)<0 or (j-1)>=10:
                    print(f" {j-1}  ",end = "")
                else:
                    print(f"  {j-1}  ",end = "")
        print("")

            #affichage de la deuxieme ligne
        for j in range(self.__dimensions[1][0],self.__dimensions[1][1]+1):
            if j==self.__dimensions[1][0] :
                print("--+",end = "")
            else:
                print("-----",end = "")
        print("")

        for i in range(self.__dimensions[0][0],self.__dimensions[0][1]):
            for x in range(0,3):
                if x==1:
                    if i<0 or i>=10:
                        print(i,end = "|")
                        #print("|",end = "")
                    else:
                        print(f" {i}",end = "|")
                        #print("|",end = "")
                else:
                    print("  |",end = "")
                for j in range(self.__dimensions[1][0],self.__dimensions[1][1]):
                    if self.__pathmap[i+15][j+15][0]==0:
                        print("     ",end = "")
                    else:
                        for k in range(len(self.__cartes_posees)):
                            if self.__cartes_posees[k].pos == [i,j]:
                                self.__cartes_posees[k].affiche(x)
                print("")

        #affichage de la derniere ligne
        for j in range(self.__dimensions[1][0],self.__dimensions[1][1]+1):
            if j==self.__dimensions[1][0] :
                print("--+",end = "")
            else:
               print("-----",end = "")
        print("")

    @property
    def cartes_posees(self) : return self.__cartes_posees

    @property
    def pathmap(self) : return self.__pathmap

    @property
    def gold_found(self) : return self.__gold_found

    @property
    def pos_gold(self) : return self.__pos_gold

    # @cartes_posees.setter
    # def cartes_posees(self,cartes):
    #     self.__cartes_posees=cartes
