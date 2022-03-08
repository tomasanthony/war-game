import copy
from unittest.mock import patch

import pytest

from src.cards.card import Card
from src.cards.deck import StandardFrenchDeck
from src.model.enums import FrenchCards
from src.model.exceptions import InvalidDeckError, CheatingError


def test_deck_validation():
    # When a deck is initialized with an invalid deck size
    # Then an InvalidDeckError is raised
    with pytest.raises(InvalidDeckError):
        _ = StandardFrenchDeck(deck_size=56)

    # Given joker cards have value in the deck (are in play)
    rankings = {FrenchCards.ace: 1, FrenchCards.two: 2, FrenchCards.three: 3, FrenchCards.four: 4,
                FrenchCards.five: 5, FrenchCards.six: 6, FrenchCards.seven: 7, FrenchCards.eight: 8,
                FrenchCards.nine: 9, FrenchCards.ten: 10, FrenchCards.jack: 11, FrenchCards.queen: 12,
                FrenchCards.king: 13, FrenchCards.joker: 14}
    # When a Standard French Deck is instantiated with jokers in play
    deck = StandardFrenchDeck(deck_size=56, rankings=rankings)
    # Then the deck is successfully validated and created
    assert deck


def test_shuffle_cards():
    # Given a Standard French Deck of unshuffled cards
    deck = StandardFrenchDeck(deck_size=52)
    unshuffled = copy.deepcopy(deck.cards)

    # When the deck is shuffled
    deck.shuffle_cards()

    # Then the order of cards is not the same as the unshuffled order
    shuffled = deck.cards
    assert unshuffled != shuffled


@patch("src.cards.deck.random")
def test_draw_card(mock_random):
    # Given a Standard French Deck's top card
    deck = StandardFrenchDeck(deck_size=52)
    top_card = deck.cards[0]

    # When a card is drawn from the top of the deck, non-randomly
    drawn_card = deck.draw_card()

    # Then the top card is the drawn card
    assert top_card == drawn_card

    # Given the same deck of cards, a mocked random object, and the expected card
    mock_random.randrange.return_value = -1
    random_card = deck.cards[-1]

    # When a card is drawn from the deck randomly
    drawn_card = deck.draw_card(draw_random=True)

    # Then the drawn card is the same as the expected random card
    assert drawn_card == random_card


def test_insert_card():
    # Given a Standard French Deck of cards and a card outside the deck
    deck = StandardFrenchDeck(deck_size=52)
    card = Card(suit=FrenchCards, pip_or_face=FrenchCards.king, rank=13)
    # When an insertion of a card is attempted to a full deck
    # Then a CheatingError is raised
    with pytest.raises(CheatingError):
        deck.insert_card(card)

    # Given the same deck, and a card that was validly drawn from the deck
    card = deck.draw_card()

    # When the card is inserted back into the deck
    # Then the insertion function successfully returns a True response
    assert deck.insert_card(card)


