import random

# Create class Deck to represent deck of cards
class Deck:
    def __init__(self, size=52):
        self.card_list = [i for i in range(size)]
        # Shuffle cards using random method
        random.shuffle(self.card_list)
        self.current_card = 0

    # Deals a card from the deck
    def deal(self):
        if self.current_card >= len(self.card_list):
            random.shuffle(self.card_list)
            # Reshuffle if all cards are dealt
            self.current_card = 0
            print('Reshuffling...!!!')
        card = self.card_list[self.current_card]
        self.current_card += 1
        return card

    # Deals an initial hand of cards.
    def deal_initial_hand(self, num_cards=5):
        hand = []
        for _ in range(num_cards):
            card = self.deal()
            hand.append(card)
        return hand

    # Replace selected cards in the hand
    def replace_cards(self, hand, cards_to_replace):
        for card_index in cards_to_replace:
            card = self.deal()
            hand[card_index] = card
        return hand


# List of card ranks and suits
# Returns the rank a suit for a given card number.
def get_card_info(card):
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    suits = ['clubs', 'diamonds', 'hearts', 'spades']
    rank = card % 13
    suit = card // 13
    return ranks[rank], suits[suit]


# Prints the current hand
def print_hand(hand):
    for card in hand:
        rank, suit = get_card_info(card)
        print(f'{rank} of {suit}')


def play_game():
    # Create a deck of cards
    deck = Deck()

    # Deal an initial hand of 5 cards
    initial_hand = deck.deal_initial_hand()
    print("Initial hand:")
    print_hand(initial_hand)

    # Ask the user/player for which cards to replace (1-5)
    try:
        cards_to_replace = input("Enter the numbers of the cards you want to replace (Any card from 1-5): ")
        cards_to_replace = [int(x.strip()) - 1 for x in cards_to_replace.split(',')]
        # Convert to 0-based index
        if any(card < 0 or card > 4 for card in cards_to_replace):
            # If user enters anything other that 1-5, error message will display.
            raise ValueError("Error! Please select cards between 1 and 5.")
    except ValueError as e:
        print(f"Invalid input: {e}")
        return  # Exit if input is invalid

    # Replace selected cards
    updated_hand = deck.replace_cards(initial_hand, cards_to_replace)

    # Print the final hand after replacing cards
    print("\nFinal hand:")
    print_hand(updated_hand)


# Start the game
if __name__ == "__main__":
    play_game()
