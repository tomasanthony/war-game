from enum import Enum
from typing import Type


class Card:
    """Cards have a suit and a rank that change based on the
    type of suited playing cards are in use. Because cards do not have
    any variability here, there is no abstraction."""

    def __init__(self, suit, pip_or_face, rank: int):
        self.suit = suit
        self.pip_or_face = pip_or_face
        self.rank = rank

    def __eq__(self, other):
        """Enable more robust comparison between cards"""
        return self.suit == other.suit and self.rank == other.rank
