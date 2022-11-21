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
        self.__cases_vides=np.zeros((5,9),int)
        self.__cartes_posees=[]

    def add_carte(self,carte,pos):
        if not isinstance ( carte , Carte ) :
            print("Erreur: uniquement des cartes peuvent être posee sur le plateau")
        
        if carte.typ != 4 and carte.typ != 5:
            carte.face=1
        carte.etat=1
        carte.pos=pos

        self.__cartes_posees.append(carte)
        self.__cases_vides[carte.pos[0]][carte.pos[1]]=1
    
    def reset_plateau(self):
        self.__cases_vides=np.zeros((5,9),int)
        self.__cartes_posees=[]

    def affiche(self):
        #Fonction qui affiche le plateau de jeu 
        os.system("cls")  #efface le contenue de la console, valable que sur windows
            #affiche de la premiere ligne
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
    
#-----------------------------------------------------------------------------------


class Menu(object):

    def __init__(self):  # Property
        self.__number = 0
        self.__players_name = []
        self.__bot = []
        self.__roles = []
    
    #Methodes
    def __aff_wel(self):  # Affichage du début
        print("+--------------------------------------------------------------------+")
        print("| Welcome to SabOOtters, where dwarf otters look for gold in a mine! |")
        print("+--------------------------------------------------------------------+")

    def __get_number(self):  # Nombre de joueurs
        print("How many players?")
        etat = False
        while (etat == False):
            self.__number = input()
            if (len(self.__number)==1 or len(self.__number)==2):
                if (self.__number.isdecimal()==True):
                    self.__number=int(self.__number)
                    if (self.__number > 2 and self.__number < 11):
                        print("There is", self.__number, "players")
                        etat = True
                    else:
                        print("Please choose a number between 3 and 10")
                else:
                    print('Please write a correct number')
            else:
                print('Please write a number')


    def __players(self):  # Configuration des joueurs
        for k in range(self.__number):
            print('Please enter the name of player', k + 1 )
            print('')
            joueur = 0
            joueur = input()
            self.__players_name.append(joueur)
            print('The name of the player is:', self.__players_name[k])
            print('Please press 0 if the player is an AI and press 1 if the player is an Human')
            etat = False
            bot = []
            while (etat == False):
                bot = input()
                if (bot == '1'):
                    self.__bot.append("Human")
                    etat = True

                elif (bot == '0'):
                    self.__bot.append("AI")
                    etat = True
                else:
                    print("Please select 0 (AI) or 1 (Human):")
                    etat = False

    def __cartes_roles(self):  # Saboteur or Digger
        personnage=[]
        if (self.__number == 3):
            personnage = ['S', 'C', 'C', 'C']
            self.__roles = random.sample(personnage, 3)
        elif (self.__number == 4):
            personnage = ['S', 'C', 'C', 'C', 'C']
            self.__roles = random.sample(personnage, 4)
        elif (self.__number == 5):
            personnage = ['S', 'S', 'C', 'C', 'C', 'C']
            self.__roles = random.sample(personnage, 5)
        elif (self.__number == 6):
            personnage = ['S', 'S', 'C', 'C', 'C', 'C']
            self.__roles = random.sample(personnage, 6)
        elif (self.__number == 7):
            personnage = ['S', 'S', 'S', 'C', 'C', 'C', 'C', 'C']
            self.__roles = random.sample(personnage, 7)
        elif (self.__number == 8):
            personnage = ['S', 'S', 'S', 'C', 'C', 'C', 'C', 'C', 'C']
            self.__roles = random.sample(personnage, 8)
        elif (self.__number == 9):
            personnage = ['S', 'S', 'S', 'C', 'C', 'C', 'C', 'C', 'C', 'C']
            self.__roles = random.sample(personnage, 9)
        elif (self.__number == 10):
            personnage = ['S', 'S', 'S', 'S', 'C', 'C', 'C', 'C', 'C', 'C', 'C']
            self.__roles = random.sample(personnage, 10)

    def __affichage_debut_fin(self):
        total=[]
        for k in range (self.__number-1):
            total.append(self.__players_name[k] + '(' + self.__bot[k]+'),')
        total.append(self.__players_name[self.__number-1] + '(' + self.__bot[self.__number-1]+')')
        total = ' '.join(total)
        print('---------------------')
        print('The', self.__number, 'players are:', total)

    def start_game(self):
        self.__aff_wel() 
        self.__get_number() 
        self.__players() 
        self.__cartes_roles()
        self.__affichage_debut_fin()

    @property
    def number(self):
        return self.__number

    @property
    def players_name(self):
        return self.__players_name

    @property
    def bot(self):
        return self.__bot

    @property
    def roles(self):
        return self.__roles

#-----------------------------------------------------------------------------------

class Player(object):
    def __init__(self,name,role,nb_players):
        self.__name = name
        self.__role = role    #le role c'est de la classe menu.personnage[i]
        self.__hand = Hand(nb_players) #pour afficher la main: player.hand.display_hand()

    def piocher_carte(self,pioche):
        pioche[0].face=1
        self.__hand.cards.append(pioche[0])
        pioche.remove(pioche[0])

    @property
    def name(self):
        return self.__name

    @property
    def role(self):
        return self.__role

    @property
    def hand(self):
        return self.__hand

    @hand.setter
    def hand(self,hand):
        self.__hand=hand




"""
• à 3 joueurs : 1 Saboteur et 3 Chercheurs
• à 4 joueurs : 1 Saboteur et 4 Chercheurs
• à 5 joueurs : 2 Saboteurs et 4 Chercheurs
• à 6 joueurs : 2 Saboteurs et 5 Chercheurs
• à 7 joueurs : 3 Saboteurs et 5 Chercheurs
• à 8 joueurs : 3 Saboteurs et 6 Chercheurs
• à 9 joueurs : 3 Saboteurs et 7 Chercheurs
• à 10 joueurs : toutes les cartes Rôle (4 Saboteurs et 7 Chercheurs)
"""

#-----------------------------------------------------------------------------------

class Hand(object):
    def __init__(self, nb_players):
        self.__cards = []
        if nb_players <= 5:
            self.__hand_size = 6
        elif nb_players <= 7:
            self.__hand_size = 5
        else:
            self.__hand_size = 4

    def affiche(self):
        #Fonction qui affiche la main du joueur   

        for x in range(0,3):
            for i in range(2*self.__hand_size):
                if x==1 and i%2==0:
                    print((i//2)+1,end = "")
                    print(": ",end = "")
                elif i%2==0:
                    print("   ",end = "")
                elif i%2 != 0 and x==1:
                    self.__cards[(i-1)//2].affiche(x)
                    print(", ",end = "")
                elif i%2 != 0:
                    self.__cards[(i-1)//2].affiche(x)
                    print("  ",end = "")
            print("")


    
    def add_card(self, card): #ajouter une carte
        if len(self.__cards)==self.__hand_size:
            return
        self.__cards.append(card)

    def remove_card(self, card): #enlever une carte
        self.__cards.remove(card)
    
    def use_card(self, card): #utiliser une carte
        self.remove_card(card)
        card.use() 

    @property
    def hand_size(self):
        return self.__hand_size

    @property
    def cards(self):
        return self.__cards

    @cards.setter
    def cards(self,cards):
        self.__cards=cards   

#-----------------------------------------------------------------------------------

class Deck(object):
    #On cree les cartes du deck
    def __init__(self):
        self.__cartes=[]
        self.__cartes.append(Carte(3))
        self.__cartes.append(Carte(4))
        for i in range(2):
            self.__cartes.append(Carte(5))
        for i in range(40):
            self.__cartes.append(Carte(0))
        for i in range(26):
            self.__cartes.append(Carte(1))
        self.__cartes.append(Carte(2))

    #fonction qui permet de melanger les cartes
    def random_cartes(self):
        self.__cartes=random.sample(self.__cartes, len(self.__cartes))

    def affiche(self):
        for i in range(0,len(self.__cartes)):
            self.__cartes[i].face=1

        for i in range(0,8):
            for x in range(0,3):
                for j in range(0,8):
                    self.__cartes[j+(i-1)*8].affiche(x)
                print("")
        for i in range(0,len(self.__cartes)):
            self.__cartes[i].face=0

    @property
    def cartes(self) : return self.__cartes

    @cartes.setter
    def cartes(self,cartes):
        self.__cartes=cartes

#-----------------------------------------------------------------------------------


class SABOOTERS(object):
    def __init__(self):
        self.__menu=Menu()
        self.__deck=Deck()
        self.__pioche=[]
        self.__defausse=[]
        self.__joueurs=[]
        self.__plateau=Plateau()

    def initpartie(self):
        #initialisation du menu
        self.__menu.start_game()

        #initialisation des joueurs
        for i in range(0,self.__menu.number):
            self.__joueurs.append(Player(self.__menu.players_name[i], self.__menu.roles[i], self.__menu.number))


    def initmanche(self):
        #initialisation de la manche

        #On melange les cartes
        self.__deck.random_cartes()

        #On defini les positions des cartes "END"
        set_pos_gold=random.sample([[0,8],[2,8],[4,8]], 3)

        #repartition des cartes
        k=0
        for i in range(0,len(self.__deck.cartes)):
            #On place les cartes arrive/depart sur le plateau
            if self.__deck.cartes[i].typ == 3 or self.__deck.cartes[i].typ == 4 or self.__deck.cartes[i].typ == 5:
                if self.__deck.cartes[i].typ==3:
                    self.__plateau.add_carte(self.__deck.cartes[i],[2,0])
                else:
                    self.__plateau.add_carte(self.__deck.cartes[i],set_pos_gold[k])
                    k=k+1
            #On cree la pioche avec les cartes action et chemin
            else :
                self.__pioche.append(self.__deck.cartes[i])
        
        #Les joueurs piochent leurs cartes
        for i in range(self.__menu.number):
            for j in range(self.__joueurs[i].hand.hand_size):
                self.__joueurs[i].piocher_carte(self.__pioche)

    def tourjoueur(self,x):
        #affichage du plateau et de la main du joueur dont c'est la tour
        self.__plateau.affiche()
        print("It is{0} turn:".format(self.__joueurs[x].name))
        self.__joueurs[x].hand.affiche()

        #Le joueur choisi une action
        print("What action do you want to take?")
        print("1) Use a card")
        print("2) Passing your turn and throw away a card")
        choix_action=int(input())

        #On s'assure que le joueur choisi une action parmis les actions possibles
        while choix_action !=1 and choix_action !=2:
            print("Please, don't do anything else and just play!")
            print("1) Use a card")
            print("2) Passing your turn and throw away a card")
            choix_action=int(input())
        

        #On rafraichi l'etat du jeu
        self.__plateau.affiche()
        print("It is {0} turn:".format(self.__joueurs[x].name))
        self.__joueurs[x].hand.affiche()

        if choix_action == 1:
            no_carte=int(input("What card would you like to play (1 to {0})?".format(self.__joueurs[x].hand.hand_size)))-1

            #On s'assure que le joueur choisisse une de ses cartes
            while no_carte < 0 or no_carte > self.__joueurs[x].hand.hand_size-1:
                print("Please, do not steal a card from your neighbour!")
                no_carte=int(input("What card would you like to play (1 to {0})?".format(self.__joueurs[x].hand.hand_size)))-1

            choix_carte=self.__joueurs[x].hand.cards[no_carte]
            pos=[]
            pos.append(int(input("Where do you want to place your card (x value)?")))
            pos.append(int(input("(y value)?")))
            
            #On s'assure que le joueur pose bien la carte sur le plateau
            while pos[0] < 0 or pos[0] > 4 or pos[1] < 0 or pos[1] >8 :
                print("Please place the card on the board (0<=x<=4) (0<=y<=8)")
                pos=[]
                pos.append(int(input("Where do you want to place your card (x value)?")))
                pos.append(int(input("(y value)?")))
                

            self.__plateau.add_carte(choix_carte,pos)
            self.__joueurs[x].hand.remove_card(choix_carte)
            self.__joueurs[x].piocher_carte(self.__pioche)

        if choix_action == 2:
            no_carte=int(input("Which card do you want to throw away (1 to {0})?".format(self.__joueurs[x].hand.hand_size)))-1
            choix_carte=self.__joueurs[x].hand.cards[no_carte]
            self.__joueurs[x].hand.remove_card(choix_carte)
            self.__joueurs[x].piocher_carte(self.__pioche)

    def tour_pour_rien(self):
        for i in range(3):
            self.tourjoueur(0)
        


jeu=SABOOTERS()
jeu.initpartie()

jeu.initmanche()
jeu.tour_pour_rien()








