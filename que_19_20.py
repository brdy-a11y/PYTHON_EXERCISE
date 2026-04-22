''' Q19. Write a program to copy contents of one file to another.'''

# Program to copyyy contents
def copy_file(source, destination):
    try:
        with open(source, 'r') as f_src:
            content = f_src.read()
            
        with open(destination, 'w') as f_dest:
            f_dest.write(content)
        print(f"Successfully copied from {source} to {destination}")
        return content
    except FileNotFoundError:
        print("Source file not found.")

# Usage
content = copy_file("data.txt", "copy_of_data.txt")     # data.txt already exists from previous question.
print(content)

#======================================================================

'''Q20. Write a program to demonstrate file pointer operations using seek(). '''

# Create a file for demonstration
with open("seek_test.txt", "w") as f:
    f.write("Hello Python World")      # new file created.

with open("seek_test.txt", "r") as f:
    # Read first 5 characters
    print(f"First 5 chars: {f.read(5)}") 
    
    # Move pointer to the beginning of the file (offset 0)
    f.seek(0)
    print(f"After seek(0): {f.read(5)}")
    
    # Move pointer to index 6
    f.seek(6)
    print(f"From index 6: {f.read()}")