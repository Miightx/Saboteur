import numpy as np
import random
import os
from abc import ABC, abstractmethod


class Carte(ABC):
    """Carte du jeu SABOOTERS
    • Type 0 : Carte chemin
    • Type 1 : Carte action
    • Type 2 : Carte map
    • Type 3 : Carte start
    • Type 4 : Carte gold
    • Type 5 : Carte pierre 
    • Type 6 : Carte éboulement """
    # Board containing the content of the cards
    #                  0         1         2         3         4         5         6         7         8         9         10        11
    tablechemin=[('(   )'), ('( | )'), ('(---)'), ('( x )'), ('(-x )'), ('( x-)'), ('(-+ )'), ('( +-)'), ('(-+-)'),('(-S-)'), ('($$$)'), ('(-N-)')]
    tableaction=[('(   )'), ('(XXX)'), ('(REP)'), ('(BRK)'), ('( P )'), ('( L )'), ('( W )'), ('( M )'), ('(MAP)')]
    tablerecto=[('(   )'), ('(+++)'), ('(+S+)'), ('(END)')]

    # Matrices containing vectors to assign an appearance to each type of card
    matchemin = [[1, 1, 1], [0, 2, 0], [1, 3, 0], [0, 3, 1], [0, 4, 0], [0, 5, 0], [1, 8, 1], [1, 6, 1], [0, 6, 1],
                 [1, 6, 0], [1, 7, 1], [0, 7, 1], [1, 7, 0], [1, 8, 1], [1, 9, 1], [10, 10, 10], [1, 11, 1]]
    mataction = [[1, 1, 1], [2, 4, 0], [2, 5, 0], [2, 6, 0], [2, 4, 5], [2, 4, 6], [2, 5, 6], [3, 4, 0], [3, 5, 0],
                 [3, 6, 0], [3, 4, 5], [3, 4, 6], [3, 5, 6], [7, 8, 4]]
    matrecto = [[1, 2, 1], [0, 3, 0]]

    # Matrices containing path vectors assigned to path cards [value indicating the presence of a card, top, left, right, bottom].
    # 0           1           2            3          4           5           6           7           8           9           10          11          12          13          14          15          16

    matpath = [[1, 1, 0, 0, 1], [1, 0, 1, 1, 0], [1, 1, 0, 0, 0], [1, 0, 0, 0, 1], [1, 0, 1, 0, 0], [1, 0, 0, 1, 0],
               [1, 1, 1, 1, 1], [1, 1, 1, 0, 1], [1, 0, 1, 0, 1], [1, 1, 1, 0, 0], [1, 1, 0, 1, 1], [1, 0, 0, 1, 1],
               [1, 1, 0, 1, 0], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]

    def __init__(self, typ):
        # Define a position by default
        self.pos = [0, 0]
        # Define the type of card
        self.__typ = typ

        # Define by default that the card is face down
        self.face = 0

    @abstractmethod
    def affiche(self, x): pass

    @abstractmethod
    def part_st(self, x): pass

    @property
    def typ(self): return self.__typ

    @property
    def face(self): return self.__face

    @face.setter
    def face(self, face):
        self.__face = 0
        if 0 <= face <= 1:
            self.__face = face
