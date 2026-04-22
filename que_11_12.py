''' Question 11. Write a program to count frequency of characters in a string. '''

text = input("Enter a string: ")
frequency = {}

for char in text:
    # if the character is already in the freq count dictionary, increment its count
    if char in frequency:
        frequency[char] += 1
    # If it is not, add it to the dictionary with a count of 1
    else:
        frequency[char] = 1

print("\nCharacter frequencies:")
for char, count in frequency.items():
    print(f"'{char}': {count}")


#=============================================================================


''' Question 12. Write a program to demonstrate list slicing and list manipulation '''

listt = [10, 20, 30, 40, 50, 60]

# Slicing
print(f"Original list: {listt}")
print(f"Slice : (index 1 to 4): {listt[1:4]}")
print(f"Slice : (skipping elements): {listt[::2]}")

# Manipulation
# Adding Elements
listt.append(70)    # adds to end
listt.insert(0, 5)  # to insert 5 at index 0

# Removing Elements
listt.remove(20)    # removes the first occurrence of 20
popped_val = listt.pop()    # removes and returns the last element

# Modifying Elements
listt[2] = 99       # changes value at index 2

print(f"Modified list: {listt}")
print(f"Popped value: {popped_val}")