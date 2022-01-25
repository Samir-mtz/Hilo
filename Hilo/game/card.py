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

    def next_card(self):
        """Generates a new random value for the second card and calculates the points according to user's answer
        Args:
            self (Card): An instance of Card.
            answer (string): higher or lower (h/l).
         """

        first_card = random.randint(1,13)
        print(f"Card showing is a {first_card}.")
        hi_lo = (input("Will the next card be higher or lower? [h/l] ")).lower()
        new_card = random.randint(1, 13)
        print(f"Your next card is a {new_card}.")
        correct_answer = "l" if new_card < first_card else "h"
        self.points = 100 if correct_answer == hi_lo else (-75)