import numpy as np


class Pos(object):
    """Position dans l'espace de jeu"""
    def __init__(self,x,y):
        self.x=x
        self.y=y

class Carte(object):
    """Carte du jeu SABOOTERS"""
    tablechemin=[('(   )'),('( | )'),('(---)'),('( x )'),('(-x )'),('( x-)'),('(-+ )'),('( +-)'),('(-+-)')]
    matchemin=[[1,1,1],[0,2,0],[1,3,0],[0,3,1],[0,4,0],[0,5,0],[1,8,1],[1,6,1],[0,6,1],[1,6,0],[1,7,1],[0,7,1],[1,7,0],[1,8,1]]
    tableaction=[('   '),('XXX'),('ATT'),('DEF'),(' P '),(' L '),(' W '),(' M '),('MAP')]
    mataction=[[1,1,1],[2,4,0],[2,5,0],[2,6,0],[2,4,5],[2,4,6],[2,5,6],[3,4,0],[3,5,0],[3,6,0],[3,4,5],[3,4,6],[3,5,6],[7,8,5]]
    def __init__(self,typ):
        self.pos=[0,0]
        self.typ=typ
        if typ == 0 :
            self.vectapparence=Carte.matchemin[np.random.choice(np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13]))]
        if typ == 1 :
            self.vectapparence=Carte.mataction[np.random.choice(np.array([0,1,2,3,4,5,6,7,8,9,10,11,12]))]
        if typ == 2:
            self.vectapparence=Carte.mataction[13]

    def affiche(self,x):
        if x==0:
            print(Chemin.table[self.vectapparence[0]],end = "")
        if x==1:
            print(Chemin.table[self.vectapparence[1]],end = "")
        if x==2:
            print(Chemin.table[self.vectapparence[2]],end = "")

class Chemin(Carte):
    """Carte Chemin"""
    table=[('(   )'),('( | )'),('(---)'),('( x )'),('(-x )'),('( x-)'),('(-+ )'),('( +-)')]
    def __init__(self,pos,typ,up,mi,do):
        "up,mi et do determine le contenu des trois parties de la carte chemin"
        Carte.__init__(self,pos,typ)
        self.up=up
        self.mi=mi
        self.do=do

    def affiche(self,x):
        if x==0:
            print(Chemin.table[self.up],end = "")
        if x==1:
            print(Chemin.table[self.mi],end = "")
        if x==2:
            print(Chemin.table[self.do],end = "")

class Cheminrand(Carte):
    """Carte Chemin aleatoire"""
    table=[('(   )'),('( | )'),('(---)'),('( x )'),('(-x )'),('( x-)'),('(-+ )'),('( +-)'),('(-+-)')]
    mat=[[1,1,1],[0,2,0],[1,3,0],[0,3,1],[0,4,0],[0,5,0],[1,8,1],[1,6,1],[0,6,1],[1,6,0],[1,7,1],[0,7,1],[1,7,0],[1,8,1]]
    def __init__(self,pos,typ):
        "up,mi et do determine le contenu des trois parties de la carte chemin"
        Carte.__init__(self,pos,typ)

        #la carte sera parmie les 13 cartes chemin possible

        self.typchem=Cheminrand.mat[np.random.choice(np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13]))]

    def affiche(self,x):
        if x==0:
            print(Cheminrand.table[self.typchem[0]],end = "")
        if x==1:
            print(Cheminrand.table[self.typchem[1]],end = "")
        if x==2:
            print(Cheminrand.table[self.typchem[2]],end = "")




class Casevide(object):
    """Case vide du plateau"""
    def affiche(x):
        if x==0:
            print("     ",end = "")
        if x==1:
            print("     ",end = "")
        if x==2:
            print("     ",end = "")

    
        
        
