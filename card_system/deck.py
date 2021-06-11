import random
from card_system import hand


class Deck:
    def __init__(self, input_cards: list):
        assert type(input_cards) == list
        self.cards = input_cards

    def get_cards(self):
        return self.cards

    def shuffle(self):
        random.shuffle(self.cards)

    def remaining_cards(self):
        return len(self.cards)

    def deal_card(self):
        if self.remaining_cards() >= 1:
            return self.cards.pop()

        return None

    def deal_cards(self, num_cards):
        cards_list = []
        if self.remaining_cards() >= num_cards:
            for i in range(0, num_cards):
                cards_list.append(self.cards.pop())
            return cards_list
        else:
            return None

    def deal_hand(self, num_cards):
        cards_list = []
        if self.remaining_cards() >= num_cards:
            for i in range(0, num_cards):
                cards_list.append(self.cards.pop())

            dealt_hand = hand.Hand(cards=cards_list)
            return dealt_hand
        else:
            return None

    def display(self):
        output = ""
        for card_i in self.cards:
            output += card_i.display()
            output += "\n"

        output += "\n\nEND OF DECK\n\n"
        return output
