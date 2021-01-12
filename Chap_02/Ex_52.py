# Letter Grade to Grade Points

# Commute the letter grades in its equivalent grade points

# Read the letter from the user
letter_grade = input("Enter the evaluation: ").upper()

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
else:
    grade_points = -1

if grade_points < 0:
    print("Evaluation not allowed!")
else:
    print("The equivalent evaluation is: {:.1f}".format(grade_points))