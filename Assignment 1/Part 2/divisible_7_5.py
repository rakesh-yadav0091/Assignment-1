# This program finds numbers between 1500 and 2000 divisible by 7 and multiples of 5.

for number in range(1500, 2000):
    if number % 7 == 0 and number % 5 == 0:
        print(number, end=" ")