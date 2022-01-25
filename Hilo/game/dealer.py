
from game.card import Card


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
        self.deck = []
        self.is_playing = True
        self.score = 0
        self.total_score = 0

        for i in range(13):
            card = Card()
            self.deck.append(card)

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
        hi_lo = input("Higher or Lower? [h/l] ")
        self.is_playing = (hi_lo == "y")
       
    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return 

        for i in range(len(self.deck)):
            card = self.deck[i]
            card.roll()
            self.score += card.points 
        self.total_score += self.score

    def do_outputs(self):
        """Displays the card and the score. Also asks the player if they want to play again. 

        Args:
            self (Dealer): An instance of Dealer.
        """
        if not self.is_playing:
            return

        values = ""
        for i in range(len(self.deck)):
            card = self.deck[i]
            values += f"{card.value} "

        print(f"The card is: {values}")
        print(f"Your score is: {self.total_score}\n")
        self.is_playing == (self.score > 0)
        play_again = input("Would you like to play again? (y/n) ")
        self.is_playing = (play_again == "y")
        