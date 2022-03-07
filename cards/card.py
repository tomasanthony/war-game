from model.enums import Enum


class Card:
    """Cards have a suit and a rank that change based on the
    type of suited playing cards are in use. Because cards do not have
    any variability here, there is no abstraction."""

    def __init__(self, suit: Enum, rank: int):
        self.suit = suit
        self.rank = rank

    def __eq__(self, compared) -> bool:
        """Enable more robust comparison between cards"""
        return self.suit == compared.suit and self.rank == compared.rank
