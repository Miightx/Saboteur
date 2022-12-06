import numpy as np

class fin_manche(object):
#count_winner et winner sont privés
    def __init__(self,roles,players, s_count, c_count,sharing_gold,count):
        self.roles = roles    #Les roles ce sont de la classe menu.personnage[i]
        self.players = players    #Les roles ce sont de la classe menu.personnage[i]
        self.__score_manche = []
        self.__s_count = s_count
        self.__c_count= c_count
        self.spm = []   #score par manche
        self.__sharing_gold = sharing_gold #Distribution score dans le cas où les mineurs gagnent peut etre a enlever
        self.__count= count

#Calcul du nombre de personnes qui ont gagné la manche
    def __count_winner(self):
        for k in range (len(self.roles)):   #Pour chaque roles je compte le nb de joueurs ayant ce role
            if (self.roles[k]=='S'):
                self.__s_count += 1
            elif (self.roles[k]=='C'):
                self.__c_count += 1

    def roles_count(self):
        count=[self.__s_count, self.__c_count]
    def __winner(self):
        etat = False
        score_manche = np.zeros(len(self.players))
        if (s_state == True): #Disons que c'est le cas où les saboteurs ont gagnés
            print('Saboteurs won this game')
            print('')
            for k in range (len(self.players)):
                if (count[0] == 1):
                    if (self.roles[k] == 'S'):  #Un sabotteur, il obtient 4 pts
                        score_manche[k]= 4
                elif(count[0] == 2 or count[0] == 3): #2 ou 3 ils obtiennent 3 pts
                    if (self.roles[k] == 'S'):
                        score_manche[k]= 3
        elif (c_state == True):     #Cas ou Mineurs gagnent
            print('Diggers won this game')
            for k in range(len(self.players)):
                self.__sharing_gold[k] = np.randint(1,3)    #Cartes or valeur entre 1 et 3
                if (self.roles[k]=='C'):                    #Personnes étant Mineur
                    while (len(self.__sharing_gold)!=0):    #Jusqu'a quand y'a plus de pts a distribuer
                        indice = 0
                        while (indice < count[1]):          #Addition des pts des mineurs quand il y a plus de cartes or que de mineurs
                            print("It is the remain gold cards")
                            print(self.__sharing_gold)
                            print("To {0} to choose the card he/she wishes")
                            while (etat == False):          #Choix de la carte d'or
                                print("Please choose a value between 1 and",len(self.players), end='')
                                self.__choice = input()
                                if (self.__choice.isdecimal() == True):
                                    self.__choice = int(self.__choice)
                                    if (self.__choice >0 or self.__choice < len(self.__sharing_gold)):
                                        print("Please choose another value")
                                        etat = True
                                    else:
                                        print("Please choose another value")
                            self.spm[indice] += self.__sharing_gold[self.__choice]      #Stockage des scores pour calcuer en fin de partie
                            self.__sharing_gold.pop(self.__choice)                      #Enlever la carte d'or choisit
                            print("{0} choose", self.__sharing_gold[self.__choice])
                            indice += 1

            print("Voici la valeur des cartes or")
            print(sharing_gold)

    def finito(self):
        self.__count_winner()
        self.__winner()


@property
def finito(self):
    return self.score_manche(), self.winner()


class fin_de_partie():
    def __init__(self, score,players, spm):
        self.__score = score
        self.__players = players
        self.spm = spm
    def __calcul_point(self, players,spm):      #Comptage des pts de chaque manche
        for i in range(len(self.__players)):
            self.__score = self.spm[0] + self.spm[1] + self.spm[2]
    @property
    def score(self):
        return self.__score





