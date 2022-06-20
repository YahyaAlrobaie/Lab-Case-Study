'''
Yahya Alrobaie
File: M02 Lab_Case Study.py
June/18/2022
version 3.0
1. This app accept student names and GPAs.
2. and test if the student qualifies for either the Dean's List(3.5 or greater) or the Honor Roll(3.25 or greater).
3. quit processing student records if the last name entered is 'ZZZ'.
'''

# using while loop with Walrus operator to get the user{last_name}and let the user exit.
while (last_name := input("Enter the student's last name or (Enter ZZZ to quit): ")) != "ZZZ":

#  get the user's first name and gpa.
    first_name = input("Enter the student's First Name: ")
    gpa = float(input("Enter the student's GPA: "))

# Display the result after get the correct user input.

    if gpa >= 3.5:
        print(f"{first_name} {last_name} has made the Dean's List!")
    elif (gpa >= 3.25) and  (gpa < 3.5):
        print(f"{first_name} {last_name} has made the Honor Roll!")
    else:
        print(f"{first_name} {last_name} has a GPA of {gpa}.")

print("Thank you for using our GPA app")

    
    
