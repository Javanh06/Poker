"""
Module for playing cards, with classes Card and Deck
"""

import random

class Card(object):
    """ A card object with a suit, rank, and file name.
    The file name refers to the card's image on disk."""

    RANKS = tuple(range(1, 14))

    SUITS = ('Spades', 'Hearts', 'Diamonds', 'Clubs')

    def __init__(self, rank, suit):
        """Creates a card with the given rank and suit."""
        if not (rank in Card.RANKS):
            raise RuntimeError('Rank must be in ' + str(Card.RANKS))
        if not (suit in Card.SUITS):
            raise RuntimeError('Suit must be in ' + str(Card.SUITS))
        self.rank = rank
        self.suit = suit

    def __str__(self):
        """Returns the string representation of a card."""
        if self.rank == 1:
            rank = 'Ace'
        elif self.rank == 11:
            rank = 'Jack'
        elif self.rank == 12:
            rank = 'Queen'
        elif self.rank == 13:
            rank = 'King'
        else:
            rank = self.rank
        return str(rank) + ' of ' + self.suit
     
    def __lt__(self, other):
        if type(other)==Card:
            if self.rank==1 or other.rank==1:
                if self.rank != 1:
                    return True
                return False
            return self.rank < other.rank
                
    def __eq__(self,other):
        if self is other:
            return True
        if type(other)!=Card:
            return False
        if self.rank == other.rank:
            return True
        else:
            return False
    
    def get_file_name(self):
        """
        This function returns the filename for the card's image
        """
        st = str(self).lower()
        st = st.split(" of ")
        st = st[1] + "_" + st[0] + ".png"
        return st

## The definition of class Deck
class Deck(object):
    def __init__(self):
        self.cards = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.cards.append(Card(rank, suit))

    def order(self, rev=False):
        self.cards.sort(reverse=rev)

    def __len__(self):
        return len(self.cards)

    def isEmpty(self):
        return len(self.cards) == 0

    def deal(self):
        return self.cards.pop()

    def shuffle(self):
        random.shuffle(self.cards)
