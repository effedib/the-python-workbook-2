# Compute a Grade Point Average

# Compute grade point average of an arbitrary number
# of letter grades enterd by the user

# Read the letter from the user
letter_grade = input("Enter the evaluation: ").upper()

# Set up the total and the count
tot_grade_points = 0
count = 0

while letter_grade != "":

    # Convert in the equivalent
    if letter_grade == 'A+' or letter_grade == 'A':
        grade_points = 4.0
    elif letter_grade == 'A-':
        grade_points = 3.7
    elif letter_grade == 'B+':
        grade_points = 3.3
    elif letter_grade == 'B':
        grade_points = 3.0
    elif letter_grade == 'B-':
        grade_points = 2.7
    elif letter_grade == 'C+':
        grade_points = 2.3
    elif letter_grade == 'C':
        grade_points = 2.0
    elif letter_grade == 'C-':
        grade_points = 1.7
    elif letter_grade == 'D+':
        grade_points = 1.3
    elif letter_grade == 'D':
        grade_points = 1.0
    elif letter_grade == 'F':
        grade_points = 0
    
    # Sum the grade points to the previous and increase the counter
    tot_grade_points += grade_points
    count += 1

    #Check for the next loop or exit
    letter_grade = input("Enter the evaluation (blank to quit): ").upper()

# Compute the average
avg = tot_grade_points / count

# Display the result
print("Grade Point Average: {:.2f}".format(avg))