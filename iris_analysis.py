# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Step 1: Load and Explore the Dataset
# Load Iris dataset
iris = load_iris()
data = pd.DataFrame(iris.data, columns=iris.feature_names)
data['species'] = iris.target
data['species'] = data['species'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})

# Display first few rows
print("First 5 rows of the dataset:")
print(data.head())

# Check data structure and missing values
print("\nDataset Info:")
print(data.info())
print("\nMissing Values Count:")
print(data.isnull().sum())

# Step 2: Basic Data Analysis
# Basic statistics
print("\nBasic Statistics:")
print(data.describe())

# Grouping by species and computing mean of petal length
species_avg = data.groupby('species')['petal length (cm)'].mean()
print("\nAverage Petal Length by Species:")
print(species_avg)

# Step 3: Data Visualization
# 1. Line Chart
plt.plot(data.index, data['petal length (cm)'], label='Petal Length', color='blue')
plt.title('Petal Length Over Index')
plt.xlabel('Index')
plt.ylabel('Petal Length (cm)')
plt.legend()
plt.show()

# 2. Bar Chart
species_avg.plot(kind='bar', color=['blue', 'green', 'red'])
plt.title('Average Petal Length by Species')
plt.xlabel('Species')
plt.ylabel('Average Petal Length (cm)')
plt.show()

# 3. Histogram
plt.hist(data['sepal length (cm)'], bins=10, color='purple', alpha=0.7)
plt.title('Distribution of Sepal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Frequency')
plt.show()

# 4. Scatter Plot
sns.scatterplot(x='sepal length (cm)', y='petal length (cm)', hue='species', data=data)
plt.title('Sepal Length vs. Petal Length')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Petal Length (cm)')
plt.show()
