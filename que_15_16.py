'''Q15. Write a program using built-in functions on list, string, and
dictionary.'''

# List functions
numbers = [5, 2, 9, 1, 5]
print(f"List: {numbers}")
print(f"Max: {max(numbers)}, Min: {min(numbers)}, Sum: {sum(numbers)}")
print(f"Sorted: {sorted(numbers)}")

# String functions
text = "  hello python  "
print(f"\nString: '{text}'")
print(f"Uppercase: '{text.upper()}'")
print(f"Stripped (remove whitespace): '{text.strip()}'")
print(f"Length: {len(text)}")

# Dictionary functions
data = {"a": 1, "b": 2}
print(f"\nDictionary: {data}")
print(f"Keys: {list(data.keys())}, Values: {list(data.values())}")

#============================================================================


'''Q16. Write functions to organize a program that performs basic
operations on strings and lists.'''

def process_list(lst):
    print(f"Processing list: {lst}")
    return [x * 2 for x in lst] # List comprehension

def process_string(s):
    print(f"Processing string: {s}")
    return s[::-1].upper() # Reverse and capitalizes the string

def main():
    # Calling the organized functions
    my_nums = [1, 2, 3, 4]
    my_str = "code"
    print(f"List : {my_nums}")
    print(f"String : {my_str}")

    double_nums = process_list(my_nums) # storing returned list
    transformed_str = process_string(my_str)  # storing returned strings.
    
    print(f"\nResults:")
    print(f"Doubled List: {double_nums}")
    print(f"Transformed String: {transformed_str}")

# Executing the main function
if __name__ == "__main__":
    main()