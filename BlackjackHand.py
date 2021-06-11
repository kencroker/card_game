import BlackjackCard
from card_system import hand, enums, card


class BlackjackHand(hand.Hand):
    def __init__(self, bj_cards: list = None, generic_hand: hand.Hand = None):
        if bj_cards is not None:

            # bj_cards must be a list of BlackjackCard objects specifically, not just a list of Card objects
            for card_i in bj_cards:
                if type(card_i) != BlackjackCard.BlackjackCard:
                    raise TypeError("BlackjackHand only takes lists of BlackjackCard objects specifically. Generic "
                                    "Card objects will not suffice.")

            super(BlackjackHand, self).__init__(bj_cards)

        elif generic_hand is not None:
            self.__alt_constructor(generic_hand=generic_hand)

        else:
            raise TypeError("Constructor requires either a list of BlackjackCard objects or a generic Hand object")

    def __alt_constructor(self, generic_hand):
        # we need to convert each card in the hand into a blackjack card
        bj_cards = []
        for card_i in generic_hand.get_cards():
            converted_card = BlackjackCard.BlackjackCard(generic_card=card_i)
            bj_cards.append(converted_card)

        # bj_card is now full of BlackjackCard objects
        # now call the parent constructor
        super(BlackjackHand, self).__init__(cards=bj_cards)

    def get_possible_scores(self):
        assert len(self.cards) != 0
        possible_scores = []
        min_possible_sum = 0
        alternative_sum = 0

        no_aces_seen = True
        for card_i in self.cards:
            if card_i.is_face_card():
                min_possible_sum += 10
                alternative_sum += 10

            # only the first ace can be counted as an 11. counting two aces as 11 each results in a bust
            elif card_i.is_ace():
                min_possible_sum += 1
                if no_aces_seen:
                    alternative_sum += 11
                    no_aces_seen = False
                else:
                    alternative_sum += 1
            else:
                val = card_i.value().value
                min_possible_sum += val
                alternative_sum += val

        possible_scores.append(min_possible_sum)
        possible_scores.append(alternative_sum)
        return possible_scores

    def score(self):
        possible_scores = self.get_possible_scores()
        max_under = -10000
        min_over = 10000

        for score in possible_scores:
            if max_under < score <= 21:
                max_under = score
            if 21 < score < min_over:
                min_over = score

        if max_under == -10000:
            return min_over
        else:
            return max_under

    def add_card(self, new_card: card.Card):
        if type(new_card) != card.Card:
            raise TypeError("Only Card objects can be added to a BlackjackHand object.")

        # if the card is not a blackjack card, convert it into one
        new_card = BlackjackCard.BlackjackCard(new_card.get_face_value(), new_card.get_suit())
        self.cards.append(new_card)

    def busted(self):
        return self.score() > 21

    def is_21(self):
        return self.score() == 21

    def is_blackjack(self):
        if len(self.cards) != 2:
            return False
        if self.score() != 21:
            return False

        possibility1 = self.cards[0].is_face_card() & self.cards[1].is_ace()
        possibility2 = (self.cards[0].get_face_value() == enums.Value.TEN) & self.cards[1].is_ace()
        possibility3 = self.cards[0].is_ace() & self.cards[1].is_face_card()
        possibility4 = self.cards[0].is_ace() & (self.cards[1].get_face_value() == enums.Value.TEN)
        return ((possibility1 | possibility2) | possibility3) | possibility4
