# This program calculates simple interest based on principal, rate, and time.

# Input values
p = float(input("Enter principal amount: "))
R = float(input("Enter rate of interest: "))
T = float(input("Enter time in years: "))

# Calculate interest
SI = (p * R * T) / 100

# Output
print("Simple Interest is:", SI)