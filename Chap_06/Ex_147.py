# Checking for a Winning Card

# This function takes a dictionary representing a Bingo card as its only parameter. If the card contains a line of five
# zeros (vertical, horizontal, diagonal) returns True, indicating that the card has won.

from Ex_146 import printBingocard


def isWinning(bingo_card: dict) -> bool:
    for k in bingo_card:
        win = sum(bingo_card[k])
        if win == 0:
            return True

    for i in range(5):
        win = 0
        for k in bingo_card:
            win += bingo_card[k][i]
        if win == 0:
            return True

    for i in range(5):
        win = 0
        n = 0
        for k in bingo_card:
            win += bingo_card[k][n]
            n += 1
        if win == 0:
            return True

    for i in range(5):
        win = 0
        n = 4
        for k in bingo_card:
            win += bingo_card[k][n]
            n -= 1
        if win == 0:
            return True

    return False


def main():
    ver = {'B': [0, 0, 0, 0, 0], 'I': [17, 25, 23, 22, 30], 'N': [33, 37, 32, 31, 44],
           'G': [51, 50, 56, 58, 54], 'O': [63, 73, 64, 75, 61]}
    hor = {'B': [0, 2, 13, 9, 7], 'I': [0, 18, 29, 25, 28], 'N': [0, 38, 31, 44, 45],
           'G': [0, 58, 50, 53, 55], 'O': [0, 70, 65, 69, 71]}
    dia1 = {'B': [0, 12, 5, 15, 2], 'I': [20, 0, 24, 22, 27], 'N': [43, 37, 0, 35, 32],
            'G': [56, 57, 48, 0, 55], 'O': [70, 63, 72, 69, 0]}
    dia2 = {'B': [7, 5, 9, 6, 0], 'I': [20, 18, 26, 0, 30], 'N': [40, 42, 0, 32, 39],
            'G': [51, 0, 47, 55, 49], 'O': [0, 64, 75, 61, 68]}
    non_win = {'B': [5, 0, 15, 1, 9], 'I': [0, 17, 29, 30, 18], 'N': [31, 37, 39, 34, 33],
               'G': [58, 48, 0, 55, 59], 'O': [73, 63, 62, 68, 0]}

    card_list = [ver, hor, dia1, dia2, non_win]

    for dic in card_list:
        printBingocard(dic)
        if isWinning(dic):
            print('This is a winning card!!!\n')
        else:
            print("This isn't a winning card!!!\n")


if __name__ == "__main__":
    main()
