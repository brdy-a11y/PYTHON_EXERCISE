'''Q31. Write a program combining numpy, pandas, and matplotlib for simple data analysis'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. NumPy: Generate random data (e.g., 50 days of sales figures)
np.random.seed(42)
days = np.arange(1, 51)
# Simulate sales: base of 100 + random variation
sales = 100 + np.random.normal(0, 15, 50) 

# 2. Pandas: Create a DataFrame and perform analysis
df = pd.DataFrame({'Day': days, 'Sales': sales})

# Calculate rolling average (moving average)
df['Moving_Avg'] = df['Sales'].rolling(window=7).mean()

# 3. Matplotlib: Plotting the results
plt.figure(figsize=(10, 6))

# Plot raw sales and moving average
plt.plot(df['Day'], df['Sales'], label='Daily Sales', color='lightgray', alpha=0.7)
plt.plot(df['Day'], df['Moving_Avg'], label='7-Day Moving Average', color='blue', linewidth=2)

plt.title('Sales Trend Analysis')
plt.xlabel('Day')
plt.ylabel('Units Sold')
plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)

plt.show()

# Displaying statistical summary
print("--- Sales Statistics ---")
print(df[['Sales']].describe())