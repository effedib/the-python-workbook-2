# Grade Points to Letter Grade

# Commute the grade points in its equivalent letter grades

# Read the grade point from the user
grade_points = float(input("Enter the evaluation: "))

# Convert in the equivalent
grade_points = round(grade_points,1)
if grade_points>=4.0:
    letter_grade = 'A+'
elif 0 >= round(grade_points-4,1) >= -0.1 :
    letter_grade = 'A'
elif -0.2 >= round(grade_points-4,1) >= -0.5:
    letter_grade = 'A-'
elif 0.4 >= round(grade_points-3,1) >= 0.2:
    letter_grade = 'B+'
elif 0.1 >= round(grade_points-3,1) >= -0.1:
    letter_grade = 'B'
elif -0.2 >= round(grade_points-3,1) >= -0.5:
    letter_grade = 'B-'
elif 0.4 >= round(grade_points-2,1) >= 0.2:
    letter_grade = 'C+'
elif 0.1 >= round(grade_points-2,1) >= -0.1:
    letter_grade = 'C'
elif -0.2 >= round(grade_points-2,1) >= -0.5:
    letter_grade = 'C-'
elif 0.4 >= round(grade_points-1,1) >= 0.2:
    letter_grade = 'D+'
elif 0.1 >= round(grade_points-1,1) >= -0.1:
    letter_grade = 'D'
elif -0.2 >= round(grade_points-1,1):
    letter_grade = 'F'

# Display the result
print("The equivalent evaluation is: {}".format(letter_grade))