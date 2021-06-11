from card_system import enums


class Card:
    def __init__(self, face_value: enums.Value, suit: enums.Suit):
        self.visible = True
        self.suit = suit
        self.face_value = face_value

    def get_suit(self):
        return self.suit

    def is_visible(self):
        return self.visible

    def get_face_value(self):
        return self.face_value

    def set_visible(self, visible):
        self.visible = visible

    def set_suit(self, suit):
        self.suit = suit

    def value(self):
        return self.face_value.value

    def display(self):
        if not self.visible:
            return "(this card is face down)"
        else:
            output = self.face_value.name
            output += " OF "
            output += self.suit.name
            return output

