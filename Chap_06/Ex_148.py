# Play Bingo

# Simulate a game of Bingo for a single card. Generate a list of all of the valid Bingo calls (B1 through O75).
# Randomize the order of its elements by calling the shuffle function in the random module. Consume calls out of the
# list and cross out numbers on the card until the card contains a winning line.

from random import shuffle
from Ex_146 import generateBingocard, printBingocard
from Ex_147 import isWinning


def generateBingocalls() -> list:
    calls_list = list()
    for i in range(1, 76):
        calls_list.append(i)
    shuffle(calls_list)

    return calls_list


def playBingo(card: dict) -> int:
    count = 0
    calls = generateBingocalls()
    for i in calls:
        for k in card:
            for n in range(5):
                if card[k][n] == i:
                    card[k][n] = 0
        count += 1
        if isWinning(card):

            return count

    return False


def main():
    min_win = max_win = avg = 0
    for i in range(1000):
        new_card = generateBingocard()
        win = playBingo(new_card)
        if win is False:
            print('Error on playBingo')
        else:
            if win < min_win or min_win == 0:
                min_win = win
            if win > max_win:
                max_win = win
            avg += win
    avg /= 1000
    print('Before you can win you must make a minimum number of {} calls'.format(min_win))
    print('Maybe to win you have to make a maximum number of {} calls'.format(max_win))
    print('The average number of calls to win is {:.2f}'.format(avg))


if __name__ == "__main__":
    main()
