# Dealing Hands of Cards

# Create, shuffle and deal 5 hands of five cards

from Ex_125 import createDeck, shuffleDeck


def dealCards(num_hands: int, cards4hand: int, deck: list) -> list:
    deal = []
    for i in range(num_hands):
        hand = []
        for card in range(cards4hand):
            hand.append(deck.pop())
        deal.append(hand)

    return deal


def main():
    new_deck = createDeck()
    new_deck = shuffleDeck(new_deck)
    dealt_cards = dealCards(4, 5, new_deck)
    print("Deal the cards:\n{}\n".format(dealt_cards))
    print("Cards remaining:\n{}".format(new_deck))


if __name__ == "__main__":
    main()
