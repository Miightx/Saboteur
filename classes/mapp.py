import numpy as np
import random
import os

class Carte(object):
    """Carte du jeu SABOOTERS"""
    #Tables contenant le contenu des cartes
    tablechemin=[('(   )'),('( | )'),('(---)'),('( x )'),('(-x )'),('( x-)'),('(-+ )'),('( +-)'),('(-+-)'),('(-S-)'),('($$$)'),('(-N-)')]
    tableaction=[('(   )'),('(XXX)'),('(ATT)'),('(DEF)'),('( P )'),('( L )'),('( W )'),('( M )'),('(MAP)')]
    tablerecto=[('(   )'),('(+++)'),('(+S+)'),('(END)')]
    
    
    #Matrices contenant contenant les vecteurs permettant d'atribuer une apparence a chaques types de cartes
    matchemin=[[1,1,1],[0,2,0],[1,3,0],[0,3,1],[0,4,0],[0,5,0],[1,8,1],[1,6,1],[0,6,1],[1,6,0],[1,7,1],[0,7,1],[1,7,0],[1,8,1],[1,9,1],[10,10,10],[1,11,1]]
    mataction=[[1,1,1],[2,4,0],[2,5,0],[2,6,0],[2,4,5],[2,4,6],[2,5,6],[3,4,0],[3,5,0],[3,6,0],[3,4,5],[3,4,6],[3,5,6],[7,8,4]]
    matrecto=[[1,2,1],[0,3,0]]

    def __init__(self,typ):
        #On defini une position par default
        self.__pos = [0,0] 
        #On defini le type de carte
        self.__typ=typ
        #On defini un etat par default de la carte, etat neutre dans la pile de carte "0"
        self.__etat=0
        #On defini par default que le carte est face cachee
        self.__face=0
        #On tire au hasard une apparence a la carte selon son type
        if typ == 0 :
            #Carte chemin
            self.__vectapparence=Carte.matchemin[np.random.choice(np.array([0,1,2,3,4,5,6,7,8,9,10,11,12,13]))]
            self.__vectrecto=Carte.matrecto[0]
        if typ == 1 :
            #Carte action
            self.__vectapparence=Carte.mataction[np.random.choice(np.array([0,1,2,3,4,5,6,7,8,9,10,11,12]))]
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

    # @ classmethod
    # def typ_only ( cls , typ ) :
    #     pos = [0,0] 
    #     return cls ( typ , pos )


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
    def pos(self) : return self.__pos
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
        if face>=0 and face<=1:
            self.__face=face
    @etat.setter
    #0:"Pile de carte" 1:"Posee sur le plateau" 2:"main de joueur" 3:"defausse" 
    def etat(self,etat):
        self.__etat=0
        if etat>=0 and etat<=3 :
            self.__etat=etat
    @pos.setter
    def pos(self, pos) : 
        self.__pos = [0,0]
        if self.etat==1:
            if pos[0]>=0 and pos[0]<=4 and pos[1]>=0 and pos[1]<=8:
                self.__pos=pos


"""
• Type 0 : Carte chemin
• Type 1 : Carte action
• Type 2 : Carte map
• Type 3 : Carte start
• Type 4 : Carte gold
• Type 5 : Carte pierre 
"""

#-----------------------------------------------------------------------------------

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
