# Both Letter Grades and Grade Points
# Convert letter grades to grade points and vice-versa.

# Converts letter grades to grade points
def lettergrd2numbergrd(letter_grade: str) -> float:
    letter_grade = letter_grade.upper()

    grades = {
        'A+': 4.0,
        'A': 4.0,
        'A-': 3.7,
        'B+': 3.3,
        'B': 3.0,
        'B-': 2.7,
        'C+': 2.3,
        'C': 2.0,
        'C-': 1.7,
        'D+': 1.3,
        'D': 1.0,
        'F': 0.0
    }

    return grades[letter_grade]


# Converts grade points to letter grades
def numbergrd2lettergrd(evaluation: str) -> str:
    if float(evaluation) > -1:
        evaluation = round(float(evaluation), 1)
        if evaluation > 4.0:
            letter_grade = 'A+'
        elif evaluation == 4.0:
            letter_grade = 'A'
        elif 3.9 > evaluation >= 3.7:
            letter_grade = 'A-'
        elif 3.7 > evaluation >= 3.3:
            letter_grade = 'B+'
        elif 3.3 > evaluation >= 3.0:
            letter_grade = 'B'
        elif 3.0 > evaluation >= 2.7:
            letter_grade = 'B-'
        elif 2.7 > evaluation >= 2.3:
            letter_grade = 'C+'
        elif 2.3 > evaluation >= 2.0:
            letter_grade = 'C'
        elif 2.0 > evaluation >= 1.7:
            letter_grade = 'C-'
        elif 1.7 > evaluation >= 1.3:
            letter_grade = 'D+'
        elif 1.3 > evaluation >= 1.0:
            letter_grade = 'D'
        elif evaluation < 1.0:
            letter_grade = 'F'

        return letter_grade


# Try both conversions
def conversionsGrades(vote: str):
    try:
        return "Here is the conversion: {}\n".format(lettergrd2numbergrd(vote))

    except:
        try:
            return "Here is the conversion: {}\n".format(numbergrd2lettergrd(vote))

        except:
            return "You must enter a valid evaluation or letter grade!\n"


def main():
    vote_input = input("Enter a valid evaluation or letter grade: ")

    # loop the conversions (or reporting errors) until the user enters a blank line
    while vote_input != "":
        print(conversionsGrades(vote_input))
        vote_input = input("Enter a valid evaluation or letter grade (blank to quit): ")


if __name__ == '__main__':
    main()
