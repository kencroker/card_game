from card_system import card


class Hand:
    def __init__(self, cards: list):
        self.cards = cards

    def get_cards(self):
        return self.cards

    def score(self):
        score = 0
        for each_card in self.cards:
            score += each_card.value()

        return score

    def add_card(self, new_card: card.Card):
        self.cards.append(new_card)

    def display(self):
        output = ""
        for card_i in self.cards:
            output += card_i.display()
            output += "\n"

        return output


