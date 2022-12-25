import random
import numpy as np
class Menu(object):
    def __init__(self, state):  # Property
        self.__number = 0
        self.__players_name = []
        self.__bot = []
        self.__roles = []
        self.__count = []
        self.__state = state
        self.__sharing_gold = []
        self.__spm = []
    #Methodes
    def __aff_wel(self):  # Affichage du début
        print("+--------------------------------------------------------------------+")
        print("| Welcome to SabOOtters, where dwarf otters look for gold in a mine! |")
        print("+--------------------------------------------------------------------+")

    def __get_number(self):  # Nombre de joueurs
        print("How many players?")
        etat = False
        while (etat == False):
            self.__number = input()
            if (len(self.__number)==1 or len(self.__number)==2):
                if (self.__number.isdecimal()==True):
                    self.__number = int(self.__number)
                    if (self.__number > 2 and self.__number < 11):
                        print("There is", self.__number, "players")
                        etat = True
                    else:
                        print("Please choose a number between 3 and 10")
                else:
                    print('Please write a correct number')
            else:
                print('Please write a number')


    def __players(self):  # Configuration des joueurs
        for k in range(self.__number):
            print('Please enter the name of player', k + 1 )
            print('')
            joueur = 0
            joueur = input()
            self.__players_name.append(joueur)
            print('The name of the player is:', self.__players_name[k])
            print('Please press 0 if the player is an AI and press 1 if the player is an Human')
            etat = False
            bot = []
            while (etat == False):
                bot = input()
                if (bot == '1'):
                    self.__bot.append("Human")
                    etat = True

                elif (bot == '0'):
                    self.__bot.append("AI")
                    etat = True
                else:
                    print("Please select 0 (AI) or 1 (Human):")
                    etat = False

    def __cartes_roles(self):  # Saboteur or Digger
        personnage=[]
        if (self.__number == 3):
            personnage = ['S', 'C', 'C', 'C']
            self.__roles = random.sample(personnage, 3)
        elif (self.__number == 4):
            personnage = ['S', 'C', 'C', 'C', 'C']
            self.__roles = random.sample(personnage, 4)
        elif (self.__number == 5):
            personnage = ['S', 'S', 'C', 'C', 'C', 'C']
            self.__roles = random.sample(personnage, 5)
        elif (self.__number == 6):
            personnage = ['S', 'S', 'C', 'C', 'C', 'C']
            self.__roles = random.sample(personnage, 6)
        elif (self.__number == 7):
            personnage = ['S', 'S', 'S', 'C', 'C', 'C', 'C', 'C']
            self.__roles = random.sample(personnage, 7)
        elif (self.__number == 8):
            personnage = ['S', 'S', 'S', 'C', 'C', 'C', 'C', 'C', 'C']
            self.__roles = random.sample(personnage, 8)
        elif (self.__number == 9):
            personnage = ['S', 'S', 'S', 'C', 'C', 'C', 'C', 'C', 'C', 'C']
            self.__roles = random.sample(personnage, 9)
        elif (self.__number == 10):
            personnage = ['S', 'S', 'S', 'S', 'C', 'C', 'C', 'C', 'C', 'C', 'C']
            self.__roles = random.sample(personnage, 10)

    def __affichage_debut_fin(self):
        total=[]
        for k in range (self.__number-1):
            total.append(self.__players_name[k] + '(' + self.__bot[k]+'),')
        total.append(self.__players_name[self.__number-1] + '(' + self.__bot[self.__number-1]+')')
        total = ' '.join(total)
        print('---------------------')
        print('The', self.__number, 'players are:', total)

    def start_game(self):
        self.__aff_wel() 
        self.__get_number() 
        self.__players() 
        self.__cartes_roles()
        self.__affichage_debut_fin()

    @property
    def number(self):
        return self.__number

    @property
    def players_name(self):
        return self.__players_name

    @property
    def bot(self):
        return self.__bot

    @property
    def roles(self):
        return self.__roles
    @property
    def count(self):
        return self.__count
    @count.setter
    def count(self,count):
        self.__count = count
    @property
    def game_start(self):
        return self.__aff_wel(), self.__get_number(), self.__players(), self.__affichage_debut_fin()
    def count_winner(self):
        for k in range (len(self.roles)):   #Pour chaque roles je compte le nb de joueurs ayant ce role
            if (self.roles[k]=='S'):
                self.__count[0] += 1
            elif (self.roles[k]=='C'):
                self.__count[1] += 1

    def winner(self, count):
        etat = False
        score_manche = np.zeros(self.__number)
        if (self.__state == 1): #Disons que c'est le cas où les saboteurs ont gagnés == 1
            print('Saboteurs won this game')
            print('')
            for k in range (self.__number):
                if (self.__count[0] == 1):
                    if (self.__roles[k] == 'S'):  #Un sabotteur, il obtient 4 pts
                        score_manche[k]= 4
                elif(self.__count[0] == 2 or self.__count[0] == 3): #2 ou 3 ils obtiennent 3 pts
                    if (self.__roles[k] == 'S'):
                        score_manche[k]= 3
        elif (self.__state == 2):     #Cas ou Mineurs gagnent == 2
            print('Diggers won this game')
            for k in range(self.__number):
                self.__sharing_gold[k] = np.randint(1,3)    #Cartes or valeur entre 1 et 3
                if (self.__roles[k]=='C'):                    #Personnes étant Mineur
                    while (len(self.__sharing_gold)!=0):    #Jusqu'a quand y'a plus de pts a distribuer
                        indice = 0
                        while (indice < count[1]):          #Addition des pts des mineurs quand il y a plus de cartes or que de mineurs
                            print("It is the remain gold cards")
                            print(self.__sharing_gold)
                            print("To {0} to choose the card he/she wishes")
                            while (etat == False):          #Choix de la carte d'or
                                print(f"Please choose a value between 1 and {self.__number}")
                                self.__choice = input()
                                if (self.__choice.isdecimal() == True):
                                    self.__choice = int(self.__choice)
                                    if (self.__choice >0 or self.__choice < len(self.__sharing_gold)):
                                        print("Please choose another value")
                                        etat = True
                                    else:
                                        print("Please choose another value")
                            self.__spm[indice] += self.__sharing_gold[self.__choice]      #Stockage des scores pour calcuer en fin de partie
                            self.__sharing_gold.pop(self.__choice)                      #Enlever la carte d'or choisit
                            print("{0} choose", self.__sharing_gold[self.__choice])
                            indice += 1

            print("Voici la valeur des cartes or")
            print(self.__sharing_gold)

    def calcul_point(self):  # Comptage des pts de chaque manche
        for i in range(self.__number):
            self.__score = self.__spm[0] + self.__spm[1] + self.__spm[2]
        print(f' Le score final est de {self.__score}')
    def fin_manche(self,count,state):
        self.count_winner()
        self.winner(count)
    def fin_de_partie(self):
        return self.calcul_point()

    @property
    def score(self):
        return self.__score
    @property
    def state(self):
        return self.__state

    @property
    def spm(self):
        return self.__spm