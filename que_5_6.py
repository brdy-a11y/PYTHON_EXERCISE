''' Question 5) Write a program using nested if to classify a number (positive, negative, zero).'''

try:
    num = float(input("Enter a number: "))

    if num >= 0:
        if num == 0:
            print("The number is Zero.")
        else:
            print("The number is Positive.")
    else:
        print("The number is Negative.")

except ValueError:
    print("Invalid input! Please enter a valid number.")


#===========================================================================================


''' Question 6) Write a program using for loop to print multiplication table of a number.'''
# Program to print the multiplication table of a number using a for loop

try:
    num = int(input("Enter the number for the multiplication table: "))
    limit = int(input("Enter the range (e.g., 10): "))

    print(f"\nMultiplication Table for {num}:")
    for i in range(1, limit + 1):
        # f-string formatting for cleaner output
        print(f"{num} x {i} = {num * i}")

except ValueError:
    print("Invalid input! Please enter integer values.")
