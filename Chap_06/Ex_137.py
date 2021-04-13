# Two Dice Simulation

# This function simulates the rolling of a pair of six-sided dice.
# The main function simulates rolling dice 1.000 times, counts the number of times each total occurs and display a
# summary table of this data.

def RollDice() -> int:

    from random import randint

    return randint(2, 12)


def main():
    expected = {2: 2.78, 3: 5.56, 4: 8.33, 5: 11.11, 6: 13.89, 7: 16.67,
                8: 13.89, 9: 11.11, 10: 8.33, 11: 5.56, 12: 2.78}
    rolls = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0}
    for i in range(1000):
        v = RollDice()
        rolls[v] += 1

    tot = sum(rolls.values())
    percentage = dict(rolls)
    for k in percentage:
        percentage[k] = rolls[k] / tot

    print("Total    Simulated   Expected")
    print("           Percent    Percent")
    for i in range(2, 13):
        print('{:>5}{:>13.2f}{:>11.2f}'.format(i, percentage[i] * 100, expected[i]))


if __name__ == "__main__":
    main()
