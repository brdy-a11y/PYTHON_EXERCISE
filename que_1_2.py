''' Question 1 ) Write a program to demonstrate different numeric data types
 (int, float) and type conversion. '''

x = 5 
print(f"x : {x} | type : {type(x)}")  # integer datatype
y = 6.66  
print(f"y : {y} | type : {type(y)}") # float datatype

print(f'x : {x} | typecasting into float => x : {int(x)}')  # type conversion from integer to float type.

print(f'y : {y} | typecasting into integer => y : {int(y)}')  # type conversion from float to integer type.

# ----------------------------------------------------------

# converting string to integer :
age = input("Enter age : ")
age_int = int(age)
print(f"before conversion => age : {age} | type : {type(age)} ")
print(f"age : {age_int} | type : {type(age_int)}")

'''------------------------------------------------------------------------------------------------------------'''

# Question 2 :  Write a program to perform all arithmetic operations on user input numbers.

# Program to perform arithmetic operations on user-provided inputs

# 1. Taking input from the user

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # 2. all arithmetic Operations
    print("\n---# Arithmetic Results #---")
    print(f"Addition:       {num1} + {num2} = {num1 + num2}")
    print(f"Subtraction:    {num1} - {num2} = {num1 - num2}")
    print(f"Multiplication: {num1} * {num2} = {num1 * num2}")
    
    # if user tries to divide by zero
    if num2 != 0:
        print(f"Division:       {num1} / {num2} = {num1 / num2}")
        print(f"Floor Division: {num1} // {num2} = {num1 // num2}")
        print(f"Modulus:        {num1} % {num2} = {num1 % num2}")
    else:
        print("Division:       Cannot divide by zero.")
        print("Floor Division: Cannot perform on zero.")
        print("Modulus:        Cannot perform on zero.")
        
    print(f"Exponentiation: {num1} ** {num2} = {num1 ** num2}")

except ValueError:
    print("Invalid input! Please enter numeric values.")