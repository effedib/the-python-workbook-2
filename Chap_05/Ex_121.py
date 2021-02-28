# Random Lottery Numbers

# Display 6 random numbers between 1 and 49 without duplicates

def randomsix():
    from random import randint

    NUM_MIN = 1
    NUM_MAX = 49
    NUM_EXT = 6
    lottery_list = []
    while len(lottery_list) < NUM_EXT:
        n = randint(NUM_MIN, NUM_MAX)
        if n not in lottery_list:
            lottery_list.append(n)

    return sorted(lottery_list)


def main():
    print(randomsix())


if __name__ == "__main__":
    main()
