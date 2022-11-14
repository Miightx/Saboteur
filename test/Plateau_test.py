import sys
sys.path.insert(0,"../PROJETPYTHON")
import classes.map as sb
import numpy as np
import fonc_affichage as aff



deck=[]
deck.append(sb.Carte(0))
deck.append(sb.Carte(0))
deck[0].etat=1
deck[1].etat=1
deck[1].pos=[3,6]

deck[0].face=1
deck[1].face=1

plateau=sb.Plateau()
plateau.maj_cartes_posees(deck)

plateau.affiche()




