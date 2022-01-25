
from game.card import Card
import random


class Dealer:
    """A person who directs the game. 
    
    The responsibility of a Dealer is to control the sequence of play.

    Attributes:
        card (Card): A instances od Card().
        is_playing (boolean): Whether or not the game is being played.
        total_score (int): The score for the entire game.
    """

    def __init__(self):
        """Constructs a new Dealer.
        Args:
            self (Dealer): an instance of Dealer.
        """
        self.is_playing = True
        self.total_score = 300
        self.card = Card()

    def start_game(self):
        """Starts the game by running the main game loop.
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """Ask the user if they want to flip a card
        Args:
            self (Dealer): An instance of Dealer.
        """
        first_card = self.card.generate_card()
        print(f"Card showing is a {first_card}.")
        hi_lo = (input("Will the next card be higher or lower? [h/l] ")).lower()
        new_card = self.card.next_card(hi_lo)
        print(f"Your next card is a {new_card}.")
        
    
    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        self.total_score += self.card.points

    def do_outputs(self):
        """Displays the earned points and the total score. Also asks the player if they want to play again. 
        Args:
            self (Dealer): An instance of Dealer.
        """
        self.is_playing = (self.total_score > 0)
        if not self.is_playing: #This happens in case the player scores 0 or less points
            print("You lost!")
            exit()
        print(f"You earned {self.card.points} points.\nYour score is: {self.total_score}\n")
        flip_card = input("Flip a card? [y/n]").lower()
        self.is_playing = (flip_card == "y")
        if not self.is_playing:
            print("See you soon!\n")
            exit()