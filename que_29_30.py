''' Q29. Write a program using pandas to filter and group data. '''
import pandas as pd

# Sample Data
data = {
    'Department': ['HR', 'IT', 'IT', 'HR', 'IT'],
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Salary': [50000, 70000, 80000, 55000, 75000]
}
df = pd.DataFrame(data)

# 1. Filtering: Employees in IT
it_employees = df[df['Department'] == 'IT']
print("IT Department Employees:\n", it_employees)

# 2. Grouping: Average Salary by Department
avg_salary = df.groupby('Department')['Salary'].mean()
print("\nAverage Salary by Department:\n", avg_salary)


# =========================================================================


''' Q30. Write a program using matplotlib to plot line and bar graphs.'''
import matplotlib.pyplot as plt

# Data
months = ['Jan', 'Feb', 'Mar', 'Apr']
sales = [100, 150, 120, 200]

# 1. Line Graph
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.plot(months, sales, marker='o', color='blue')
plt.title('Line Graph: Sales Trend')
plt.xlabel('Month')
plt.ylabel('Sales')

# 2. Bar Graph
plt.subplot(1, 2, 2)
plt.bar(months, sales, color='green')
plt.title('Bar Graph: Sales Comparison')
plt.xlabel('Month')
plt.ylabel('Sales')

plt.tight_layout()
plt.show()