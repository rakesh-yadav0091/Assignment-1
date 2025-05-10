# This program divides two integers and shows the result with exactly two decimal places.

# Input two integers
a = int(input("Enter the first number: "))
b = (int(input("Enter the second number: ")))

# Check for division by zero
if b != 0:
    result = a / b
    print("Result:", format(result, ".2f"))
else:
    print("Error: Cannot divided by zero.")