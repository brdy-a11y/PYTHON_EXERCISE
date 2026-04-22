'''Q17. Write a program to read contents of a file using read(), readline(), and readlines(). '''

# Create a dummy file for demonstration
with open("test.txt", "w") as f:
    f.write("L1: Python programming is funnn.\nL2: File handling too.\nL3: End of this file surely.")

# Reading file contents
print("--- Using read() for reading entire file) ---")
with open("test.txt", "r") as f:
    print(f.read())

print("\n--- Using readline() for reading line by line) ---")
with open("test.txt", "r") as f:
    print(f.readline(), end="")
    print(f.readline(), end="")

print("\n\n--- Using readlines() (Returns a list of lines) ---")
with open("test.txt", "r") as f:
    lines = f.readlines()
    print(lines)

# =================================================================================================


'''Q18. Write a program to write and append data to a file.'''

# Writing (Overwrites whatever is there in file initially)
with open("data.txt", "w") as f:
    f.write("This is the existing text in file initially.\n")

# Appending (Adds to existing file)
with open("data.txt", "a") as f:
    f.write("This is appended data using \"a\".")

# Verifiyingg : 
with open("data.txt", "r") as f:
    print(f"File content: {f.read()}")

