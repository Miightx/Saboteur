import numpy as np
import random





class Menu(object):

    def __init__(self):  # Property
        self.__number = 0
        self.__players_name = []
        self.__bot = []
        self.__roles = []
    
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
                    self.__number=int(self.__number)
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
import numpy as np

class fin_manche():
#count_winner et winner sont privés
    def __init__(self,score_manche, s_count, c_count,sharing_gold):
        self.__score_manche = score_manche
        self.__s_count = s_count
        self.__c_count= c_count
        self.__spm = []   #score par manche
        self.sharing_gold = [] #Distribution score dans le cas où les mineurs gagnent peut etre a enlever

#Calcul du nombre de personnes qui ont gagné la manche
    def count_winner(self, s_count, c_count):
        for k in range (len(self.roles)):
            if (self.roles[k]=='S'):
                s_count += 1
            elif (self.roles[k]=='C'):
                c_count += 1
                score_manche = np.array(len(self.players), 3)


    def winner(self,c_count, s_count, score_manche,sharing_gold):
        s_state = False
        c_state = False
        etat = False
        score_manche = np.zeros(len(self.players))
        if (s_state == True): #Disons que c'est le cas où les saboteurs ont gagnés
            print('Saboteurs won this game')
            print('')
            for k in range (len(self.joueur)):
                if (s_count == 1):
                    if (self.roles[k] == 'S'):
                        score_manche[k]== 4
                elif(s_count == 2 or s_count == 3):
                    if (self.roles[k] == 'S'):
                        score_manche[k]== 3
        elif (c_state == True):
            print('Diggers won this game')
            for k in range(len(self.joueurs)):
                sharing_gold[k] = np.randint(1,3)
                if (self.roles[k]=='C'):
                    while (len(sharing_gold)!=0):
                        indice = 0
                        while (indice < c_count):
                            print("It is the remain gold cards")
                            print(sharing_gold)
                            print("To {0} to choose the card he/she wishes")
                            while (etat == False):
                                print("Please choose a value between 1 and",len(self.joueurs), end='')
                                choice = input()
                                if (self.__choice.isdecimal() == True):
                                    self.__choice = int(self.__choice)
                                    if (self.__choice >0 or self.__choice < len(self.__sharing_gold)):
                                        print("Please choose another value")
                                        etat = True
                                    else:
                                        print("Please choose another value")
                            score[indice] += sharing_gold[choice]
                            sharing_gold.pop(choice)
                            print("{0} choose", sharing_gold[choice])
                            indice += 1

            print("Voici la valeur des cartes or")
            print(sharing_gold)

                    #creation de self.number cartes d'or valant entre 1 et 3
                    #joueur choisit la carte
class fin_de_partie():
    def __init__(self, score):
        self.__score = score

    def calcul_point(self, spm):
        for i in range(len(self.__menu.joueurs)):
            score = self.__spm[0]+self.__spm[1]+self.__spm[2]

@property
def game_start(self):
    return self.aff_wel(), self.get_number(), self.players(), self.affichage_debut_fin()

    


