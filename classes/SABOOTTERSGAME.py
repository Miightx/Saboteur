import sys
sys.path.insert(0,"../PROJETPYTHON")
import classes.classes as sb 

import numpy as np


class SABOOTERS(object):
    def __init__(self):
        self.__menu=sb.Menu()
        self.__deck=[]
        self.__joueurs=[]
        self.__plateau=sb.Plateau()

    def initpartie(self):
        self.__menu.start_game()


