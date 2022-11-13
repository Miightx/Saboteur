class Hand:
    def __init__(self, nb_players):
        self.cards = []
        if nb_players <= 5:
            self.hand_size = 6
        elif nb_players <= 7:
            self.hand_size = 5
        else:
            self.hand_size = 4

    def display_hand(self):
        for i in range(len(self.cards)):
            print(self.cards[i], end=" ")
    
    def add_card(self, card):
        if len(self.cards)==self.hand_size:
            return
        self.cards.append(card)