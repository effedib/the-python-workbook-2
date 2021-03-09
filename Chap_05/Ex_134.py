# Generate All Sublist of a List


def genAllSubs(list_mom: list) -> list:
    sublists = [[]]

    for l in range(1, len(list_mom) + 1):
        # range (-l +1) to doesn't exit from the large list
        for i in range(0, len(list_mom) - l + 1):
            sublists.append(list_mom[i:i + l])

    return sublists


def main():
    lista = [19, 32, 54, 69]
    print(genAllSubs(lista))


if __name__ == "__main__":
    main()
