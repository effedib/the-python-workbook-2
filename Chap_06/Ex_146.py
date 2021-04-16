# Create a Bingo Card

# The First function creates a random Bingo card, the Second function displays the Bingo card with the columns labelled
# appropriately.

def generateBingocard():
    from random import randint

    # I have to create a dict of lists like this:
    # bingo_card = {'B': [], 'I': [], 'N': [], 'G': [], 'O': []}

    bingo_card = dict()
    for letter in ['B', 'I', 'N', 'G', 'O']:
        bingo_card[letter] = []

    for i, c in enumerate(bingo_card):
        for n in range(5):
            # Generate a random number between (1, 15) and step ahead 15 numbers every letter in the dict bingo_card
            num = randint(0, 15) + (i * 15)
            while num in bingo_card[c]:
                num = randint(1, 15) + (i * 15)
            bingo_card[c].append(num)

    return bingo_card


def printBingocard(card: dict):
    for k in card:
        print('{:>2}'.format(k), end=' ')
    print()

    for i in range(5):
        for k in card:
            print('{:>2}'.format(card[k][i]), end=' ')
        print()


def main():
    bingo_label = generateBingocard()
    print(bingo_label)
    printBingocard(bingo_label)


if __name__ == "__main__":
    main()
