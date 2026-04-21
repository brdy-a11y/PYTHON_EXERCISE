''' Question 9. Demonstrate use of break, continue, and pass in loops. '''

print("--- Demonstration of 'break' (Stops the loop entirely) ---")
for i in range(1, 6):
    if i == 4:
        break # completely terminate this loops execution.
    print(i, end=" ") # Output: 1 2 3

print("\n\n--- Demonstration of 'continue' (Skips current iteration) ---")
for i in range(1, 6):
    if i == 3:
        continue # to skip current iteration
    print(i, end=" ") # Output: 1 2 4 5

print("\n\n--- Demonstration of 'pass' (Acts as a placeholder) ---")
for i in range(1, 6):
    if i == 2:
        pass # Does nothing, continues loop; not tampering loop execution.
    print(i, end=" ") # Output: 1 2 3 4 5
print()


# ======================================================================================================


''' Question 10. Write a program to perform string operations (slicing, concatenation, reversing).'''

text = "HelloPythonCheekyGeek"

# 1. Slicing
# Syntax: [start:stop:step]
substring = text[0:5]    # Characters from index 0 to 4
slice_step = text[::2]   # Every char skipping 2 

# 2. Concatenation
str1 = "Hello"
str2 = "World"
full_str = str1 + " " + str2

# 3. Reversing
reversed_text = text[::-1] # directly reverses string

print(f"Original String: {text}")
print(f"Sliced (0-5):   {substring}")
print(f"Step Slicing:   {slice_step}")
print(f"Concatenated:   {full_str}")
print(f"Reversed:       {reversed_text}")