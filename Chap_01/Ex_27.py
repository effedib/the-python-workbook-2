# When is Easter

# Read the year from user
anno = int(input("Per conoscere la data in cui cade la Santa Pasqua,\ndevi prima digitare l'anno: "))

# Gregorian algorithm as function
def easter(year: int) -> str:
    a = year % 19
    b = year // 100
    c = year % 100
    d = b // 4
    e = b % 4
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i = c // 4
    k = c % 4
    l = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * l) // 451
    month = (h + l - 7 * m + 114) // 31
    day = 1 + ((h + l - 7 * m + 114) % 31)
    print("Data Santa Pasqua per l'anno %d: %d/%d/%d" % (year, day, month, year))

# Display the result
easter(anno)