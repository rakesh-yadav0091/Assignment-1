# This program checks whether the number entered by the user is even or odd.

#Taking input from the user
num = int(input("Enter a number: "))

# check if number is divisible by 2
if num % 2 == 0:
    print("The number is Even.")
else:
    print("The nimber is odd.")