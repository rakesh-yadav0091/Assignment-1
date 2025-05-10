# This program counts the number of digits and letters in a user-provided string.

text = input("Enter a string: ")

letters = digits = 0

for char in text:
    if char.isalpha():
        letters += 1
    elif char.isdigit():
        digits += 1

print("Letters:", letters)
print("Digits:", digits)