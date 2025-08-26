from random import shuffle


class Card:

    def __init__(self, value, suit):
        allowed_suit = ("Hearts", "Diamonds", "Clubs", "Spades")
        allowed_value = ("A", "2", "3", "4", "5", "6", "7",
                         "8", "9", "10", "J", "Q", "K")

        if suit not in allowed_suit or value not in allowed_value:
            raise ValueError("Entered invalid argument to suit or value")
        self.suit = suit
        self.value = value

    def __repr__(self):
        return f"{self.value} of {self.suit}"


class Deck:
    def __init__(self):
        allowed_suit = ("Hearts", "Diamonds", "Clubs", "Spades")
        allowed_value = ("A", "2", "3", "4", "5", "6", "7",
                         "8", "9", "10", "J", "Q", "K")
        # list comprehension
        self.cards = [Card(value, suit)
                      for suit in allowed_suit for value in allowed_value]

    def __repr__(self):
        return f"Deck of {self.count()} cards."

    def __iter__(self):
        return iter(self.cards)

    def count(self):
        return len(self.cards)

    def _deal(self, number):
        count = self.count()
        if count == 0:
            raise ValueError("All cards have been dealt")
        actual = min(count, number)

        # saving the removed cards to "cards" with slicing and updating the deck of cards
        cards = self.cards[-actual:]
        self.cards = self.cards[:-actual]
        return cards

    def deal_card(self):
        # need to return specific item otherwise it would return a list with single intem in it
        return self._deal(1)[0]

    def deal_hand(self, number):
        return self._deal(number)

    def shuffle(self):
        if self.count() < 52:
            raise ValueError("Only full decks can be shuffled")
        shuffle(self.cards)


d = Deck()
d.shuffle()
print(d.cards)

for card in d:
    print(card)
