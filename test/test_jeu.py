import sys
sys.path.insert(0,"../PROJETPYTHON")
from classes.deck import Deck
from classes.menu import Menu
from classes.player import Player
from classes.hand import Hand

from classes.mapp import Carte
from classes.mapp import Plateau
from classes.SABOOTTERSGAME import SABOOTERS



jeu=SABOOTERS()
jeu.initpartie()

jeu.initmanche()
jeu.tour_pour_rien()
