
# RANDOMIZER FROM PYTHON
import random

# FUNCTION TO DRAW A RANDOM CARD FROM THE LISTS BELOW
def draw_random_card():
    SUITS = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    RANKS = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

    # RANDOM SELECTION OF SUIT AND RANK
    rank = random.choice(RANKS)
    suit = random.choice(SUITS)

    # PRINT THE RANK AND SUIT
    print(f"{rank} of {suit}")


# EXECUTE THE FUNCTION
draw_random_card()

