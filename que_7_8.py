''' Question 7. Write a program to iterate through string, list, and dictionary
using loops.'''

# 1. Iterating through a String
string_data = "Hello"
print("String iteration:")
for char in string_data:
    print(char, end=" ")
print("\n")

# 2. Iterating through a List
list_data = [10, 20, 30, 40]
print("List iteration:")
for item in list_data:
    print(item, end=" ")
print("\n")

# 3. Iterating through a Dictionary
dict_data = {"a": 1, "b": 2, "c": 3}
print("Dictionary iteration:")
for key, value in dict_data.items():
    print(f"Key: {key}, Value: {value}")


#=====================================================================================


''' Question 8. Write a program using while loop to compute sum of first N natural numbers.'''

try:
    n = int(input("Enter a positive integer N: "))
    
    if n < 0:
        print("Please enter a non-negative integer.") # clear instructions.
    else:
        total_sum = 0
        current = 1
    
        while current <= n:    
        # While loop logic
            total_sum += current
            current += 1
            
        print(f"The sum of the first {n} natural numbers is: {total_sum}")

except ValueError:
    print("Invalid input! Please enter an integer.")