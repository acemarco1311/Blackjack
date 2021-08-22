import math
import random

class Player:

    def __init__(self, name):
        """Constructs a Player with the given name and an empty hand of Cards"""
        self.__name = name
        self.__score = 0
        self.__cards = []
    
    def get_name(self):
        """Returns the Player's name"""
        return self.__name

    def hit_me(self, card):
        """Puts the argument Card into the Player's hand"""
        self.__cards.append(card)
        
    def get_hand(self):
        """Returns the Player's hand as a list of Cards

           You will need to loop through the list and call the Card
           methods to find out the value of each.
        """
        return self.__cards

    def get_hand_value(self):
        """Returns an int representing the combined value of all
            cards in Player's hand.

            Aces will be increased to a value of 11 if the resulting
            value would be less than or equal to 21. Otherwise, Aces
            will have a value of 1. All other face cards including
            Jacks, Queens and Kings will contribute 10 to the total
            value. Number cards will contribute their number value.
        """
        value = 0
        for c in self.__cards:
            value += c.get_value()
        for i in range(len(self.__cards)):
            if self.__cards[i].get_rank() == "Ace":
                if value + 10 <= 21:
                    value += 10
        return value

    def reset_hand(self):
        """removes all Cards from the Player's hand"""
        self.__cards.clear()
    
    def is_bust(self):
        """Returns True if the hand value is greater than 21.
            Otherwise False
        """
        if self.get_hand_value() > 21:
            return True
        return False
    
    def get_score(self):
        """Returns the number of games the Player has won in a row."""
        return self.__score

    def win(self):
        """Adds 1 to the number of games the Player has won in a row."""
        self.__score += 1

    def lose(self):
        """Resets the number of games won back to zero."""
        self.__score = 0
    
    def __str__(self):
        return "Blackjack Player: " + self.__name


class Deck:

    def __init__(self):
        """Constructs a Deck of 52 Cards in numerical order."""
        self.__cards = []
        self.reset()
        
    def reset(self):
        """Restores any Cards removed by drawing cards and sorts them in numerical order."""
        self.__cards.clear()
        for val in range(1, 14):
            for suit in range(1, 5):
                self.__cards.append(Card(val, suit))

    def shuffle(self):
        """Randomizes the order of Cards left in the Deck."""
        random.shuffle(self.__cards)

    def draw_card(self):
        """Returns the top Card of the Deck or None if there are none left."""
        if self.size() > 0:
            return self.__cards.pop()

    def size(self):
        """Returns the number of Cards left in the Deck."""
        return len(self.__cards)

    def __str__(self):
        return str(self.size()) + " card deck"


class Card:
    
    def __init__(self, rank_num, suit_num):
        """Constructs a card from a rank_num from 1-13 and suit_num from 1-4

           The rank_num determines the value of the card.
           1 is Ace
           11 is Jack
           12 is Queen
           13 is King
           2 - 10 are number values

           The suit_num determines the suit string of the card.
           1 is Spades
           2 is Hearts
           3 is Diamonds
           4 is Clubs
           
           Any other arguments will throw an Error.
        """
        if rank_num < 1 or rank_num > 13:
            raise ValueError(rank_num)
        if suit_num < 1 or suit_num > 4:
            raise ValueError(suit_num)
        
        if rank_num == 1:
            self.__rank = "Ace"
        elif rank_num == 11:
            self.__rank = "Jack"
        elif rank_num == 12:
            self.__rank = "Queen"
        elif rank_num == 13:
            self.__rank = "King"
        elif rank_num > 0 and rank_num <= 10:
            self.__rank = str(rank_num)
            
        if suit_num == 1:
            self.__suit = "Spades"
        elif suit_num == 2:
            self.__suit = "Hearts"
        elif suit_num == 3:
            self.__suit = "Diamonds"
        elif suit_num == 4:
            self.__suit = "Clubs"

        self.__value = min(rank_num, 10)

    def get_value(self):
        """Return the number value of the Card from 1-10.
           Ace will return 1 even though it's value may be 1 or 11.
        """
        return self.__value

    def get_rank(self):
        """Returns the rank of the Card as a String."""
        return self.__rank

    def get_suit(self):
        """Returns the suit of the Card as a String."""
        return self.__suit

    def __str__(self):
        return self.__rank + " of " + self.__suit

