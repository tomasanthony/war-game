from src.cards.deck import Deck


class Player:
    def __init__(self):
        self.card_hand = []

    def build_hand(self, deck: Deck, hand_size: int):
        """

        Args:
            deck (Deck): deck of playing cards
            hand_size (int): the size of a players hand
        """
        while hand_size > 0 and len(deck.cards) > 0:
            self.card_hand.append(deck.draw_card(draw_random=True))
            hand_size -= 1

    def draw_card(self, deck: Deck):
        """

        Args:
            deck (Deck): deck of cards from which to draw. Card inserted to the bottom of the hand.
        """
        self.card_hand.append(deck.draw_card())

    def play_card(self):
        """
        Returns: (Card): the card that is being played
        """
        return self.card_hand.pop(0)
