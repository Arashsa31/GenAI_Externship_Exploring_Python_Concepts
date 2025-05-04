#Task 1 - Variables: Your First Python Intro
name = "Arash"
age = 30
height = 5.11
print("Task 1 - Variables: Your First Python Intro")
print("Hey there, my name is " + name + "! I'm " + str(age) + " years old and " + str(height) + " feet tall.\n")

#Task 2 - Operators: Playing with Numbers
num1 = 3
num2 = 5
print("Task 2 - Operators: Playing with Numbers")
print("The sum of " + str(num1) + " and " + str(num2) + " is: ", num1 + num2)
print("The subtraction of " + str(num1) + " and " + str(num2) + " is: ", num1 - num2)
print("The multiplication of " + str(num1) + " and " + str(num2) + " is: ", num1 * num2)
print("The division of " + str(num1) + " and " + str(num2) + " is: ", num1 / num2, "\n")

#Task 3 - Conditional Statements: The Number Checker
print("Task 3 - Conditional Statements: The Number Checker")
user_input = input("Please enter a number: ")
user_input = float(user_input)
if user_input > 0:
    print("This number is positive. Awesome!")
elif user_input < 0:
    print("This number is negative. Better luck next time!")
elif user_input == 0:
    print("Zero it is. A perfect balance!")
else:
    print("Error!")