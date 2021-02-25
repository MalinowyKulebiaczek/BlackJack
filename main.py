import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six',
         'Seven', 'Eight', 'Nine', 'Ten', 'Jack',
         'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5,
          'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9,
          'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit


class Deck:

    def __init__(self):
        self.cards = []
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))     # building all the 52 cards in deck

    def __str__(self):
        deck_string = ''
        for card in self.cards:
            deck_string += card.__str__() + '\n'
        return "The deck: \n" + deck_string

    def shuffle_deck(self):
        random.shuffle(self.cards)

    def deal(self):
        card = self.cards.pop()
        return card


class Hand:

    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0

    def __str__(self):
        deck_string = ''
        for card in self.cards:
            deck_string += card.__str__() + '\n'
        return "Hand: \n" + deck_string

    def add_card(self, card):
        self.cards.append(card)
        self.calculate_value()

    def calculate_value(self):
        val = 0
        for card in self.cards:
            val += values[card.rank]
        self.value = val
        self.adjust_for_ace()

    def adjust_for_ace(self):   # function that changes value of aces (from 11 to 1) if hand value exceeds 21
        for card in self.cards:
            if self.value <= 21:    # if hand value is under 21, we quit the method and don't change anything
                break
            if card.rank == 'Ace':  # if we have an ace then we reduce its value by 10
                self.value -= 10


class Chips: # in Polish: zetony

    def __init__(self, total=100):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet



playing = True

'''
# TESTY
card1 = Card(suits[0], ranks[0])
card2 = Card(suits[1], ranks[1])
print(card1)
print(card2)
print(card1.rank)
card1.rank = ranks[2]
print(card1.rank)

deck = Deck()
print(deck)
deck.shuffle_deck()
print(deck)
player = Hand()
player.add_card(deck.deal())
player.add_card(deck.deal())
print(player.value)
print(player)
'''

if __name__ == '__main__':
    pass


