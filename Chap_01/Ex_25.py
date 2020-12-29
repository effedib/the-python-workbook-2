# Units of time (again)

# Convert seconds in days, hours and minutes
DAY = 86400
HOURS = 3600
MINUTES = 60

# Read time in seconds from user
time = int(input("Inserire il tempo in secondi: "))

# Compute in form D:HH:MM:SS
day = 0; hours = 0; minutes = 0
while time > 0:
    if time > DAY:
        day = time / DAY
        time = time % DAY
    elif time > HOURS:
        hours = time / HOURS
        time = time % HOURS
    elif time > MINUTES:
        minutes = time / MINUTES
        time = time % MINUTES
    else:
        break

# Display the result
print("Tempo: %d:%02d:%02d:%02d" % (day, hours, minutes, time))