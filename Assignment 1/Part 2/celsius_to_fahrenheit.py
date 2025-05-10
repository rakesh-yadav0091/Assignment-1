#This program converts temperature from celsius to fahrenheit.

# Take input from user
celsius = float(input("Enter temperature in celsius: "))

#convert
fahrenheit = (celsius * 9/5 + 32)

#output
print(f"{celsius}°C is equal to {fahrenheit}°F")