# Shuffling a Deck of Cards

# The first function creates a deck of 52 cards into a list, the second function shuffles this deck

def createDeck() -> list:
    suits = ('s', 'h', 'd', 'c')
    cards = ('T', 'J', 'Q', 'K', 'A')

    deck = []
    for s in suits:
        for c in range(2, 10):
            card = str(c) + s
            deck.append(card)
        for c in cards:
            card = c + s
            deck.append(card)

    return deck


def shuffleDeck(deck: list) -> list:
    from random import randrange
    deck = createDeck()
    for i, c in enumerate(deck):
        pos = randrange(i, len(deck))
        deck[i], deck[pos] = deck[pos], deck[i]

    return deck


def main():
    deck = createDeck()
    print(deck)
    print(shuffleDeck(deck))


if __name__ == "__main__":
    main()
