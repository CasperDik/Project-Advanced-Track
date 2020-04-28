class Card:
    suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
    ranks = ["narf", "Ace", "2", "3", "4", "5", "6", "7","8", "9", "10", "Jack", "Queen", "King"]

    def __init__(self, suit=0, rank= 0):
        self.rank = rank
        self.suit = suit
    def __str__(self):
        return (self.ranks[self.rank]+ " of " + self.suits[self.suit])

    def compare(self,other):                #Ace is lowest card
        if self.suit > other.suit:
            return 1
        if self.suit < other.suit:
            return -1
        if self.rank > other.rank:
            return 1
        if self.rank < other.rank:
            return -1
        else:
            return 0
    def __eq__(self, other):
        return self.compare(other) == 0

    def __le__(self, other):
        return self.compare(other) <=0

    def __ge__(self, other):
        return self.compare(other) >= 0

    def __gt__(self, other):
        return self.compare(other) > 0

    def __lt__(self, other):
        return self.compare(other) < 0

    def __ne__(self, other):
        return self.compare(other) != 0

    def cmp(self,other):                #Ace is highest card
        if self.suit > other.suit:
            return 1
        if self.suit < other.suit:
            return -1
        if self.rank > other.rank and other.rank != 1:
            return 1
        if self.rank < other.rank and self.rank != 1:
            return -1
        if other.rank == 1 and other.rank < self.rank:
            return -1
        if self.rank == 1 and self.rank < other.rank:
            return 1
        else:
            return 0


