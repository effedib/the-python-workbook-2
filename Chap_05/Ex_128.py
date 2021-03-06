# Count the Elements

# This function determines and returns the number of elements within a list that are greater than or equal to some
# minimum value and less than some maximum value.

def countRange(n_list: list, min_val: float, max_val: float) -> int:
    count = 0

    for i in n_list:
        if min_val <= i < max_val:
            count += 1

    return count


def main():
    num_list = [3, 3.2, 5, 6.4, 9, 15.6]

    print(countRange(num_list, 3.1, 14))


if __name__ == "__main__":
    main()

