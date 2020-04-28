from chapter11_section4.Cards import Card
from chapter11_section4.Deck import Deck
from chapter11_section5.Hand import Hand

class CardGame:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()

class OldMaidhand(Hand):
    def remove_matches(self):
        count = 0
        original_cards = self.cards[:]
        for card in original_cards:
            match = Card(3 - card.suit, card.rank)
            if match in self.cards:
                self.cards.remove(card)
                self.cards.remove(match)
                print("Hand {0}: {1} matches {2}".format(self.name, card, match))
                count += 1
        return count


game = CardGame()
hand = OldMaidhand("Frank")
game.deck.deal([hand],13)
print(hand)
hand.remove_matches()
print(hand)