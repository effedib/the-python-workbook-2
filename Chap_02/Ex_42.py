# Note to Frequency

# Read the name of a note from the user and display the note's frequency

# Octave table'list
C4, D4, E4, F4, G4, A4, B4 = [261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88]

# Read the note name from the user
name = input('Enter the note: ').lower()
note = name[0]
octave = int(name[1])

# Match the name of the note witch its frequency
if note == 'c':
    freq = C4
elif note == 'd':
    freq = D4
elif note == 'e':
    freq = E4
elif note == 'f':
    freq = F4
elif note == 'g':
    freq = G4
elif note == 'a':
    freq = A4
elif note == 'b':
    freq = B4

# Adjust the frequency to bring it into correct octave
freq = freq / (2 ** (4 - octave))

# Display the result
print("Note's frequency: {:.2f}".format(freq))
