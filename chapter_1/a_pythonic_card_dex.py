# Example 1-1. A deck as a sequence of playing cards
import collections

from random import choice
# Tạo class chứa rank và suit của con bài
Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()
    
    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        # Khi định nghĩa lại hàm __len__ này thì khi gọi len() sẽ gọi đến hàm này và trả về độ dài của _cards
        return len(self._cards)

    def __getitem__(self, position):
        #  Khi gọi đến FrenchDeck[1] thì sẽ gọi đến hàm này và trả về giá trị của _cards[1]
        return self._cards[position]


if __name__ == "__main__":
    french_deck = FrenchDeck()
    print(french_deck._cards)
    print(len(french_deck))
    print(french_deck[1])
    print(choice(french_deck))
    print(french_deck[:3])
    print(french_deck[12::13])
    
    for card in french_deck:
        print(card)
        
    for card in reversed(french_deck):
        print(card)