import numpy as np
import random



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
    

    @property
    def hand_size(self):
        return self.__hand_size

    @property
    def cards(self):
        return self.__cards

    @cards.setter
    def cards(self,cards):
        self.__cards=cards   