from enum import *
from collections import deque
import random


class Suit(IntEnum):
    Club = auto()
    Diamond = auto()
    Heart = auto()
    Spade = auto()

    @staticmethod
    def from_symbol(s):
        if s == 'C' or s == 'c':
            return Suit.Club
        elif s == 'D' or s == 'd':
            return Suit.Diamond
        elif s == 'H' or s == 'h':
            return Suit.Heart
        elif s == 'S' or s == 's':
            return Suit.Spade
        else:
            raise KeyError('Unknown suit {0}'.format(s))


class Rank(IntEnum):
    Ace = 1
    Two = 2
    Three = 3
    Four = 4
    Five = 5
    Six = 6
    Seven = 7
    Eight = 8
    Nine = 9
    Ten = 10
    Jack = 11
    Queen = 12
    King = 13

    @staticmethod
    def from_symbol(s):
        if s == 'A':
            return Rank.Ace
        elif s == 'T':
            return Rank.Ten
        elif s == 'J':
            return Rank.Jack
        elif s == 'Q':
            return Rank.Queen
        elif s == 'K':
            return Rank.King
        else:
            return Rank(int(s))

    def __str__(self):
        return ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A'][self.value - 1]


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __repr__(self):
        return '{0}{1}'.format(str(self.rank), self.suit.name)

    def __le__(self, other):
        return self.rank <= other.rank

    def __lt__(self, other):
        return self.rank < other.rank

    def __ge__(self, other):
        return not(self < other)

    def __gt__(self, other):
        return not(self <= other)

    def __eq__(self, other):
        return self.rank == other.rank and self.suit == other.suit

    @classmethod
    def from_symbol(cls, s):
        r = Rank.from_symbol(s[0])
        s = Suit.from_symbol(s[1])
        return cls(r, s)

    @staticmethod
    def deck():
        return deque(Card(r, s) for s in Suit for r in Rank)

    @staticmethod
    def shuffled_deck(seed=None):
        deck = Card.deck()
        if seed is not None:
            random.seed(seed)
        random.shuffle(deck)
        return deck
