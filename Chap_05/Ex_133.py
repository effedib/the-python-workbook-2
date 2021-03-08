# Does a list contain a sublist?

def isSublist(smaller, larger) -> bool:
    if smaller is None or smaller == larger:

        return True

    sublist = []
    i = 0
    for l in smaller:
        if l in larger[i:]:
            if sublist == [] or \
               (larger[larger.index(l)-1] == sublist[len(sublist)-1]):
                sublist.append(l)
                i = larger.index(l)

    if smaller == sublist:

        return True

    else:

        return False


def main():
    small = [5, 9, 12]
    large = [5, 9, 12, 15]
    print(isSublist(small, large))


if __name__ == "__main__":
    main()
