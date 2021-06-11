import Agent


class BlackjackGame:
    def __init__(self, num_players):
        self.players = []
        for i in range(0, num_players):
            self.players.append(Agent.Player())

        self.dealer = Agent.Dealer()

    def pregame_display(self):
        i = 0
        for player in self.players:
            print("Player ", i, "'s hand:\n", player.get_hand().display())
            i += 1

        print("Dealer's hand: \n", self.dealer.get_hand().display())

    def player_turn(self):
        player_scores = []
        # print("\n\nFirst player:\n")

        # first_iteration = True
        for player in self.players:
            """
            if first_iteration:
                first_iteration = False
            else:
                print("\n\nNext player:\n")
            """

            player.play_hand()
            player_scores.append(player.get_score())

        return player_scores

    def dealer_turn(self):

        self.dealer.play_hand()
        self.dealer.show_cards()
        return self.dealer.get_score()

    def play_game(self):
        player_scores = self.player_turn()
        dealer_score = self.dealer_turn()

        self.display_results(player_scores, dealer_score)

    @staticmethod
    def display_results(player_scores: list, dealer_score: int):
        for i in range(len(player_scores)):
            if player_scores[i] > 21:
                print("Player", i, "is bust! Player ", i, "loses against dealer.\n")

            elif dealer_score > 21:
                print("Player", i, "is not bust but the dealer is! Player ", i, "wins against dealer.\n")

            elif player_scores[i] == dealer_score:
                print("Player", i, "pushes against dealer.\n")

            elif player_scores[i] > dealer_score:
                print("Player", i, "wins against dealer.\n")

            elif player_scores[i] < dealer_score:
                print("Player", i, "loses against dealer.\n")







