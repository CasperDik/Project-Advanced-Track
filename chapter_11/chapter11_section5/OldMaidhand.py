from chapter_11.chapter11_section4.Cards import Card
from chapter_11.chapter11_section4.Deck import Deck
from chapter_11.chapter11_section5.Hand import Hand


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

class OldMaidGame(CardGame):
    def play(self, names):
        self.deck.remove(Card(0,12))
        self.hands = []
        for name in names:
            self.hands.append(OldMaidhand(name))

        self.deck.deal(self.hands)
        print("---------- Cards have been dealt")
        self.print_hands()

        matches = self.remove_all_matches()
        print("---------- Matches discarded, play begins")
        self.print_hands()

        turn = 0
        num_hands = len(self.hands)
        while matches < 25:
            matches += self.play_one_turn(turn)
            turn = (turn + 1) % num_hands
        print("---------- Game is Over")
        self.print_hands()

    def remove_all_matches(self):
        count = 0
        for hand in self.hands:
            count += hand.remove_matches()
        return count

    def play_one_turn(self, i):
        if self.hands[i].empty():
            return 0
        neighbor = self.find_neighbor(i)
        picked_card = self.hands[neighbor].pop()
        self.hands[i].add(picked_card)
        print("Hand", self.hands[i].name, "picked", picked_card)
        count = self.hands[i].remove_matches()
        self.hands[i].shuffle()
        return count

    def find_neighbor(self, i):
        num_hands = len(self.hands)
        for next in range(1, num_hands):
            neighbor = (i + next) % num_hands
        if not self.hands[neighbor].empty():
            return neighbor

    def print_hands(self):
        for hand in self.hands:
            print(hand)

game = OldMaidGame()
game.play(["Allen", "Jeff", "Chris"])