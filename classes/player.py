import sys
sys.path.insert(0,"../PROJETPYTHON")
import classes.hand as sb

class Player:
    def __init__(self,name,role, nb_players):
        self.name = name
        self.role = role    #le role c'est de la classe menu.personnage[i]
        self.hand = sb.Hand(nb_players) #pour afficher la main: player.hand.display_hand()




"""
• à 3 joueurs : 1 Saboteur et 3 Chercheurs
• à 4 joueurs : 1 Saboteur et 4 Chercheurs
• à 5 joueurs : 2 Saboteurs et 4 Chercheurs
• à 6 joueurs : 2 Saboteurs et 5 Chercheurs
• à 7 joueurs : 3 Saboteurs et 5 Chercheurs
• à 8 joueurs : 3 Saboteurs et 6 Chercheurs
• à 9 joueurs : 3 Saboteurs et 7 Chercheurs
• à 10 joueurs : toutes les cartes Rôle (4 Saboteurs et 7 Chercheurs)
"""