# Scrabble Score

# Compute and display the Scrabble score for a word.

def ScrabbleScore(word: str) -> int:

    point_letters = {
        'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1,
        'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8,
        'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1,
        'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1,
        'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10
    }

    score = 0
    for c in word.upper():
        score += point_letters[c]

    return score


def main():
    string = input('Enter a string to calculate the equivalent Scrabble Score: ')
    print('The Scrabble Score for the word: {} is: {}'.format(string, ScrabbleScore(string)))


if __name__ == "__main__":
    main()
