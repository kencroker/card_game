from card_system import card
from card_system import enums


class BlackjackCard(card.Card):
    def __init__(self, value: enums.Value = None, suit: enums.Suit = None, generic_card: card.Card = None):
        if generic_card is not None:
            super(BlackjackCard, self).__init__(generic_card.get_face_value(), generic_card.get_suit())
        elif value is not None and suit is not None:
            super(BlackjackCard, self).__init__(value, suit)
        else:
            raise TypeError("The constructor requires either a value and suit or a generic Card object.")

    def is_ace(self):
        return self.face_value == enums.Value.ACE

    def is_face_card(self):
        return self.face_value in [enums.Value.JACK, enums.Value.QUEEN, enums.Value.KING]

    def value(self):
        if self.is_ace():
            return 1
        else:
            return self.face_value

    def min_value(self):
        if self.is_ace():
            return 1
        else:
            return self.face_value

    def max_value(self):
        if self.is_ace():
            return 11
        else:
            return self.face_value

