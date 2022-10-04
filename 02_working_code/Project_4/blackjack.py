"""
The following code is the classes, functions, structure and logic used to creat a blackjack
game between a player and computer dealer.

Classes will be used to create the deck, deal hands and track cards, handle betting and hold the pots.

For this blackjack game it will be a simulation only, with no human input.
"""

# Import libraries and setup deck tuples 
import random

suit = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
rank = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
vals = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10,
        'Queen': 10, 'King': 10, 'Ace': 11}


class Card:
    # Creates the attributes and value for a card
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.vals = vals[rank]

    # Returns a print statement describing the card
    def __str__(self):
        return self.rank + ' of ' + self.suit


class Deck:
    # Creates a new deck of 52 unique card instances
    def __init__(self):
        self.deck_cards = []
        for suits in suit:
            for ranks in rank:
                self.deck_cards.append(Card(suits, ranks))

                # Returns a print statement describing the deck contents

    def __str__(self):
        deck_list = ''
        for card in self.deck_cards:
            deck_list += '\n ' + card.__str__()  # add each Card object's print string
        return 'The deck has:' + deck_list

    def shuffle(self):
        random.shuffle(self.deck_cards)

    # Deals a single card off the top of the deck
    def deal(self):
        single_card = self.deck_cards.pop(0)
        return single_card


class Hand:
    # Creates a hand of cards for a player
    def __init__(self):
        self.hand_cards = []
        self.value = 0
        self.aces = 0

        # Describes the contents of the player's hand

    def __str__(self):
        hand_list = ''
        for card in self.hand_cards:
            hand_list += '\n' + card.__str__()
        return f'hand has: \n' + hand_list

        # Function call to modify the ace count score based on hand value

    def adjust_for_aces(self):
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1

            # Adds a card to they player's hand

    def add_card(self, card):
        self.hand_cards.append(card)
        self.value += vals[card.rank]
        if card.rank == 'Ace':
            self.aces += 1
        Hand.adjust_for_aces(self)


class Chips:
    # initializes chips and betting structure
    def __init__(self, total):
        self.total = total
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


def make_bet(chips, round_num):
    # Takes a bet and checks if it exceeds the total available
    while True:
        try:
            chips.bet = int(input('How many chips do you want to bet?    '))
        except ValueError:
            print('Error - Bet must be an integer!')
        else:
            if chips.bet > chips.total:
                print('Your bet cannot exceed', chips.total)
            else:
                break


def show_some(player, dealer):
    # Show partial dealer hand and full player hand for play action
    print("\nDealer's hand: ")
    print("\t<card face down>")
    print("\t", dealer.hand_cards[1])
    print("\nPlayer's hand:  ", *player.hand_cards, sep='\n\t ')
    print("Player's score = ", player.value)


def show_all(player, dealer):
    # Show all hands for end of round
    print("\nDealer's hand:  ", *dealer.hand_cards, sep='\n ')
    print("Dealer's score = ", dealer.value)
    print("\nPlayer's hand:  ", *player.hand_cards, sep='\n ')
    print("Player's score = ", player.value)


def hit(deck, hand):
    player_hand.add_card(deck.deal())


def hit_or_stand(deck, hand):
    # Ask for player input for action
    while True:
        action = str(input('\nHit or Stand [H/S]?:   '))
        if action[0].lower() == 'h':
            print('\nPlayer Hits')
            hit(deck, hand)
            action = 'hit'
            break
        elif action[0].lower() == 's':
            print('\nPlayer passes. Dealer is playing.')
            action = 'stand'
            break
        else:
            print('Invalid entry, please try again.')
    return action


# Final gameplay logic for win/loss actions
def player_busts(player, dealer, chips):
    print('\nPlayer BUSTS - Dealer WINS')

    chips.lose_bet()


def player_wins(player, dealer, chips):
    print('\nPlayer WINS !')
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print('\nDealer BUSTS - Player WINS')
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    print('\nDealer wins')
    chips.lose_bet()


def push(player, dealer):
    print("\nPlayer and Dealer TIE - it's a PUSH")


'''
Game Logic
'''
# Explain the game and prompt total betting pot
print('Welcome to the high-rollers table!\n')
print('The game is blackjack, highest to 21 wins without going bust!\n\
Dealer must hit until they have atleast 17 and Aces count as 1 or 11.\n')
while True:
    try:
        total = int(input('How much do you wish to play with today?    '))
    except ValueError:
        print('Error - Bet must be an integer!')
    else:
        break

total_start = total

# Initiate a new game by making the deck, and a discard pile to be shuffled re-inturoduced
deck = Deck()
discard_pile = []
deck.shuffle()

# Initiate hands for player and dealer, as well as betting pot
dealer_hand = Hand()
player_hand = Hand()
player_chips = Chips(total)

playing = True
round_count = 0

while playing:
    round_count += 1
    bust = False
    # Deal hands
    dealer_hand = Hand()
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    make_bet(player_chips, round_count)
    print(
        f'\nRound {str(round_count)} - The player has {str(player_chips.total)} chips and bets {str(player_chips.bet)}.')

    show_some(player_hand, dealer_hand)

    round_on = True
    # Starts a new round logic after taking the bet and dealing first cards
    while round_on:
        # Asks for player action based on hand value, shows new deal
        action = hit_or_stand(deck, player_hand)

        # shows player hand update if hit
        if action == 'hit':
            show_some(player_hand, dealer_hand)

        # Checks if player bust
        if player_hand.value > 21:
            player_busts(player_hand, dealer_hand, player_chips)
            bust = True
            round_on = False

        # Dealer auto-play logic
        if (player_hand.value <= 21) and (action == 'stand'):
            while round_on:
                # Checks for dealer bust
                if dealer_hand.value > 21:
                    show_all(player_hand, dealer_hand)
                    dealer_busts(player_hand, dealer_hand, player_chips)
                    bust = True
                    round_on = False
                    break
                # Continues taking cards if score less than 17
                elif dealer_hand.value < 17:
                    dealer_hand.add_card(deck.deal())
                else:
                    round_on = False
                    show_all(player_hand, dealer_hand)
                    break

        # If neither has busted, check who wins
        if not round_on and not bust:
            if player_hand.value > dealer_hand.value:
                player_wins(player_hand, dealer_hand, player_chips)
            elif player_hand.value < dealer_hand.value:
                dealer_wins(player_hand, dealer_hand, player_chips)
            else:
                push(player_hand, dealer_hand)

        if not round_on:
            # Round is over, prompt replay
            print(
                f"\nThe player's chips stand at {str(player_chips.total)}\nThe player's winnings stand at {str(player_chips.total - total)}")
            while True:
                cont = input('\nContinue playing [Y/N]?    ')
                if cont[0].lower() == 'y':
                    # Put hands in discard pile
                    discard_pile.append(player_hand.hand_cards)
                    discard_pile.append(dealer_hand.hand_cards)
                    break
                elif cont[0].lower() == 'n':
                    print('\nThanks for playing. Please come again!')
                    print(f'You are leaving with {str(player_chips.total - total)} chips in total winnings')
                    playing = False
                    break
                else:
                    print('Invalid entry, please try again.')
