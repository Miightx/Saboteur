import sys
sys.path.insert(0,"../PROJETPYTHON")
import classes.hand as sb
import classes.map as sb
import classes.menu as sb
import classes.player as sb
import numpy as np


class SABOOTERS(object):
    def __init__(self):
        self.__menu=sb.Menu()
        self.__deck=[]
        self.__joueurs=[]
        self.__plateau=Plateau()

    def initpartie(self):
        self.menu.start_game()


