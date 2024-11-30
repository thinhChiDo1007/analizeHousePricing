# Re-importing necessary libraries and data due to system reset
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Reload the data
data = pd.read_excel("MELBOURNE_HOUSE_PRICES_LESS.csv")

# Set the aesthetic style of the plots
sns.set(style="whitegrid")

# Create a histogram for the 'Price' distribution
plt.figure(figsize=(10, 6))
sns.histplot(data[data['Price'].notnull()]['Price'], bins=30, kde=True)
plt.title('Distribution of House Prices')
plt.xlabel('Price')
plt.ylabel('Frequency')
plt.show()

# Create a box plot to show house prices by Region
plt.figure(figsize=(12, 8))
sns.boxplot(x='Regionname', y='Price', data=data)
plt.xticks(rotation=45)
plt.title('House Prices by Region')
plt.xlabel('Region')
plt.ylabel('Price')
plt.show()

# Create a scatter plot to show the relationship between 'Distance' and 'Price'
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Distance', y='Price', data=data)
plt.title('Price vs. Distance from CBD')
plt.xlabel('Distance (km)')
plt.ylabel('Price')
plt.show()