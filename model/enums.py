from enum import Enum


class FrenchSuits(Enum):
    """French suited cards use clubs, diamonds, hearts, and spades suits"""
    clubs = 'Clubs'
    diamonds = 'Diamonds'
    hearts = 'Hearts'
    spades = 'Spades'


class GermanSuits(Enum):
    """German suited cards use acorns, leaves, hearts, and bells suits"""

    acorns = 'Acorns'
    leaves = 'Leaves'
    hearts = 'Hearts'
    bells = 'Bells'


class LatinSuits(Enum):
    """Latin suited cards use swords, cups, coins, and clubs suits"""
    swords = 'Swords'
    cups = 'Cups'
    coins = 'Coins'
    clubs = 'Clubs'


class FrenchCards(Enum):
    """These enums are to associate standard string values with
    the card types. The value rankings of the card are not given here,
    but at the Deck level, because some decks may rank cards differently.
    For instance, Ace high or jokers are wild"""
    one = 'One'
    two = 'Two'
    three = 'Three'
    four = 'Four'
    five = 'Five'
    six = 'Six'
    seven = 'Seven'
    eight = 'Eight'
    nine = 'Nine'
    ten = 'Ten'
    jack = 'Jack'
    queen = 'Queen'
    king = 'King'
    joker = "Joker"
