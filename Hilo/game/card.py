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
        self.value = 0
        self.points = 0

    def first_card(self):
        """Generates a new random value for the first card"""
        self.value = random.randint(1, 13)

    def next_card(self, answer):
        """Generates a new random value for the second card and calculates the points according to user's answer
        Args:
            self (Card): An instance of Card.
            answer (string): higher or lower (h/l).
        """
        new_card = random.randint(1, 13)
        correct_answer = "l" if new_card < self.value else "h"
        self.points = 100 if correct_answer == answer else -75