import numpy as np


class Carte(object):
    """Carte du jeu SABOOTERS"""
    #Tables contenant le contenu des cartes
    tablechemin=[('(   )'),('( | )'),('(---)'),('( x )'),('(-x )'),('( x-)'),('(-+ )'),('( +-)'),('(-+-)')]
    tableaction=[('(   )'),('XXX'),('ATT'),('DEF'),(' P '),(' L '),(' W '),(' M '),('MAP')]
    #Matrices contenant contenant les vecteurs permettant d'atribuer une apparence a chaques types de cartes
    matchemin=[[1,1,1],[0,2,0],[1,3,0],[0,3,1],[0,4,0],[0,5,0],[1,8,1],[1,6,1],[0,6,1],[1,6,0],[1,7,1],[0,7,1],[1,7,0],[1,8,1]]
    mataction=[[1,1,1],[2,4,0],[2,5,0],[2,6,0],[2,4,5],[2,4,6],[2,5,6],[3,4,0],[3,5,0],[3,6,0],[3,4,5],[3,4,6],[3,5,6],[7,8,5]]

    def __init__(self,typ):
        #On defini une position par default
        self.pos=[0,0]
        self.typ=typ
        #On tire au hasard une apparence a la carte selon son type
        if typ == 0 :
            self.vectapparence=Carte.matchemin[np.random.choice(np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13]))]
        if typ == 1 :
            self.vectapparence=Carte.mataction[np.random.choice(np.array([0,1,2,3,4,5,6,7,8,9,10,11,12]))]
        if typ == 2:
            self.vectapparence=Carte.mataction[13]

    def affiche(self,x):
        #On affiche la partie de la carte que l'on souhaite afficher
        if self.typ == 0:
            if x==0:
                print(Carte.tablechemin[self.vectapparence[0]],end = "")
            if x==1:
                print(Carte.tablechemin[self.vectapparence[1]],end = "")
            if x==2:
                print(Carte.tablechemin[self.vectapparence[2]],end = "")
        if self.typ == 1 or self.typ == 2:
            if x==0:
                print(Carte.tableaction[self.vectapparence[0]],end = "")
            if x==1:
                print(Carte.tableaction[self.vectapparence[1]],end = "")
            if x==2:
                print(Carte.tableaction[self.vectapparence[2]],end = "")


class Casevide(object):
    """Case vide du plateau"""
    def affiche(x):
        if x==0:
            print("     ",end = "")
        if x==1:
            print("     ",end = "")
        if x==2:
            print("     ",end = "")

    
        
        
