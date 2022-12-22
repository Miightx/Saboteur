import numpy as np
import random
import os


class Carte(object):
    """Carte du jeu SABOOTERS"""
    #Tables contenant le contenu des cartes
                #   0          1         2         3         4         5         6         7         8         9         10        11
    tablechemin=[('(   )'),('( | )'),('(---)'),('( x )'),('(-x )'),('( x-)'),('(-+ )'),('( +-)'),('(-+-)'),('(-S-)'),('($$$)'),('(-N-)')]
    tableaction=[('(   )'),('(XXX)'),('(REP)'),('(BRK)'),('( P )'),('( L )'),('( W )'),('( M )'),('(MAP)')]
    tablerecto=[('(   )'),('(+++)'),('(+S+)'),('(END)')]
    
    
    #Matrices contenant contenant les vecteurs permettant d'atribuer une apparence a chaques types de cartes
    matchemin=[[1,1,1],[0,2,0],[1,3,0],[0,3,1],[0,4,0],[0,5,0],[1,8,1],[1,6,1],[0,6,1],[1,6,0],[1,7,1],[0,7,1],[1,7,0],[1,8,1],[1,9,1],[10,10,10],[1,11,1]]
    mataction=[[1,1,1],[2,4,0],[2,5,0],[2,6,0],[2,4,5],[2,4,6],[2,5,6],[3,4,0],[3,5,0],[3,6,0],[3,4,5],[3,4,6],[3,5,6],[7,8,4]]
    matrecto=[[1,2,1],[0,3,0]]

    def __init__(self,typ):
        #On defini une position par default 
        self.pos = [0,0] #La position de la carte n'est pas un attribut privé car une carte peut se trouvé à priori n'importe où

        #On defini le type de carte
        self.__typ=typ
        #On defini un etat par default de la carte, etat neutre dans la pile de carte "0"
        # self.__etat=0
        #On defini par default que le carte est face cachee
        self.__face=0
        #On tire au hasard une apparence a la carte selon son type
        if typ == 0 :
            #Carte chemin
            self.__vectapparence=Carte.matchemin[np.random.choice(np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13]))]
            self.__vectrecto=Carte.matrecto[0]
        if typ == 1 :
            #Carte action
            self.__vectapparence=Carte.mataction[np.random.choice(np.array([1,2,3,4,5,6,7,8,9,10,11,12]))]
            self.__vectrecto=Carte.matrecto[0]
        if typ == 2:
            #Carte map
            self.__vectapparence=Carte.mataction[13]
            self.__vectrecto=Carte.matrecto[0]
        if typ == 3:
            #Carte start
            self.__vectapparence=Carte.matchemin[14]
            self.__vectrecto=Carte.matrecto[0]
        if typ == 4:
            #Carte gold
            self.__vectapparence=Carte.matchemin[15]
            self.__vectrecto=Carte.matrecto[1]
        if typ == 5:
            #Carte pierre
            self.__vectapparence=Carte.matchemin[16]
            self.__vectrecto=Carte.matrecto[1]

        if typ == 6:
            #Carte éboulement
            self.__vectapparence=Carte.mataction[0]
            self.__vectrecto=Carte.matrecto[0]



    def affiche(self,x):
        #On affiche la partie de la carte que l'on souhaite afficher
        if self.__face==1:
            if self.__typ == 0 or self.__typ == 3 or self.__typ == 4 or self.__typ == 5:
                if x==0:
                    print(Carte.tablechemin[self.__vectapparence[0]],end = "")
                if x==1:
                    print(Carte.tablechemin[self.__vectapparence[1]],end = "")
                if x==2:
                    print(Carte.tablechemin[self.__vectapparence[2]],end = "")
            if self.__typ == 1 or self.__typ == 2:
                if x==0:
                    print(Carte.tableaction[self.__vectapparence[0]],end = "")
                if x==1:
                    print(Carte.tableaction[self.__vectapparence[1]],end = "")
                if x==2:
                    print(Carte.tableaction[self.__vectapparence[2]],end = "")
        if self.__face==0:
            if x==0:
                print(Carte.tablerecto[self.__vectrecto[0]],end = "")
            if x==1:
                print(Carte.tablerecto[self.__vectrecto[1]],end = "")
            if x==2:
                print(Carte.tablerecto[self.__vectrecto[2]],end = "")

    def affiche_carte_entiere(self):
        for x in range(0,3):
            print(Carte.tablechemin[self.__vectapparence[x]])
        
            


    @property
    def typ(self) : return self.__typ
    @property
    def vectapparence(self) : return self.__vectapparence
    @property
    def vectrecto(self) : return self.__vectrecto
    @property
    def etat(self) : return self.__etat
    @property
    def face(self) : return self.__face

    @face.setter
    def face(self,face):
        self.__face=0
        if face>=0 and face<=1:
            self.__face=face
    # @etat.setter
    # #0:"Pile de carte" 1:"Posee sur le plateau" 2:"main de joueur" 3:"defausse" 
    # def etat(self,etat):
    #     self.__etat=0
    #     if etat>=0 and etat<=3 :
    #         self.__etat=etat



"""
• Type 0 : Carte chemin
• Type 1 : Carte action
• Type 2 : Carte map
• Type 3 : Carte start
• Type 4 : Carte gold
• Type 5 : Carte pierre 
• Type 6 : Carte éboulement 
"""


