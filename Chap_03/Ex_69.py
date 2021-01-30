# Admission Price

# Compute the admission cost for a group of people according to their ages

# Read the fist age
first_age = input("Enter the age of the first person: ")

# Set up the total
total_cost = 0

age = first_age
while age != "":
    # Cast age to int type
    age = int(age)

    # Check the cost
    if age <= 2:
        cost = 0
    elif 3 <= age <= 12:
        cost = 14.00
    elif age >= 65:
        cost = 18.00
    else:
        cost = 23.00
    
    # Update the total cost
    total_cost += cost

    # Check for the next loop or exit
    age = input("Enter the age of the next person (blank to quit): ")

# Display the result
print("Total cost for the group: {:.2f}".format(total_cost))