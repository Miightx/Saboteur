from random import randint
class Player:
    def __init__(self,name, role, hand):
        self.name = name
        self.role = role
        self.hand = hand
        
    def attrib_role(nb_joueur):
        rolej = []
        if nb_joueur < 3:
            print("entrez ")
            for i in range(nb_joueur-1):
                a = randint(0,1)
        



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