📊 **Iris Dataset Analysis with Pandas & Matplotlib**
📌 **Description**

This project demonstrates how to analyze data using Pandas and visualize insights with Matplotlib.
We use the famous Iris dataset, a classic dataset for classification problems, which contains 150 samples of iris flowers with four features:

Sepal length

Sepal width

Petal length

Petal width

The flowers belong to three species: Setosa, Versicolor, and Virginica.

🎯 **Objectives**

Load and explore a dataset using Pandas.

Perform basic data analysis (statistics, grouping).

Create visualizations with Matplotlib.

Derive insights and observations from the dataset.

🛠️ **Technologies Used**

Python 3

Pandas

Matplotlib

scikit-learn (for loading the Iris dataset)

📂 **Project Structure**
week-7-assignment/
│── iris_analysis.py   # Main Python script
│── README.md          # Project documentation

🚀**How to Run**

Clone the repository:

git clone https://github.com/<your-username>/week-7-assignment.git
cd week-7-assignment


Install required libraries:

pip install pandas matplotlib scikit-learn


Run the script:

python iris_analysis.py

📊 **Features Implemented**
**✅ Task 1: Load and Explore Dataset**

Loaded the Iris dataset using sklearn.datasets.load_iris().

Converted it into a Pandas DataFrame.

Displayed first 5 rows with .head().

Checked data types and missing values with .info().

Handled missing values (none found in this dataset).

**✅ Task 2: Basic Data Analysis**

Used .describe() to calculate mean, median, std, min, max, quartiles.

Grouped by species and computed average petal length.

Observed that:

Setosa has the smallest petals.

Virginica has the largest petals.

Versicolor falls in between.

**✅ Task 3: Data Visualization**

Line Chart – Sepal length trends across samples.

Bar Chart – Average petal length per species.

Histogram – Distribution of petal length.

Scatter Plot – Relationship between sepal length and petal length.

Each plot includes:

Title

Axis labels

Legends where necessary

🔎 **Findings & Observations**

Clear separation between Setosa and the other two species based on petal size.

Virginica generally has the longest petals and sepals.

The dataset is well-structured with no missing values.

Scatter plots show strong correlations between features (useful for classification).

📸 **Example Visualizations**
Bar Chart: Average Petal Length per Species

✅ **Submission Requirements Covered**

✔️ Data loading and exploration
✔️ Basic analysis with statistics and grouping
✔️ Four different visualizations (line, bar, histogram, scatter)
✔️ Observations and findings documented

🤝 **Credits**

Dataset: Iris Dataset - UCI Machine Learning Repository

Libraries: Pandas, Matplotlib, Scikit-learn
