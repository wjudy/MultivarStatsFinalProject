import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.impute import SimpleImputer

# Load dataset
file_path = "life_expectancy.csv"
data = pd.read_csv(file_path)

# Convert the categorical variable "Status: to binary (0 for Developing, 1 for Developed)
data["Status"] = data["Status"].replace({"Developing": 0, "Developed": 1})

# Simple imputer for missing values
imputer = SimpleImputer(strategy="mean")

# Apply the imputer to the dataset (excluding the country and year columns)
data_imputed = pd.DataFrame(imputer.fit_transform(data.iloc[:, 2:]), columns=data.columns[2:])

# Combine the original country and year columns with the imputed data
data_imputed.insert(0, "Year", data["Year"])
data_imputed.insert(0, "Country", data["Country"])

# Calculate the average life expectancy for each year
average_life_expectancy_by_year = data_imputed.groupby("Year")["Life_expectancy"].mean().reset_index()

# Calculate the average life expectancy for each year for developing countries
average_life_expectancy_developing = data_imputed[data_imputed["Status"] == 0].groupby("Year")["Life_expectancy"].mean().reset_index()

# Calculate the average life expectancy for each year for developed countries
average_life_expectancy_developed = data_imputed[data_imputed["Status"] == 1].groupby("Year")["Life_expectancy"].mean().reset_index()


# # Plot the average life expectancy year over year for all countries
# plt.figure(figsize=(10, 6))
# sns.lineplot(x="Year", y="Life_expectancy", data=average_life_expectancy_by_year)
# plt.title("Average Life Expectancy Year Over Year - All Countries")
# plt.xlabel("Year")
# plt.ylabel("Life Expectancy")
# plt.show()

# # Plot the average life expectancy year over year for developing countries
# plt.figure(figsize=(10, 6))
# sns.lineplot(x="Year", y="Life_expectancy", data=average_life_expectancy_developing)
# plt.title("Average Life Expectancy Year Over Year - Developing Countries")
# plt.xlabel("Year")
# plt.ylabel("Life Expectancy")
# plt.show()

# # Plot the average life expectancy year over year for developed countries
# plt.figure(figsize=(10, 6))
# sns.lineplot(x="Year", y="Life_expectancy", data=average_life_expectancy_developed)
# plt.title("Average Life Expectancy Year Over Year - Developed Countries")
# plt.xlabel("Year")
# plt.ylabel("Life Expectancy")
# plt.show()

# Plot the average life expectancy year over year for all countries, developing countries, and developed countries on the same graph
plt.figure(figsize=(12, 8))
sns.lineplot(x="Year", y="Life_expectancy", data=average_life_expectancy_by_year, label="Total", lw=2)
sns.lineplot(x="Year", y="Life_expectancy", data=average_life_expectancy_developing, label="Developing", lw=1)
sns.lineplot(x="Year", y="Life_expectancy", data=average_life_expectancy_developed, label="Developed", lw=1)

plt.title("Average Life Expectancy Year Over Year")
plt.xlabel("Year")
plt.ylabel("Life Expectancy")
plt.ylim(0,100)
plt.legend()
plt.show()




# # Save a separate CSV file for each year from 2000 to 2015
# for year in range(2000, 2016):
#     # Filter the data for the current year
#     data_year = data_imputed[data_imputed["Year"] == year]
    
#     # Save the data for the current year to a CSV file
#     output_file_path = f"life_expectancy_{year}.csv"
#     data_year.to_csv(output_file_path, index=False)
#     print(f"Saved data for year {year} to {output_file_path}")
