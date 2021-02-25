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
        str = ''
        for card in self.cards:
            str += card.__str__() + '\n'
        return "The deck: \n" + str

playing = True

'''
card1 = Card(suits[0], ranks[0])
card2 = Card(suits[1], ranks[1])
print(card1)
print(card2)
print(card1.rank)
card1.rank = ranks[2]
print(card1.rank)
'''
deck = Deck()
print(deck)



if __name__ == '__main__':
    pass


