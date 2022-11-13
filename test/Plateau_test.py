import class.map as sb
import numpy as np
import fonc_affichage as aff



deck=[]
deck.append(sb.Carte(0))
deck.append(sb.Carte(0))
deck[0].etat=1
deck[1].etat=1
deck[1].pos=[3,6]



plateau=sb.Plateau()
plateau.maj_cartes_posees(deck)

plateau.affiche()




