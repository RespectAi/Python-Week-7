# Task 1

import pandas as pd

# Load CSV file
df = pd.read_csv('C:/Users/Admin/Downloads/tableConvert.com_r7v5ww.csv')  # Replace with your file path

# Display the first 5 rows
print(df.head())

pd.set_option('display.max_rows', None)  # Show all rows
pd.set_option('display.max_columns', None)  # Show all columns
print(df)

# Check column names and data types
print(df.info())

# Summary statistics
print(df.describe())

# Update row 0
df.loc[0, 'sepal_length'] = 5.3  # Updates 5.1 → 5.3

# Update row 5
df.loc[5] = [5.5, 3.8, 1.6, 0.3, 'setosa']

# Print the updated rows to confirm
print("Row 0 after update:\n", df.loc[0])
print("\nRow 5 after update:\n", df.loc[5])

df.to_csv('temp.csv', index=False)
df = pd.read_csv('temp.csv')

# Task 2

import pandas as pd

# Load your CSV file
file_path = "C:/Users/Admin/Documents/PLP Febuary Chort/Python2/Python Assignments/Python-Week-7/temp.csv"
df = pd.read_csv(file_path)

# Drop the 'species' column (non-numeric)
numerical_df = df.drop('species', axis=1)

# Calculate statistics
mean = numerical_df.mean()
median = numerical_df.median()
std_dev = numerical_df.std()

# Mode (handles multiple modes or no mode)
mode = numerical_df.mode().iloc[0]  # Takes the first mode if multiple exist

# Combine results into a summary DataFrame
summary_df = pd.DataFrame({
     'Mean': mean,
     'Median': median,
     'Mode': mode,
     'Standard Deviation': std_dev
})

print(summary_df)

import pandas as pd

# Load the CSV file
df = pd.read_csv('temp.csv')

# Group by 'species' and calculate the mean of all numerical columns
grouped_mean = df.groupby('species').mean().round(2)  # Rounded to 2 decimals
print(grouped_mean)

# Group by petal_length 
petal_length_mean = df.groupby('species')['petal_length'].mean().round(2)
print("\nPetal Length Mean:\n", petal_length_mean)

# Group by petal_width
petal_width_mean = df.groupby('species')['petal_width'].mean().round(2)
print("\nPetal Width Mean:\n", petal_width_mean)

# Group by petal_sepal_length
sepal_length_mean = df.groupby('species')['sepal_length'].mean().round(2)
print("\nSepal Length Mean:\n", sepal_length_mean)

# Group by petal_sepal_width
sepal_width_mean = df.groupby('species')['sepal_width'].mean().round(2)
print("\nSepal Width Mean:\n", sepal_width_mean)



###  Identify any patterns or interesting findings from your analysis.

print("\n 3. Identify any patterns or interesting findings from your analysis.")

print ("1. Distinct Clustering by Species \n\n")
print("The three species show clear separations in their mean measurements, making them ideal for classification tasks.\n ")

print("  Feature \t	setosa versicolor virginica\n")
print("Sepal Length (cm)	4.99	5.94	6.59\n")
print("Sepal Width (cm)	3.42	2.77	2.97\n")
print("Petal Length (cm)	1.47	4.26	5.55\n")
print("Petal Width (cm)	0.24	1.33	2.03\n")
print("Key Observations:\n")
print("Virginica has the longest sepals and largest petals.\n")
print("Setosa has the widest sepals and smallest petals.\n")
print("Versicolor sits between the two in all measurements.\n\n")

print("2. Petal Dimensions Are Most Discriminative\n")
print("Petal length and width show the largest differences across species:\n")
print("Setosa: Petals are tiny (1.47 cm long, 0.24 cm wide).\n")
print("Virginica: Petals are 3–4x larger (5.55 cm long, 2.03 cm wide).\n")
print("This aligns with why petal features are often used to classify Iris species in ML models.\n\n")


print("3. Sepal Width vs. Length Trade-off\n")
print("Setosa prioritizes sepal width over length:\n")
print("Sepal width = 3.42 cm (highest), length = 4.99 cm (lowest).\n")
print("Virginica prioritizes sepal length over width:\n")
print("Sepal length = 6.59 cm (highest), width = 2.97 cm.\n\n")

print("4. Low Variance in Setosa\n")
print("Setosa has the least variability in measurements (smallest standard deviations):\n")
print("Petal width: 0.11 cm (vs. 0.20 cm for virginica).\n")
print("Suggests setosa is more uniform compared to other species.\n\n")

print("5. Virginica Shows Highest Petal Width Variability\n")  
print("Virginica has the largest spread in petal width (std = 0.27 cm), indicating natural diversity in this trait.\n")

# Task 3

