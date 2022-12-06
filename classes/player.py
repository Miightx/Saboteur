import numpy as np
import random
import os
from .hand import Hand
from .card import Carte
from .board import Plateau
import sys



class Player(object):
    def __init__(self,name,role,nb_players):
        self.__name = name
        self.__role = role    #le role c'est de la classe menu.personnage[i]
        self.__hand = Hand(nb_players) #pour afficher la main: player.hand.display_hand()

    def piocher_carte(self,pioche):
        if len(pioche)<=0:
            print("Erreur: la pioche est vide")
            sys.exit()
        
        self.__hand.add_card(pioche[0])
        pioche.remove(pioche[0])

    def choix_action(self,plateau):

        if not isinstance ( plateau , Plateau ) :
            print("Erreur: uniquement des cartes peuvent être ajouté à la main d'un joueur")
            sys.exit()

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
        return choix_action

    def choix_carte_act(self,plateau):

        #On demande au joueur quel carte il veut jouer
        no_carte=int(input("What card would you like to play (1 to {0})?".format(self.__hand.hand_size)))-1

        #On s'assure que le joueur choisisse une de ses cartes
        while no_carte < 0 or no_carte > self.__hand.hand_size-1:
            print("Please, do not steal a card from your neighbour!")
            no_carte=int(input("What card would you like to play (1 to {0})?".format(self.__hand.hand_size)))-1

        #On recupere la carte que le joueur a choisi
        choix_carte=self.__hand.cards[no_carte]

        return choix_carte

    def choix_carte_rem(self,plateau):
        #On demande au joueur quelle carte il veut se defausser
        no_carte=int(input("Which card do you want to throw away (1 to {0})?".format(self.__hand.hand_size)))-1

        #On s'assure que le joueur choisisse une de ses cartes
        while no_carte < 0 or no_carte > self.__hand.hand_size-1:
            print("Please, don't steal a card from your neighbour!")
            no_carte=int(input("What card would you like to play (1 to {0})?".format(self.__hand.hand_size)))-1
                
        choix_carte=self.__hand.cards[no_carte]

        return choix_carte
    
    def choix_pos(self,plateau):
        pos=[]
        pos.append(int(input("Where do you want to place your card (x value)?")))
        pos.append(int(input("(y value)?")))
            
        #On s'assure que le joueur pose bien la carte sur le plateau
        while pos[0] < -10 or pos[0] > 10 or pos[1] < -10 or pos[1] >10 :
            print("Please place the card on the board (-10<=x<=10) (-10<=y<=10)")
            pos=[]
            pos.append(int(input("Where do you want to place your card (x value)?")))
            pos.append(int(input("(y value)?")))
        return pos


    @property
    def name(self):
        return self.__name

    @property
    def role(self):
        return self.__role

    @property
    def hand(self):
        return self.__hand

    # @hand.setter
    # def hand(self,hand):
    #     self.__hand=hand




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
