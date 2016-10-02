import random

Deck = []
def addlands(xli):
    x = 0
    while x <= 20:
        xli.append ('l')
        x += 1

addlands(Deck)
print('Printing Deck')
print(Deck)

Deck.extend((2,2,2,2,2,2,3,3,3,3,3,3,4,4,4,4,5,5,6))
print('Print after Deck.extend')
print(Deck)
print type(Deck)

def Game():
    class player:
        life = 20
        deck = Deck
        field = []
        hand = []
        graveyard = []

        def __init__(self, name):
            self.name = name


    P1 = player('Player 1')
    P2 = player('Player 2')


    random.shuffle(P1.deck)
    random.shuffle(P2.deck)

    for i in range(1,7):
        x = P1.deck.pop()
        P1.hand.extend(x)
        # print (P1.hand)
        y = P2.deck.pop()
        P2.hand.extend(y)

    print(P1.hand)

Game()