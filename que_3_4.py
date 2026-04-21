''' Question 3) Write a program to demonstrate variable assignment and swapping values. '''

# Initial Assignment
a = 5
b = 10

print(f"Before swapping: a = {a}, b = {b}")

# Swapping using a temporary variable
temp = a
a = b
b = temp
print(f"After swapping (using temp): a = {a}, b = {b}")

# Swapping using Python's tuple unpacking
x = 20
y = 30
print(f"\nBefore swapping: x = {x}, y = {y}")

x, y = y, x  # Tuple unpacking
print(f"After swapping (using tuple unpacking): x = {x}, y = {y}")

#==================================================================================

''' Question 4) Write a program using if-else to find the largest of three numbers.'''

try: # for detecting wrong type of input.
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    num3 = float(input("Enter third number: "))

    if (num1 >= num2) and (num1 >= num3):
        largest = num1
    elif (num2 >= num1) and (num2 >= num3):
        largest = num2
    else:
        largest = num3

    print(f"The largest number among {num1}, {num2}, and {num3} is {largest}")

except ValueError:
    print("Invalid input! Please enter numeric values.")