import sys
sys.path.insert(0,"../PROJETPYTHON")
import classes as sb 

import numpy as np


class SABOOTERS(object):
    def __init__(self):
        self.__menu=me.Menu()
        self.__deck=[]
        self.__joueurs=[]
        self.__plateau=m.Plateau()

    def initpartie(self):
        self.__menu.start_game()


