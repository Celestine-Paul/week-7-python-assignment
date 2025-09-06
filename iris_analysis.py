# ------------------------------------------------------------
# 📊 Analyzing Data with Pandas & Visualizing with Matplotlib
# Dataset: Iris Dataset
# ------------------------------------------------------------

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# ------------------------------------------------------------
# Task 1: Load and Explore the Dataset
# ------------------------------------------------------------
try:
    # Load dataset from sklearn
    iris = load_iris(as_frame=True)
    df = iris.frame  # converts to pandas DataFrame
    df['species'] = df['target'].map(dict(enumerate(iris.target_names)))  # add species column

    print("✅ Dataset loaded successfully!\n")
except FileNotFoundError:
    print("❌ File not found. Please check your dataset path.")
except Exception as e:
    print("⚠️ Error loading dataset:", e)

# Display first 5 rows
print("📌 First 5 rows of the dataset:")
print(df.head(), "\n")

# Data info
print("📌 Dataset Info:")
print(df.info(), "\n")

# Missing values
print("📌 Missing Values:")
print(df.isnull().sum(), "\n")

# (No missing values in Iris dataset, but we include handling step)
df = df.dropna()

# ------------------------------------------------------------
# Task 2: Basic Data Analysis
# ------------------------------------------------------------

# Basic statistics
print("📌 Basic Statistics:")
print(df.describe(), "\n")

# Group by species and compute mean
print("📌 Mean values grouped by species:")
group_means = df.groupby('species').mean(numeric_only=True)
print(group_means, "\n")

# Observations
print("📌 Observations:")
print("- Iris-virginica tends to have the largest petals and sepals.")
print("- Iris-setosa generally has the smallest dimensions.\n")

# ------------------------------------------------------------
# Task 3: Data Visualization
# ------------------------------------------------------------

sns.set(style="whitegrid")  # better styling

# 1. Line chart - sepal length trend across samples
plt.figure(figsize=(8, 5))
plt.plot(df['sepal length (cm)'], label='Sepal Length')
plt.title("Line Chart: Sepal Length Trend")
plt.xlabel("Sample Index")
plt.ylabel("Sepal Length (cm)")
plt.legend()
plt.show()

# 2. Bar chart - average petal length per species
plt.figure(figsize=(8, 5))
sns.barplot(x="species", y="petal length (cm)", data=df, ci=None, palette="Set2")
plt.title("Bar Chart: Average Petal Length per Species")
plt.xlabel("Species")
plt.ylabel("Average Petal Length (cm)")
plt.show()

# 3. Histogram - distribution of sepal width
plt.figure(figsize=(8, 5))
plt.hist(df["sepal width (cm)"], bins=15, color="skyblue", edgecolor="black")
plt.title("Histogram: Sepal Width Distribution")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter plot - Sepal length vs Petal length
plt.figure(figsize=(8, 5))
sns.scatterplot(x="sepal length (cm)", y="petal length (cm)", hue="species", data=df, palette="Set1")
plt.title("Scatter Plot: Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.legend(title="Species")
plt.show()

# ------------------------------------------------------------
# End of Assignment
# ------------------------------------------------------------
print("🎉 Analysis and Visualization complete!")
