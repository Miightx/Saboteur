class Hand:
    def __init__(self, nb_players):
        self.cards = []
        if nb_players <= 5:
            self.hand_size = 6
        elif nb_players <= 7:
            self.hand_size = 5
        else:
            self.hand_size = 4

    def display_hand(self): #montrer la main
        for i in range(len(self.cards)):
            print(self.cards[i], end=" ")
    
    def add_card(self, card): #ajouter une carte
        if len(self.cards)==self.hand_size:
            return
        self.cards.append(card)

    def remove_card(self, card): #enlever une carte
        self.cards.remove(card)
    
    def use_card(self, card): #utiiliser une carte
        self.remove_card(card)
        #card.use()        