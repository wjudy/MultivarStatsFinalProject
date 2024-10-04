import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
file_path = "life_expectancy.csv"
data = pd.read_csv(file_path)

# Print the first 5 rows
print("Original data:")
print(data.head())

# Simple imputer for missing values
from sklearn.impute import SimpleImputer

# Create a SimpleImputer object and specify the strategy (e.g., mean, median, or most_frequent)
imputer = SimpleImputer(strategy="mean")

# Apply the imputer to the dataset (excluding the country and year columns)
data_imputed = pd.DataFrame(imputer.fit_transform(data.iloc[:, 3:]), columns=data.columns[3:])

# Combine the original country and year columns with the imputed data
data_imputed.insert(0, "Status", data["Status"])
data_imputed.insert(0, "Year", data["Year"])
data_imputed.insert(0, "Country", data["Country"])


# Print the first 5 rows of the imputed data
print("\nImputed data:")
print(data_imputed.head())

# Segment the data by country and year
data_grouped = data_imputed.groupby(["Country", "Year", "Status"]).mean()
print("\nData segmented by country, year, and status:")
print(data_grouped.head())

# Reset the index to make the country and year columns available for further analysis
data_grouped.reset_index(inplace=True)

# Perform exploratory data analysis (EDA)
# Basic statistics
print("\nBasic statistics:")
print(data_grouped.describe())

# Check for correlations between variables
correlation_matrix = data_grouped.corr()
print("\nCorrelation matrix:")
print(correlation_matrix)

# Visualize the correlation matrix using a heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation heatmap")
plt.show()

# Histogram of life expectancy
plt.figure(figsize=(8, 6))
sns.histplot(data_grouped["Life_expectancy"], kde=True, bins=20)
plt.title("Life Expectancy Distribution")
plt.xlabel("Life Expectancy")
plt.ylabel("Frequency")
plt.show()

# Box plot of life expectancy by region (if region column exists in dataset)
if "Region" in data.columns:
    plt.figure(figsize=(12, 6))
    sns.boxplot(x="Region", y="Life_expectancy", data=data_grouped)
    plt.title("Life Expectancy by Region")
    plt.xlabel("Region")
    plt.xticks(rotation=45)
    plt.ylabel("Life Expectancy")
    plt.show()
