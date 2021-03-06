import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six',
         'Seven', 'Eight', 'Nine', 'Ten', 'Jack',
         'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5,
          'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9,
          'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

playing = True  # variable to control main while loop - it defines whether player keeps on hitting or chooses to stand


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
                self.cards.append(Card(suit, rank))  # building all the 52 cards in deck

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

    def adjust_for_ace(self):  # function that changes value of aces (from 11 to 1) if hand value exceeds 21
        for card in self.cards:
            if self.value <= 21:  # if hand value is under 21, we quit the method and don't change anything
                break
            if card.rank == 'Ace':  # if we have an ace then we reduce its value by 10
                self.value -= 10


class Chips:  # in Polish: zetony

    def __init__(self, total=100):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


#  ------ Functions ------  #
def take_bet(chips):
    while True:
        try:
            print("Your current total of chips is: ", chips.total)
            chips.bet = int(input("What is your bet? (Integer): "))
        except ValueError:
            print('It must  be an integer!')
        else:
            if chips.bet > chips.total:
                print("You don't have enough chips! Your total of chips is: ", chips.total)
            else:
                break


def hit(deck, hand):
    card = deck.deal()
    hand.add_card(card)


def hit_or_stand(deck, hand):
    global playing
    while True:
        x = input("Do you want to hit or stand? [h/s] ")

        if x.lower() == 'h':
            print("Player hits")
            hit(deck, hand)
            break

        elif x.lower() == 's':
            print("Player stands")
            playing = False
            break

        else:
            print("Wrong input! You must type either 'h' or 's'")


# printing functions
def show_some(player, dealer):
    print("Dealer:")
    print("<hidden card>", *dealer.cards[1:], sep='\t')
    print(" ")
    print("Player:")
    print(*player.cards, sep='\t')


def show_all(player, dealer):
    print("Dealer:\t value:", dealer.value)
    print(*dealer.cards, sep='\t')
    print("Player:\t value:", player.value)
    print(*player.cards, sep='\t')


# win/lose functions
def player_busts(player, dealer, chips):
    print("Player busts! Player value: ", player.value)
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print("Player wins! Player value: ", player.value, "  Dealer value: ", dealer.value)
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print("Dealer busts! Dealer value: ", dealer.value)
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    print("Dealer wins! Player value: ", player.value, "  Dealer value: ", dealer.value)
    chips.lose_bet()


def push(player, dealer):
    print("Player and dealer has the same value. It's a push! Player value: ", player.value, "\t Dealer value:",
          dealer.value)



if __name__ == '__main__':
    while True:
        print("Welcome to BlackJack! Get as close to 21 as you can without going over!\n",
        "Dealer hits until it reaches 17. Aces count as 1 or 11.")

        deck = Deck()
        deck.shuffle_deck()
        player = Hand()
        dealer = Hand()
        player_chips = Chips()

        # adding two card to dealer's and player's hand
        dealer.add_card(deck.deal())
        dealer.add_card(deck.deal())
        player.add_card(deck.deal())
        player.add_card(deck.deal())

        # asking user to place a bet
        take_bet(player_chips)

        show_some(player, dealer)

        while playing:

            # player decides if he hits or stands
            hit_or_stand(deck, player)
            show_some(player, dealer)

            if player.value > 21:
                player_busts(player, dealer, player_chips)
                break

        if player.value <= 21:

            while dealer.value < 17:
                hit(deck, dealer)

            show_all(player, dealer)

            # win/loose scenarios
            if dealer.value > 21:
                dealer_busts(player, dealer, player_chips)
            elif dealer.value > player.value:
                dealer_wins(player, dealer, player_chips)
            elif dealer.value < player.value:
                player_wins(player, dealer, player_chips)
            elif dealer.value == player.value:
                push(player, dealer)

        print("\nPlayer's total chips: ", player_chips.total)

        inp = input("Would you like to play one more time? [y/n] ")

        if inp.lower() == 'y':
            playing=True
        else:
            print("Thanks for playing!")
            break
