from chapter11_section4.Deck import Deck

class Hand(Deck):
    def __init__(self, name =""):
        self.cards =[]
        self.name = name
    def add(self, card):
        self.cards.append(card)
    def __str__(self):
        s = "Hand of " + self.name
        if self.empty():
            s += " is empty \n"
        else:
            s += " contains:\n"
        return s + Deck.__str__(self)


deck = Deck()
deck.shuffle()
hand = Hand("Frank")
deck.deal([hand],5)
#print(hand)