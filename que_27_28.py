'''Q27. Write a program using numpy to perform array operations (creation, indexing, arithmetic).'''

import numpy as np

# 1. Creation
arr = np.array([1, 2, 3, 4, 5])
print(f"Original Array: {arr}")

# 2. Indexing
print(f"Element at index 2: {arr[2]}")

# 3. Arithmetic Operations (Vectorized)
arr_sum = arr + 10
arr_mul = arr * 2

print(f"Array + 10: {arr_sum}")
print(f"Array * 2:  {arr_mul}")


# ======================================================================================================


''' Q28. Write a program using pandas to read a CSV file and perform
basic analysis. '''

import pandas as pd

# Creating a dummy 'employees.csv' file for this example
data = {'Name': ['Raman', 'Abdul', 'Sanya'], 'Age': [25, 30, 35], 'Salary': [50000, 60000, 70000]}
pd.DataFrame(data).to_csv('employees.csv', index=False)

# 1. Reading the CSV file
df = pd.read_csv('employees.csv')

# 2. Basic Analysis
print("--- Data Overview ---")
print(df.head()) # Displays the first 5 rows

print("\n--- Statistical Summary ---")
print(df.describe()) # Provides count, mean, std, min, max, etc.