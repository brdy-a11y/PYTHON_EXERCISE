''' Question 21. Write a program to connect to a database and create a table. '''
import sqlite3

# 1. Connect to database (also it creates file if it doesn't exist)
conn = sqlite3.connect('my_database.db')

# 2. Create a cursor object
cursor = conn.cursor()  # to be able to run commands

# 3. Create a table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        age INTEGER
    )
''')

print("Table 'students' created successfully.")

# 4. Commit changes and close connection
conn.commit()
conn.close()


# ====================================================================

''' Question 22. Write a program to perform INSERT, UPDATE, DELETE,
and SELECT operations on a database. '''

import sqlite3

# Connect to the existing database
conn = sqlite3.connect('my_database.db')
cursor = conn.cursor()

# 1. INSERT Operation
cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", ("Alice", 21))
cursor.execute("INSERT INTO students (name, age) VALUES (?, ?)", ("Bob", 22))
conn.commit()
print("Records inserted successfully.")

# 2. SELECT Operation
print("\n--- Current Data ---")
cursor.execute("SELECT * FROM students")
for row in cursor.fetchall():
    print(row)

# 3. UPDATE Operation
cursor.execute("UPDATE students SET age = ? WHERE name = ?", (25, "Alice"))
conn.commit()
print("\nRecord updated: Alice's age changed to 25.")

# 4. DELETE Operation
cursor.execute("DELETE FROM students WHERE name = ?", ("Bob",))
conn.commit()
print("Record deleted: Bob removed from table.")

# Final check
print("\n--- Final Data ---")
cursor.execute("SELECT * FROM students")
print(cursor.fetchall())

conn.close()