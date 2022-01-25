
from game.card import Card
import random


class Dealer:
    """A person who directs the game. 
    
    The responsibility of a Dealer is to control the sequence of play.

    Attributes:
        deck (List[deck]): A list of Card instances.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """

    def __init__(self):
        """Constructs a new Dealer.
        
        Args:
            self (Dealer): an instance of Dealer.
        """
        self.cards = []
        self.is_playing = True
        self.score = 0
        self.total_score = 300
        self.hi_lo = ""

        card = Card()
        self.cards.append(card)

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
        """Ask the user if they want to a new card.

        Args:
            self (Dealer): An instance of Dealer.
        """
        flip_card = input("Flip a card? [y/n]").lower()
        self.is_playing = (flip_card == "y")
       
    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return 

        card = self.cards[0]
        card.next_card() 
        self.total_score += card.points

    def do_outputs(self):
        """Displays the card and the score. Also asks the player if they want to play again. 

        Args:
            self (Dealer): An instance of Dealer.
        """
        if not self.is_playing:
            return

        values = ""
        card = self.cards[0]
        values += f"{card.value} "

        print(f"Your score is: {self.total_score}\n")
        self.is_playing == (self.score > 0)
        