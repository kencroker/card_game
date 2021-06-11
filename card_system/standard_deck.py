from card_system import deck
from card_system import card
from card_system import enums


class StandardDeck(deck.Deck):
    def __init__(self):
        card_list = []
        for i in enums.Value:
            for j in enums.Suit:
                new_card = card.Card(i, j)
                card_list.append(new_card)

        super(StandardDeck, self).__init__(card_list)
