# Ia s License Plate Valid?

# Display if a licens plate is valid for the older or newer style license plate

letters = (
    "b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s",
    "t", "v", "w", "x", "y", "z","a", "e", "i", "o", "u"
)

numbers = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')

# Read the license plate from the user
plate = input("Enter the license plate: ").lower()

# Check the plate and display it
if len(plate) == 6 and \
    plate[0] or plate[1] or plate[2] in letters and \
    plate[3] or plate[4] or plate[5] in numbers:
    print("This is an older style of license plate")
elif len(plate) == 7 and \
    plate[0] or plate[1] or plate[2] or plate[3] in numbers and \
    plate[4] or plate[5] or plate[6] in letters:
    print("This is a newer style of license plate")
else:
    print("This is not valid for either style of license plate")
