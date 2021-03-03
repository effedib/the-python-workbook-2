# Shuffling a Deck of Cards

# The first function creates a deck of 52 cards into a list, the second function shuffles this deck

def createDeck() -> list:
    suits = ('s', 'h', 'd', 'c')
    cards = ('T', 'J', 'Q', 'K', 'A')

    # deck = []
    # for s in suits:
    #     for c in range(2, 10):
    #         deck.append(str(c) + s)
    #     for c in cards:
    #         deck.append(c + s)

    # Same for loop with list comprehensions
    deck = [(str(c) + s) for s in suits for c in range(2, 10)]
    deck = deck + [(c + s) for s in suits for c in cards]

    return deck


def shuffleDeck(deck: list) -> list:
    from random import randrange
    deck = createDeck()
    for i in range(len(deck)):
        pos = randrange(i, len(deck))
        deck[i], deck[pos] = deck[pos], deck[i]

    return deck


def main():
    deck = createDeck()
    print(deck)
    print(shuffleDeck(deck))


if __name__ == "__main__":
    main()
