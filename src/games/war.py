from src.cards.deck import StandardFrenchDeck
from src.player.player import Player


class War:
    def __init__(self):
        self.deck = StandardFrenchDeck()
        self.player_1 = Player()
        self.player_2 = Player()
        self.score = 0
        self.in_play = False

    def initialize_hands(self):
        """
        This function initializes the playing hands for the players.
        """
        self.player_1.build_hand(deck=self.deck, hand_size=self.deck.deck_size // 2)
        self.player_2.build_hand(deck=self.deck, hand_size=self.deck.deck_size // 2)

    def play_round(self):
        """
        This function plays a round of the game war.
        """
        winner = False
        won_cards = []
        while not winner and self.player_1.card_hand and self.player_2.card_hand:
            player_1_card = self.player_1.play_card()
            print(f'Player One plays {player_1_card.pip_or_face.value} of {player_1_card.suit.value}')
            player_2_card = self.player_2.play_card()
            print(f'Player Two plays {player_2_card.pip_or_face.value} of {player_2_card.suit.value}')
            won_cards.extend([player_1_card, player_2_card])
            if player_1_card.rank > player_2_card.rank:
                winner = True
                self.player_1.card_hand.extend(won_cards)
                print('Player One wins this round!')
            elif player_2_card.rank > player_1_card.rank:
                winner = True
                self.player_2.card_hand.extend(won_cards)
                print('Player Two wins this round!')
            else:
                print('Tie, starting a card War!')
                winner = self.card_war(won_cards)
                if winner == 1:
                    self.player_1.card_hand.extend(won_cards)
                else:
                    self.player_2.card_hand.extend(won_cards)

        print(f'Score:\n'
              f'Player One - {len(self.player_1.card_hand)}\n'
              f'Player Two - {len(self.player_2.card_hand)}\n')
        if not self.player_1.card_hand and not self.player_2.card_hand:
            self.in_play = False
            print('Tie Game!')

        elif not self.player_1.card_hand:
            self.in_play = False
            print('Player One loses!')

        elif not self.player_2.card_hand:
            self.in_play = False
            print('Player Two loses!')

    def card_war(self, won_cards):
        """This function executes a war, using the mutable won_cards list to pass the winnings
        back to the calling function

        Args:
            won_cards (list): a list of cards that were won during the war.
            """
        tie = True
        while tie and len(self.player_1.card_hand) >= 4 and len(self.player_2.card_hand) >= 4:
            down_cards = [self.player_1.play_card(), self.player_1.play_card(), self.player_1.play_card(),
                          self.player_2.play_card(), self.player_2.play_card(), self.player_2.play_card()]
            player_1_war_card = self.player_1.play_card()
            player_2_war_card = self.player_2.play_card()
            won_cards.extend(down_cards)
            won_cards.extend([player_1_war_card, player_2_war_card])
            if player_1_war_card.rank > player_2_war_card.rank:
                return 1
            elif player_2_war_card.rank > player_1_war_card.rank:
                return 2
        if len(self.player_1.card_hand) < 4 and len(self.player_2.card_hand) < 4:
            self.player_1.card_hand = []
            self.player_2.card_hand = []
            return True

        elif len(self.player_1.card_hand) < 4:
            self.player_1.card_hand = []
            return True
        elif len(self.player_2.card_hand) < 4:
            self.player_2.card_hand = []
            return True

    def play_game(self):
        """
        This function handles input from the player.
        """
        self.in_play = True
        while self.in_play:
            start_round = input(
                '\'Play\' or press \'Enter\' to play a round of war.\n\'Stop\' to exit.\n\'Speedy\' to play all '
                'rounds '
            )
            if start_round.lower() in ['speed game', 'fast', 'quick', 'speed', 'speedy']:
                while self.in_play:
                    self.play_round()
            elif start_round.lower() in ['no', 'stop', 'n', 'quit', 'q', 'oh please stop', ""]:
                print('Quitting Game\n')
                exit()
            elif start_round.lower() in ['play', 'start', 'yes', 'y', 'you\'re hired']:
                print('Playing a round of war!\n')
                self.play_round()
            else:
                print('Please enter a valid command\n')


if __name__ == "__main__":
    war = War()
    war.initialize_hands()
    war.play_game()
