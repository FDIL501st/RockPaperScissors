from enum import Enum
from random import choice

class Hand(Enum):
    ROCK = "Rock"
    PAPER = "Paper"
    SCISSORS = "Scissors"

    def __gt__(self, other) -> bool:
        """Only compares two hands. Returns true if the left hand beats the other hand in rock paper scissors.
        For example, paper > rock is true as paper beats rock. """
        if isinstance(other, Hand):
            if self == Hand.ROCK and other == Hand.SCISSORS:
                return True
            elif self == Hand.SCISSORS and other == Hand.PAPER:
                return True
            elif self == Hand.PAPER and other == Hand.ROCK:
                return True
            else:
                return False
        else:
            return NotImplemented
    # No need to do __lt__ as python will automatically just return opposite of __gt__, which is what we want

    @staticmethod
    def randomHand():
        """Returns a random hand."""
        hands = [Hand.ROCK, Hand.PAPER, Hand.SCISSORS]
        return choice(hands)

    @staticmethod
    def stringToHand(hand: str):
        """Returns a hand by matching the string provided to a hand.
        If hand provided is not a valid hand, will return None."""
        
        if hand == Hand.ROCK.value:
            return Hand.ROCK
        elif hand == Hand.PAPER.value:
            return Hand.PAPER
        elif hand == Hand.SCISSORS.value:
            return Hand.SCISSORS
        else:
            return None

if __name__ == "__main__":
    hands = []
    for x in range(5):
        hands.append(Hand.randomHand())
    print(hands)

    for x in range(4):
        print(hands[x] == hands[x+1])
    
    