from abc import ABC, abstractmethod
from card import Card
import random

from model.enums import FrenchSuits, FrenchCards
from model.exceptions import CheatingError, InvalidDeckError


class Deck(ABC):
    """Abstract class for a deck of playing cards. Variation exists
    within playing card deck size, suits, and cards. Default methods
    are provided for deck shuffling, drawing, and inserting. Subclasses can
    override these functions depending on the game."""

    @abstractmethod
    def __init__(self, deck_size: int):
        self.rankings = self.__build_rankings()
        self.cards = self.__build_deck()
        self.deck_size = deck_size
        self.missing_cards = []
        if not self.validate_deck_composition():
            raise InvalidDeckError

    @abstractmethod
    def __build_deck(self) -> list[Card]:
        """Decks are not consistently built the same way, so this function does not have a parent implementation"""
        pass

    def __build_rankings(self) -> dict:
        """Decks rankings vary, so this function does not have a parent implementation"""

        pass

    def draw_card(self, draw_random: bool = False) -> Card:
        """Draw a card from the deck, either the card at the top
        of the deck or a random card. Deletes the card from the deck because it is no
        longer in the deck, it is in a hand. We add the card to a list of missing cards,
        in order to prevent 'cheating' by validating a returned card is in this list.
        The end of the card list is treated as the top of the deck - a LIFO stack.

        Args:
            draw_random (bool): whether to draw a card randomly from the deck

        Returns:
            (Card) : returns a single card from the deck of cards
            """
        if draw_random:
            index = random.randrange(len(self.cards))
            card = self.cards.pop(index)
            self.missing_cards.append(card)
            return card
        else:
            card = self.cards.pop()
            self.missing_cards.append(card)
            return card

    def insert_card(self, card: Card, insert_random: bool = False) -> bool:
        """Insert a card back into the deck. Validating it is a card that is
        missing from the deck and in a hand. Inserts randomly or at the top of
        the deck (appended to the list).

        Args:
            insert_random (bool): whether to insert a card randomly into the deck
            card (Card): a card to insert into the deck

        Returns:
            bool : returns a single card from the deck of cards
            """
        if card not in self.missing_cards:
            raise CheatingError

        elif insert_random:
            index = random.randrange(len(self.cards))
            self.cards.insert(index, card)
            return True
        else:
            card = self.cards.pop()
            self.missing_cards.append(card)
            self.cards.append(card)
            return True

    def shuffle_cards(self):
        """Randomly shuffles the deck of cards in place"""
        random.shuffle(self.cards)

    def validate_deck_composition(self) -> bool:
        """A deck needs to divide its size evenly across suits and their card types"""
        return self.deck_size / len(FrenchSuits) == len(FrenchCards)


class StandardFrenchDeck(Deck):
    """Standard French Deck"""

    def __init__(self, deck_size=52):
        super().__init__(deck_size=deck_size)

    def __build_deck(self) -> list[Card]:
        """Building a deck based on the size of the deck, the types of cards, and the suits.
        The"""
        cards = []
        for suit in FrenchSuits:
            for card in FrenchCards:
                cards.append(Card(suit, self.rankings[card.value]))

        return cards

    def __build_rankings(self) -> dict:
        """Build rankings for a standard 52 card french deck. Jokers have no value and are not present in a standard
        52 card deck. """
        rankings = {FrenchCards.one: 1, FrenchCards.two: 2, FrenchCards.three: 3, FrenchCards.four: 4,
                    FrenchCards.five: 5, FrenchCards.six: 6, FrenchCards.seven: 7, FrenchCards.eight: 8,
                    FrenchCards.nine: 9, FrenchCards.ten: 10, FrenchCards.jack: 11, FrenchCards.queen: 12,
                    FrenchCards.king: 13, FrenchCards.joker: None}
        return rankings
