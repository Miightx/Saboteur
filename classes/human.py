import numpy as np
import random
import os
from .hand import Hand
from .card import Carte
from .board import Plateau
from .player import Player
import sys



class Human(Player):
    def __init__(self,name,role,nb_players):
        super ( ) . __init__ (name,role,nb_players)

    def __print_game_state_player(self,plateau):
        #affichage du plateau et de la main du joueur dont c'est la tour
        plateau.affiche()
        print("It is{0} turn:".format(self.name))
        self.hand.affiche()

    def __choix_action(self,plateau):

        if not isinstance ( plateau , Plateau ) :
            print("Erreur: Le joueur a besoin du plateau pour prendre une decision")
            sys.exit()


        #affichage du plateau et de la main du joueur dont c'est la tour
        self.__print_game_state_player(plateau)


        #Le joueur choisi une action
        print("What action do you want to take?")
        print("1) Use a card")
        print("2) Passing your turn and throw away a card")
        

        etat = False
        while (etat == False):
            choix_action=input()
            if (choix_action.isdecimal()==True):
                choix_action=int(choix_action)
                if (choix_action == 1 or choix_action == 2):
                    etat = True
                else:
                    self.__print_game_state_player(plateau)
                    print("Please, don't do anything else and just play!")
                    print("1) Use a card")
                    print("2) Passing your turn and throw away a card")
            else:
                self.__print_game_state_player(plateau)
                print("Please, don't do anything else and just play!")
                print("1) Use a card")
                print("2) Passing your turn and throw away a card")


        return choix_action

    def __choix_carte_act(self,plateau):
        if not isinstance ( plateau , Plateau ) :
            print("Erreur: Le joueur a besoin du plateau pour prendre une decision")
            sys.exit()

        #On demande au joueur quel carte il veut jouer
        self.__print_game_state_player(plateau)
        print("What card would you like to play (1 to {0})?".format(self.hand.hand_size))

        #On s'assure que le joueur choisisse une de ses cartes
        etat = False
        while (etat == False):
            no_carte=input()
            if (no_carte.isdecimal()==True):
                no_carte=int(no_carte)
                if (no_carte > 0 and no_carte <= self.hand.hand_size):
                    etat = True
                    no_carte=no_carte-1
                else:
                    self.__print_game_state_player(plateau)
                    print("Please, do not steal a card from your neighbour!")
                    print("What card would you like to play (1 to {0})?".format(self.hand.hand_size))
            else:
                self.__print_game_state_player(plateau)
                print("Please, do not steal a card from your neighbour!")
                print("What card would you like to play (1 to {0})?".format(self.hand.hand_size))


        #On recupere la carte que le joueur a choisi
        choix_carte=self.hand.cards[no_carte]

        return choix_carte

    def __choix_carte_rem(self,plateau):
        if not isinstance ( plateau , Plateau ) :
            print("Erreur: Le joueur a besoin du plateau pour prendre une decision")
            sys.exit()

        #On demande au joueur quelle carte il veut se defausser
        self.__print_game_state_player(plateau)
        print("Which card do you want to throw away (1 to {0})?".format(self.hand.hand_size))

        #On s'assure que le joueur choisisse une de ses cartes
        etat = False
        while (etat == False):
            no_carte=input()
            if (no_carte.isdecimal()==True):
                no_carte=int(no_carte)
                if (no_carte > 0 and no_carte <= self.hand.hand_size):
                    etat = True
                    no_carte=no_carte-1
                else:
                    self.__print_game_state_player(plateau)
                    print("Please, do not steal a card from your neighbour!")
                    print("Which card do you want to throw away (1 to {0})?".format(self.hand.hand_size))
            else:
                self.__print_game_state_player(plateau)
                print("Please, do not steal a card from your neighbour!")
                print("Which card do you want to throw away (1 to {0})?".format(self.hand.hand_size))
                
        choix_carte=self.hand.cards[no_carte]

        return choix_carte
    
    def __choix_pos(self,plateau):
        if not isinstance ( plateau , Plateau ) :
            print("Erreur: Le joueur a besoin du plateau pour prendre une decision")
            sys.exit()

        pos=[]
        x=0
        y=0


        self.__print_game_state_player(plateau)
        print("Where do you want to place your card ?")


            
        #On s'assure que le joueur pose bien la carte sur le plateau
        etat = False
        while (etat == False):
            x=input("(x value)")
            y=input("(y value)")
            if (x.isdecimal()==True and y.isdecimal()==True):
                x=int(x)
                y=int(y)
                if (x >= -10 and x <= 10 and y >= -10 and y <= 10):
                    if plateau.cases_vides[x+15][y+15]==0 :
                        etat = True
                        pos=[x,y]
                    else:
                        self.__print_game_state_player(plateau)
                        print("A card is already positioned at the desired location, choose another position")
                        print("Where do you want to place your card ?")
                else:
                    self.__print_game_state_player(plateau)
                    print("Please place the card on the board (-10<=x<=10) (-10<=y<=10)")
                    print("Where do you want to place your card ?")
            else:
                self.__print_game_state_player(plateau)
                print("Please place the card on the board (-10<=x<=10) (-10<=y<=10)")
                print("Where do you want to place your card ?")


        return pos

    def tourjoueur(self,plateau,pioche,defausse):

        #Le joueur choisi une action
        choix_action=self.__choix_action(plateau)
        
        if choix_action == 1:

            #On demande au joueur quel carte il veut jouer
            choix_carte=self.__choix_carte_act(plateau)
            
            #On demande au joueur ou il veut poser sa carte
            pos=self.__choix_pos(plateau)
              
            #La carte est placee sur le plateau et le joueur pioche une nouvelle carte
            plateau.add_carte(choix_carte,pos)
            self.hand.remove_card(choix_carte)
            self.piocher_carte(pioche)

        if choix_action == 2:

            #On demande au joueur quelle carte il veut se defausser
            choix_carte=self.__choix_carte_rem(plateau)

            #La carte est retire de la main du joueur et place dans la defausse et la joueur pioche une nouvelle carte
            defausse.append(choix_carte)
            self.defausse_carte(choix_carte, defausse)
            self.piocher_carte(pioche)


    # @property
    # def name(self):
    #     return self.name

    # @property
    # def role(self):
    #     return self.role

    # @property
    # def hand(self):
    #     return self.hand

    # @hand.setter
    # def hand(self,hand):
    #     self.hand=hand




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
