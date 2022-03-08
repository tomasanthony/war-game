from abc import ABC, abstractmethod
import random
from typing import Optional

from src.cards.card import Card
from src.model.enums import FrenchSuits, FrenchCards
from src.model.exceptions import InvalidDeckError, CheatingError


class Deck(ABC):
    """Abstract class for a deck of playing cards. Variation exists
    within playing card deck size, suits, and cards. Default methods
    are provided for deck shuffling, drawing, and inserting. Subclasses can
    override these functions depending on the game."""

    @abstractmethod
    def __init__(self, deck_size: int, *args, **kwargs):
        self.rankings = self.build_rankings(*args, **kwargs)
        self.cards = self._build_deck()
        self.deck_size = deck_size
        self.missing_cards = []
        if not self.validate_deck_composition():
            raise InvalidDeckError

    @abstractmethod
    def _build_deck(self) -> list[Card]:
        """Decks are not consistently built the same way, so this function does not have a parent implementation"""
        pass

    def build_rankings(self, *args, **kwargs) -> dict:
        """Decks rankings vary, so this function does not have a parent implementation
            """

        pass

    def draw_card(self, draw_random: bool = False) -> Card:
        """Draw a card from the deck, either the card at the top
        of the deck or a random card. Deletes the card from the deck because it is no
        longer in the deck, it is in a hand. We add the card to a list of missing cards,
        in order to prevent 'cheating' by validating a returned card is in this list.
        The begining of the list is treated as the top of the deck.

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
            card = self.cards.pop(0)
            self.missing_cards.append(card)
            return card

    def insert_card(self, card: Card, insert_random: bool = False) -> bool:
        """Insert a card back into the deck. Validating it is a card that is
        missing from the deck and in a hand. Inserts randomly or at the top of
        the deck (inserted at index 0 to the list).

        Args:
            insert_random (bool): whether to insert a card randomly into the deck
            card (Card): a card to insert into the deck

        Returns:
            bool : returns true if the card was successfully inserted
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
            self.cards.insert(0, card)
            return True

    def shuffle_cards(self):
        """Randomly shuffles the deck of cards in place"""
        random.shuffle(self.cards)

    def validate_deck_composition(self) -> bool:
        """A deck needs to divide its size evenly across suits and their card types. If
        the joker card has no value, it is not in the deck. Validation adjust accordingly
        Returns:
            (bool) : a bool indicating whether the deck composition is valid or not."""
        if self.rankings[FrenchCards.joker] is None:
            return self.deck_size / len(FrenchSuits) == len(FrenchCards) - 1
        else:
            return self.deck_size / len(FrenchSuits) == len(FrenchCards)


class StandardFrenchDeck(Deck):
    """Standard French Deck"""

    def __init__(self, deck_size=52, rankings=None):
        super().__init__(deck_size=deck_size, rankings=rankings)

    def _build_deck(self) -> list[Card]:
        """Building a deck based on the size of the deck, the types of cards, and the suits.
        Only add a card to the deck if it has been given a ranking, e.g. joker cards are in use
        Returns:
            (list) : a list of cards the deck is built with"""
        cards = []
        for suit in FrenchSuits:
            for card in FrenchCards:
                if self.rankings[card] is not None:
                    cards.append(Card(suit=suit, pip_or_face=card, rank=self.rankings[card]))
        return cards

    def build_rankings(self, rankings=None) -> dict:
        """Build rankings for a standard 52 card french deck. Jokers have no value and are not present in a standard
        52 card deck.
        Args:
            rankings (dict[Optional]): non default rankings to create the deck with.

        Returns:
            (dict) : a dictionary of the provided rankings or the default rankings."""
        default_rankings = {FrenchCards.ace: 14, FrenchCards.two: 2, FrenchCards.three: 3, FrenchCards.four: 4,
                            FrenchCards.five: 5, FrenchCards.six: 6, FrenchCards.seven: 7, FrenchCards.eight: 8,
                            FrenchCards.nine: 9, FrenchCards.ten: 10, FrenchCards.jack: 11, FrenchCards.queen: 12,
                            FrenchCards.king: 13, FrenchCards.joker: None}
        return rankings or default_rankings
