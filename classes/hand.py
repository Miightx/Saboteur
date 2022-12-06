import numpy as np
import random
import sys
from .card import Carte



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
            for i in range(2*len(self.__cards)):
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
        if not isinstance ( card , Carte ) :
            print("Erreur: uniquement des cartes peuvent être ajouté à la main d'un joueur")
            sys.exit()
        if len(self.__cards)==self.__hand_size:
            return
        card.face=1
        self.__cards.append(card)

    def remove_card(self, card): #enlever une carte
        if not isinstance ( card , Carte ) :
            print("Erreur: uniquement des cartes peuvent être retiré de la main d'un joueur")
            sys.exit()
        self.__cards.remove(card)
    

    @property
    def hand_size(self):
        return self.__hand_size

    @property
    def cards(self):
        return self.__cards

    # @cards.setter
    # def cards(self,cards):
    #     self.__cards=cards   