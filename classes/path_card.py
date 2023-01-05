import numpy as np
import random
import os
from .card import Carte
import sys


class Path_card(Carte):
    """Cartes chemin du jeu SABOOTERS
    • Type 0 : Carte chemin
    • Type 3 : Carte start
    • Type 4 : Carte gold
    • Type 5 : Carte pierre"""

    def __init__(self, typ):
        super().__init__(typ)

        #We define a default direction for the card
        self.__sens=0 #The attribute is private because we want to control its modification

        # Appearance is randomly drawn on the card according to its type
        if typ == 0:  # Path Map
            chemin = np.random.choice(np.array([0, 1, 2, 3, 4, 5, 6, 7]))
            self.__vectapparence = Carte.matchemin[chemin]
            self.__vectrecto = Carte.matrecto[0]
            self.__path = Carte.matpath[chemin]
        elif typ == 3:
            # Map start
            self.__vectapparence = Carte.matchemin[8]
            self.__vectrecto = Carte.matrecto[0]
            self.__path = Carte.matpath[8]
        elif typ == 4:
            # Gold card
            self.__vectapparence = Carte.matchemin[9]
            self.__vectrecto = Carte.matrecto[1]
            self.__path = Carte.matpath[9]
        elif typ == 5:
            # Stone card
            self.__vectapparence = Carte.matchemin[10]
            self.__vectrecto = Carte.matrecto[1]
            self.__path = Carte.matpath[10]
        else:
            print("Error: the value of the card type is incorrect, initialization by default of a path card")
            a = input("press any bouton to continue")
            # Path Map
            chemin = np.random.choice(np.array([0, 1, 2, 3, 4, 5, 6, 7]))
            self.__vectapparence = Carte.matchemin[chemin]
            self.__vectrecto = Carte.matrecto[0]
            self.__path = Carte.matpath[chemin]

    def part_st(self, x):
        """Method to display a part of the map"""
        # Display the part of the map you want to see
        if self.face == 1:
            if x == 0:
                return Carte.tablechemin[self.__vectapparence[self.__sens][0]]
            elif x == 1:
                return Carte.tablechemin[self.__vectapparence[self.__sens][1]]
            elif x == 2:
                return Carte.tablechemin[self.__vectapparence[self.__sens][2]]
            else:
                print("Error: the display value of the card is incorrect, please choose a value between 0 and 2")
                sys.exit()

        if self.face == 0:
            if x == 0:
                return Carte.tablerecto[self.__vectrecto[0]]
            elif x == 1:
                return Carte.tablerecto[self.__vectrecto[1]]
            elif x == 2:
                return Carte.tablerecto[self.__vectrecto[2]]
            else:
                print("Error: the display value of the card is incorrect, please choose a value between 0 and 2")
                sys.exit()

    def __str__(self):
        """Function toString"""
        st = Carte.tablechemin[self.__vectapparence[self.__sens][0]] + "\n" + Carte.tablechemin[self.__vectapparence[self.__sens][1]] + "\n" + \
             Carte.tablechemin[self.__vectapparence[self.__sens][2]]
        return st

    # Fonction de comparaison
    def __eq__(self, other):

        if not isinstance(other, Path_card):
            return False

        if self is other:
            return True

        if self.typ != other.typ or self.__vectapparence != other.vectapparence:
            # The other attributes are not tested because they do not determine the nature of the card
            return False

        return True

    @property
    def vectapparence(self):
        return self.__vectapparence

    @property
    def sens(self) : return self.__sens
    @sens.setter
    def sens(self,sens):
        if sens == 1:
            self.__sens=sens
        #On défini un sens par default à la carte
        else:
            self.__sens=0

    @property
    def vectrecto(self):
        return self.__vectrecto

    @property
    def path(self):
        return self.__path
