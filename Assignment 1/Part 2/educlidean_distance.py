# This program calculates the Euclidean distance between two user_defined points.

import math

# Input coordinates 
x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

# Calculate distance
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Output
print("Euclidean distance is:", round(distance, 2))