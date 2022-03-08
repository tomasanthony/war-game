from src.cards.deck import StandardFrenchDeck
from src.player.player import Player


def test_build_hand():
    # Given a card game player and a deck of cards
    player = Player()
    deck = StandardFrenchDeck()

    # When that player builds their playing card hand
    player.build_hand(deck, deck.deck_size//2)

    # Then that players playing card hand exists and is the specified length
    assert player.card_hand and len(player.card_hand) == deck.deck_size//2
