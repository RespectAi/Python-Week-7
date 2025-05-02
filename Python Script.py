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
# line chart
print("\n\nTask 3: Data Visualization\n\n")
print("Line chat: Test Across Observation Line Chart \n\n")
print("import pandas as pd\n")
print("import matplotlib.pyplot as plt\n")

print("file_path = 'tableConvert.com_r7v5ww.csv'\n")

print("# Load the CSV\n")
print("df = pd.read_csv(file_path)\n")

print("# Plot trends\n")
print("plt.figure(figsize=(12, 6))\n")
print("for column in ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']:\n")
print("plt.plot(df.index, df[column], marker='o', linestyle='--', label=column)\n")

print("plt.title('Attribute Trends Across Observations')\n")
print("plt.xlabel('Observation Index (Row)')\n")
print("plt.ylabel('Measurement (cm)')\n")
print("plt.legend()\n")
print("plt.grid(True)\n")
print("plt.show()\n")

# line chart explanation
print("\n1. Test Across Observation Line Chart\n")
print("This chart plots numerical attributes (e.g., sepal length, petal width) against the observation index (row number) in your dataset. Since our Iris dataset lacks a time-based column, the row index acts as a pseudo-sequence to visualize trends or anomalies across entries.\n")
print("Purpose\n")
print("Identify Outliers: Detect unusual values (e.g., a sepal_length of 7.0 for a setosa in row 49).\n")
print("Spot Patterns: Observe if measurements fluctuate randomly or follow a hidden trend (e.g., data sorted by size).\n")
print("Data Quality Check: Ensure consistency (e.g., petal widths should not spike randomly unless valid).\n\n")

print("Interpretation\n")
print("X-axis: Observation index (row number, 0 to N).\n")
print("Y-axis: Measurement values (in cm) for each attribute.\n")
print("Lines: Each line represents a numerical column (e.g., sepal_length).\n")

# Pairwise Relationship Chart (Pair Plot)
print("2. Pairwise Relationship Chart (Pair Plot)\n\n")

print("sns.pairplot(df, hue='species')\n")
print("plt.show()\n")

# Pairwise Relationship Chart (Pair Plot) explanation
print("\n2. Pairwise Relationship Chart (Pair Plot)\n")
print("A pair plot is a grid of scatterplots that visualize relationships between all pairs of numerical columns in your dataset. It’s a powerful tool for exploring correlations and clustering by species.\n")
print("Purpose\n")
print("Correlation Analysis: Identify linear/non-linear relationships (e.g., petal length vs. petal width).\n")
print("Cluster Detection: See if species naturally group in 2D space (e.g., setosa vs. virginica).\n")
print("Distribution Check: Diagonal histograms show the distribution of each attribute.\n")
print("interpretation\n")

print("\bGrid Structure:\n")
print("Rows/Columns: Numerical attributes (e.g., sepal_length, petal_length).\n")
print("Diagonal: Histograms of each attribute.\n")
print("Off-Diagonal: Scatterplots of attribute pairs.\n")

#Bar Chart

print("Bar Chart\n\n")
print("Mean median and standard deviation of each species\n\n")

print("import pandas as pd\n")
print("import matplotlib.pyplot as plt\n")

print("# Load the dataset\n")
print("df = pd.read_csv('tableConvert.com_r7v5ww.csv')\n")

print("# Group by species and calculate statistics\n")
print("grouped = df.groupby('species').agg(['mean', 'median', 'std']).round(2)\n")
print("species = grouped.index.tolist()  # ['setosa', 'versicolor', 'virginica']\n")
print("numerical_cols = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']\n")

print("# Define colors for numerical columns\n")
print("colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728']  # Blue, Orange, Green, Red\n")

print("# Create a 3x3 grid (3 species × 3 statistics)\n")
print("fig, axes = plt.subplots(3, 3, figsize=(20, 15))\n")
print("plt.subplots_adjust(hspace=0.4, wspace=0.3)\n")

print("# Plot for each species and statistic\n")
print("for row, species_name in enumerate(species):\n")
print("    # Mean\n")
print("    axes[row, 0].bar(numerical_cols, grouped.loc[species_name].xs('mean', level=1), color=colors)\n")
print("    axes[row, 0].set_title(f'{species_name} - Mean', fontsize=12)\n")
print("    axes[row, 0].set_ylabel('Mean (cm)')\n")
print("    axes[row, 0].grid(axis='y', linestyle='--', alpha=0.7)\n")
    
print("    # Median\n")
print("    axes[row, 1].bar(numerical_cols, grouped.loc[species_name].xs('median', level=1), color=colors)\n")
print("    axes[row, 1].set_title(f'{species_name} - Median', fontsize=12)\n")
print("    axes[row, 1].set_ylabel('Median (cm)')\n")
print("   axes[row, 1].grid(axis='y', linestyle='--', alpha=0.7)\n")
    
print("    # Standard Deviation\n")
print("    axes[row, 2].bar(numerical_cols, grouped.loc[species_name].xs('std', level=1), color=colors)\n")
print("    axes[row, 2].set_title(f'{species_name} - Standard Deviation', fontsize=12)\n")
print("    axes[row, 2].set_ylabel('Std Dev (cm)')\n")
print("    axes[row, 2].grid(axis='y', linestyle='--', alpha=0.7)\n")

print("# Add legend (use first subplot for legend)\n")
print("handles = [plt.Rectangle((0,0),1,1, color=colors[i]) for i in range(len(numerical_cols))]\n")
print("fig.legend(handles, numerical_cols, loc='upper right', bbox_to_anchor=(0.99, 0.99), title='Attributes')\n")

print("plt.suptitle('Statistical Comparison by Species and Attribute', fontsize=16)\n")
print("plt.show()\n")

# Bar Chart explanation
print("1. Detailed Explanation of Mean, Median, and Standard Deviation Charts\n")
print("These charts visualize key statistical measures (mean, median, and standard deviation) for each numerical attribute (sepal length, sepal width, petal length, petal width) across the three Iris species (setosa, versicolor, virginica).\n")
print("Mean Chart\n")
print("What It Shows: The average value of each attribute for a species.\n")
print("Interpretation:\n")
print("Example: For virginica, the mean petal_length is 5.55 cm, indicating larger petals compared to setosa (1.47 cm).\n")
print("Use Case: Compare central tendencies across species.\n")

print("Median Chart\n")
print("What It Shows: The middle value of each attribute when sorted.\n")
print("Interpretation:\n")
print("Example: The median sepal_width for setosa is 3.42 cm, matching its mean, suggesting a symmetric distribution.\n")
print("Use Case: Identify skewness (if mean ≠ median).\n")

print("Standard Deviation Chart\n")
print("What It Shows: The spread/variability of data points around the mean.\n")
print("Interpretation:\n")
print("Example: virginica has the highest SD in petal_width (0.27 cm), meaning petal widths vary widely.\n")
print("Use Case: Assess data consistency.\n")

# Histogram
print("\n\n Histogram\n")
print(" Histogram of each species \n\n")

print("import pandas as pd\n")
print("import matplotlib.pyplot as plt\n")
print("import numpy as np\n")

print("# Load the dataset\n")
print("df = pd.read_csv('tableConvert.com_r7v5ww.csv')\n")

print("# Define features and species\n")
print("features = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']\n")
print("species = df['species'].unique()\n")

print("# Create subplots\n")
print("fig, axes = plt.subplots(3, 4, figsize=(20, 12))\n")
print("plt.subplots_adjust(hspace=0.4, wspace=0.3)\n")

print("# Plot histograms for each species and feature\n")
print("for row, sp in enumerate(species):\n")
print("    species_df = df[df['species'] == sp]\n")
print("    for col, feature in enumerate(features):\n")
print("        ax = axes[row, col]\n")
print("        data = species_df[feature]\n")
        
print("        # Calculate histogram bins and counts\n")
print("        counts, bins = np.histogram(data, bins=15)\n")
print("        max_bin_idx = np.argmax(counts)\n")
print("        mode_lower = bins[max_bin_idx]\n")
print("        mode_upper = bins[max_bin_idx + 1]\n")
        
print("        # Plot histogram\n")
print("        ax.hist(data, bins=15, color='skyblue', edgecolor='black', alpha=0.7)\n")
print("        ax.axvspan(mode_lower, mode_upper, color='red', alpha=0.3, label=f'Mode: {mode_lower:.1f}-{mode_upper:.1f}')\n")
print("        ax.set_title(f'{sp} - {feature}', fontsize=10)\n")
print("        ax.set_xlabel(f'{feature} (cm)')\n")
print("        ax.set_ylabel('Frequency')\n")
print("        ax.legend()\n")

print("plt.suptitle('Modal Intervals (Most Frequent Bins) for Each Species and Feature', fontsize=14, y=1.02)\n")
print("plt.show()\n")


# Histogram explanation
print("1. Histogram of Each Species\n")
print("The histograms visualize the distribution of measurements (sepal length, sepal width, petal length, petal width) for each Iris species (setosa, versicolor, virginica). The mode (most frequent value range) is highlighted in red for each feature.\n")
print("1. Histogram Structure\n")
print("X-axis: Measurement values (e.g., sepal length in cm).\n")
print("Y-axis: Frequency (number of observations in each bin).\n")
print("Bins: 15 intervals (ranges) dividing the data.\n")
print("Red Shading: Highlights the modal interval (bin with the highest frequency).\n")


#Scatter Plot
print("\n\nScatter Plot\n")
print("Scatter plot of petal length vs petal width\n\n")

print("import pandas as pd\n")
print("import matplotlib.pyplot as plt\n")
print("import seaborn as sns\n")

print("# Load the dataset\n")
print("df = pd.read_csv('tableConvert.com_r7v5ww.csv')\n")

print("# Create a scatter plot\n")
print("plt.figure(figsize=(10, 6))\n")
print("sns.scatterplot(\n")
print("    data=df,\n")
print("    x='petal_length',\n")
print("    y='petal_width',\n")
print("    hue='species',\n")
print("    palette=['blue', 'orange', 'green'],\n")
print("    s=100,  # Size of points\n")
print("    alpha=0.8  )\n")


print("plt.title('Petal Length vs. Petal Width by Species', fontsize=14)\n")
print("plt.xlabel('Petal Length (cm)', fontsize=12)\n")
print("plt.ylabel('Petal Width (cm)', fontsize=12)\n")
print("plt.grid(True, linestyle='--', alpha=0.3)\n")
print("plt.legend(title='Species')\n")
print("plt.show()\n")

# Scatter Plot explanation
print("1. Petal Length vs. Petal Width Scatter Plot\n")
print("This scatter plot visualizes the relationship between petal length (x-axis) and petal width (y-axis) for the three Iris species (setosa, versicolor, virginica).\n")

print("1. Key Components\n")
print("X-axis: Petal Length (cm) – Measures the length of petals.\n")
print("Y-axis: Petal Width (cm) – Measures the width of petals.\n")
print("Color Coding:\n")
print("Blue: setosa\n")
print("Orange: versicolor\n")
print("Green: virginica\n")
print("Each Point: Represents one flower (row) in the dataset.\n")