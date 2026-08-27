while True:
    try:
        first_number = float(input("Enter the 1st Number !"))
        break
    except ValueError:
        print("Invalid input! Please enter numbers only.\n")


while True:
    try:
        second_number = float(input("Enter the 2nd Number !"))
        break
    except ValueError:
        print("Invalid input! Please enter numbers only.\n")

addition = first_number + second_number
subtraction = first_number - second_number
multiplication = first_number * second_number


if second_number != 0:
       division  = first_number / second_number
else:
       division = "Cannot divide by zero"      

print("Addition", addition)
print("Subtraction", subtraction)
print("Multiplication", multiplication)
print("Division", division)
