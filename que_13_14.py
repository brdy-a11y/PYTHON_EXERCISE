''' Q13. Write a program to perform tuple operations and demonstrate
immutability. '''

# 1. Creating a tuple
tuple_ = (10, 20, 30, 40, 50)
print(f"Original Tuple: {tuple_}")

# 2. Accessing elements (indexing/slicing)
print(f"First element: {tuple_[0]}")
print(f"Sliced tuple: {tuple_[1:4]}")

# 3. Concatenation
new_tuple = tuple_ + (60, 70)
print(f"Concatenated Tuple: {new_tuple}")

# 4. Demonstrating Immutability
# uncommenting the line below will raise a TypeError
# my_tuple[0] = 100 
print("Note: Tuples are immutable; attempting to modify an index will cause an error.")

# =======================================================================================


'''Q14. Write a program to perform dictionary operations (add, update, delete).'''

# 1. Initialize dictionary
student = {"name": "Anish", "age": 20, "course": "CSE"}
print(f"Initial Dictionary: {student}")

# 2. Add a new key-value pair
student["grade"] = "A"
print(f"After adding 'grade': {student}")

# 3. Update an existing value
student["age"] = 21
print(f"After updating 'age': {student}")

# 4. Delete a key-value pair
del student["course"]
# Alternative: student.pop("course")
print(f"After deleting 'course': {student}")