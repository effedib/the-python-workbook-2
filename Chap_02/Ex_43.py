# Frequency to Note

# Convert a frequency note to its name (if exist)

# Octave table'list
C4_FREQ, D4_FREQ, E4_FREQ, F4_FREQ, G4_FREQ, A4_FREQ, B4_FREQ = [261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88]

# Read the frequency from the user
freq = float(input("Enter the frequency: "))
LIMIT = 1

# Verify if the frequency is in the table
if (C4_FREQ-LIMIT) < freq < (C4_FREQ+LIMIT):
    freq_name = 'C4'
elif (D4_FREQ-LIMIT) < freq < (D4_FREQ+LIMIT):
    freq_name = 'D4'
elif (E4_FREQ-LIMIT) < freq < (E4_FREQ+LIMIT):
    freq_name = 'E4'
elif (F4_FREQ-LIMIT) < freq < (F4_FREQ+LIMIT):
    freq_name = 'F4'
elif (G4_FREQ-LIMIT) < freq < (G4_FREQ+LIMIT):
    freq_name = 'G4'
elif (A4_FREQ-LIMIT) < freq < (A4_FREQ+LIMIT):
    freq_name = 'A4'
elif (B4_FREQ-LIMIT) < freq < (B4_FREQ+LIMIT):
    freq_name = 'B4'
else:
    freq_name = ''

# Display the result
if freq_name == '':
    print("The frequency doesn't correspond to a known note")
else:
    print("The note is: {:s}".format(freq_name))


