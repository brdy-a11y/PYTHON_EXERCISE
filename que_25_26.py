''' Q25. Write a program demonstrating multiple exceptions handling. '''

def divide_numbers(a, b):
    try:
        result = a / b
        # Let's assume we want to process a list here
        my_list = [1, 2]
        print(f"List item: {my_list[5]}") # This will raise an IndexError
        
    except ZeroDivisionError:
        print("Error: You cannot divide by zero.")
    except IndexError:
        print("Error: You tried to access an index that doesn't exist.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Testing the function
divide_numbers(10, 2)


# ==============================================================================


''' Q26. Write a program using finally and custom exceptions.'''

# Defining a custom exception ( self declared )
class NegativeNumberError(Exception):
    # Exception raised for errors in the input number
    pass

def check_age(age):
    if age < 0:
        raise NegativeNumberError("Age cannot be negative!")
    print(f"Age set to: {age}")

# Using finally and custom exception
try:
    age = int(input("enter age : "))
    check_age(age)
except NegativeNumberError as e:
    print(f"Caught custom exception: {e}")
finally: # always runs, after try and except.
    print("Execution complete. Cleaning up resources...")