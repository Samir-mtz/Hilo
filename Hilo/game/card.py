import random


class Card:
    """A card with a different value between 1 and 13.

    The responsibility of Card is to keep track of the values of the cards and calculate the points for 
    it.
    """

    def __init__(self):
        """Constructs a new instance of Card.

        Args:
            self (Card): An instance of Card.
        """
        self.points = 0
        self.value = 0

    def generate_card(self):
        self.value = random.randint(1,13)
        return self.value

    def next_card(self, hi_lo):
        """Generates a new random value for the second card and calculates the points according to user's answer
        Args:
            self (Card): An instance of Card.
            hi_lo (string): higher or lower (h/l).
        """
        new_card = self.value
        while(new_card == self.value): #This makes sure that the value is higher or lower but not equal to the first card.
            new_card = random.randint(1,13)

        correct_answer = "l" if new_card < self.value else "h"
        self.points = 100 if correct_answer == hi_lo else (-75)
        return new_card