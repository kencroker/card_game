import BlackjackHand
from card_system import standard_deck


class Agent:
    def __init__(self):
        sd = standard_deck.StandardDeck()
        sd.shuffle()
        the_hand = sd.deal_hand(num_cards=2)

        self.hand = BlackjackHand.BlackjackHand(generic_hand=the_hand)

    def get_score(self):
        return self.hand.score()

    def get_hand(self):
        return self.hand

    def show_cards(self):
        print(self.hand.display())

    def hit(self):
        sd = standard_deck.StandardDeck()
        self.hand.add_card(sd.deal_card())

    def stand(self):
        pass


class Dealer(Agent):
    def __init__(self):
        super(Dealer, self).__init__()
        self.hand.get_cards()[1].set_visible(False)

    def play_hand(self):
        # once the dealer starts playing their hand, the hidden card becomes visible
        self.hand.get_cards()[1].set_visible(True)

        # keep hitting while score is 16 or under. After that, stand
        while self.hand.score() <= 16:
            self.hit()
        self.stand()


class Player(Agent):
    def __init__(self):
        super(Player, self).__init__()

    def double_down(self):
        pass

    @staticmethod
    def show_options_to_user():
        for i in range(0, 10):
            chosen_option = input("Will you hit or stand?")
            if chosen_option in ['hit', 'stand']:
                return chosen_option
            else:
                print("Please type in either 'hit' or 'stand' (in lowercase)")
                continue

        raise ValueError("Can't get a valid input")

    def play_hand(self):
        while self.get_score() <= 21:

            user_option = self.show_options_to_user()
            if user_option == 'stand':
                break

            elif user_option == 'hit':
                self.hit()
                self.show_cards()


