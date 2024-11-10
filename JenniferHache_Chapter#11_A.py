import random

# create class Deck to represent deck of cards
class Deck:
    def __init__(self, size):
        self.card_list = [i for i in range(size)]
        # use random function to shuffle cards
        random.shuffle(self.card_list)
        # store current card
        self.current_card = 0
        # store card deck size of 52
        self.size = size

    # deal card from deck (self)
    def deal(self):
        # use if statement to reshuffle cards if all cards have been dealt
        if self.size - self.current_card < 1:
            random.shuffle(self.card_list)
            self.current_card = 0
            # let user/player know cards are being reshuffled
            print('Reshuffling...!!!')
        self.current_card += 1
        # return current card (self)
        return self.card_list[self.current_card - 1]

# list card ranks
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
# list of suits: clubs, diamonds, hearts, spades
suits = ['clubs', 'diamonds', 'hearts', 'spades']

# Create a deck of 52 cards
my_deck = Deck(52)

# Deal 5 cards for the initial hand
initial_hand = []
for i in range(5):
    # deal 5 cards
    d = my_deck.deal()
    r = d % 13
    # Get rank
    s = d // 13
    # Get suit
    initial_hand.append((r, s))
    print(ranks[r], 'of', suits[s])

# Ask the user/player for which cards to replace. must choose up to 5 cards max.(1-5)
cards_to_replace = input("Enter the numbers of the cards you want to replace (Can only choose up to card 5): ")
cards_to_replace = [int(x) - 1 for x in cards_to_replace.split(',')]

# replace selected cards
for card_index in cards_to_replace:
    d = my_deck.deal()
    r = d % 13
    s = d // 13
    initial_hand[card_index] = (r, s)

# print the final hand after replacing cards. let user know this is the final hand
print("\nFinal hand after draw:")
for r, s in initial_hand:
    print(ranks[r], 'of', suits[s])
