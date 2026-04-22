''' Q23. Demonstrate transaction control (commit and rollback) in database
operations. '''

import sqlite3

conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()

try:
    # Start a transaction
    cursor.execute("INSERT INTO students (name, age) VALUES ('Charlie', 20)")
    cursor.execute("INSERT INTO students (name, age) VALUES ('David', 22)")
    
    # Simulating an error to trigger rollback : 
    # eg. - cursor.execute("INSERT INTO students (name, age) VALUES (, 22)")
    # raise : Exception("Simulated error occurs here!")
    conn.commit()
    print("Transaction committed successfully.")
except Exception as e:
    conn.rollback()
    print(f"Transaction failed, rolled back changes. Error: {e}")
finally:
    conn.close()

# ========================================================================


''' Q24. Write a program to handle exceptions using try-except blocks.'''

try:
    num1 = int(input("Enter numerator: "))
    num2 = int(input("Enter denominator: "))
    result = num1 / num2
    print(f"Result: {result}")

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Invalid input, please enter integers only.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")