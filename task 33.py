#Task 33
#Define a variable called "grade" and get its value from user input.
#Check if the grade is greater than or equal to 90, display "A".
#If the grade is between 80 and 89 (inclusive), display "B".
#If the grade is between 70 and 79 (inclusive), display "C".
#If the grade is less than 70, display "F".

grade = int(input("Enter your grade: "))

if grade >= 90:
    print("A")
elif 80 <= grade <= 89:
    print("B")
elif 70 <= grade <= 79:
    print("C")
else:
    print("F")
