import numpy as np
import random
from abc import ABC, abstractmethod
import os
from .hand import Hand
from .card import Card
from .board import Board
import sys



class Player(ABC):
    def __init__(self,name, role, nb_players):
        self.__name = name
        self.__role = role    # the role is of the class menu.character[i]
        self.__hand = Hand(nb_players)   # to display the hand: player.hand.display_hand()

    def pick_card(self, pioche):
        """Method that allows the player to draw a card"""
        if len(pioche) <= 0:
            print("Error: the deck is empty")
            sys.exit()
        
        self.__hand.add_card(pioche[0])
        pioche.remove(pioche[0])

    def defausse_card(self, card, defausse):
        """Method to remove a card from the player"""
        defausse.append(card)
        self.__hand.remove_card(card)

    # Abstract method that allows a human or an AI to play during a round
    @abstractmethod
    def player_turn(self, Board, pioche, defausse): pass


    @property
    def name(self):
        return self.__name

    @property
    def role(self):
        return self.__role

    @role.setter
    def role(self,role):
        if role == "S":
            self.__role = role
        # Define by default "C" as a role
        else:
            self.__role = "C"


    @property
    def hand(self):
        return self.__hand

