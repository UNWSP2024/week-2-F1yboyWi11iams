
def average_age():
    # Get User Input
    print("This program is designed to take input of the user's friend's names and ages and averages the ages of the friends.")
    name = input('Enter Friend 1 Name: ')
    age1 = input('Enter Friend 1 Age: ')
    print(name, age1)
    name2 = input('Enter Friend 2 Name: ')
    age2 = input('Enter Friend 2 Age: ')
    print(name2, age2)
    name3 = input('Enter Friend 3 Name: ')
    age3 = input('Enter Friend 3 Age: ')
    print(name3, age3)
    name4 = input('Enter Friend 4 Name: ')
    age4 = input('Enter Friend 4 Age: ')
    print(name4, age4)
    name5 = input('Enter Friend 5 Name: ')
    age5 = input('Enter Friend 5 Age: ')
    print(name5, age5)

    # Sum ages
    sum_ages = int(age1 + age2 + age3 + age4 + age5)
    print(f'Sum of Ages: ', sum_ages)

    # Average the ages
    average_ages = (sum_ages / 5)

    # Print the results
    print("Average of Friend's Ages: ", average_ages)

# Line which calls the above function.
average_age()
