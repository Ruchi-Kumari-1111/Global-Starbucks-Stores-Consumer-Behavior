import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

# Hiding unnecessary background warnings
warnings.filterwarnings('ignore')

# Dynamically find the path of the folder containing this script
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'starbucks_store_locations.csv')

# 1. Dataset Load Kijiye
print("Data load ho raha hai, please wait...\n")
df = pd.read_csv(file_path, encoding='latin1')

print("--- Starbucks Global Dataset Preview ---")
print(df.head().to_string()) 


# ==========================================
# 2. Summary Statistics
# ==========================================
print("\n" + "="*50)
print("--- 1. Dataset General Info ---")
df.info()

print("\n--- 2. High-Level Summary ---")
print(df.describe(include='all'))

print("\n--- 3. Top 10 Countries with Most Starbucks Stores ---")
print(df['Country'].value_counts().head(10))

print("\n--- 4. Store Distribution by Ownership Type ---")
print(df['Ownership Type'].value_counts())
print("="*50 + "\n")


# ==========================================
# 3. Histogram (Bar Distribution)
# ==========================================
plt.figure(figsize=(9, 5))
sns.countplot(data=df, x='Ownership Type', hue='Ownership Type', order=df['Ownership Type'].value_counts().index, palette='viridis')

plt.title('Global Distribution of Starbucks Ownership Types', fontsize=14, fontweight='bold')
plt.xlabel('Ownership Type', fontsize=12)
plt.ylabel('Number of Stores', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.5)

# Saving Graph 1 to the Task-2 folder
graph1_path = os.path.join(script_dir, '1_ownership_distribution.png')
plt.savefig(graph1_path, bbox_inches='tight', dpi=300)
print(f"💾 Graph 1 saved successfully at: {graph1_path}")

print("\n📊 Graph 1 Open ho raha hai... (Explanation graph band karne ke baad aayegi)")
plt.show() 

print("\n📊 Graph Explanation (Distribution):")
print("- Tallest Bar (Dark Blue/Purple): Represents the most common ownership type globally (usually Company Owned or Licensed).")
print("- Shorter Bars (Green/Yellow): Represent less common types like Joint Ventures or Franchises.")
print("- Insight: This visually proves which business model Starbucks relies on the most for global expansion.")


# ==========================================
# 4. Boxplot (Outlier Detection)
# ==========================================
plt.figure(figsize=(10, 5))
sns.boxplot(data=df, x='Ownership Type', y='Longitude', hue='Ownership Type', palette='Set2')

plt.title('Geographical Spread & Outlier Detection (Longitude)', fontsize=14, fontweight='bold')
plt.xlabel('Ownership Type', fontsize=12)
plt.ylabel('Longitude Value', fontsize=12)

# Saving Graph 2 to the Task-2 folder
graph2_path = os.path.join(script_dir, '2_geographical_spread_boxplot.png')
plt.savefig(graph2_path, bbox_inches='tight', dpi=300)
print(f"💾 Graph 2 saved successfully at: {graph2_path}")

print("\n📊 Graph 2 Open ho raha hai... (Agle code ke liye window close kijiye)")
plt.show()

print("\n📊 Graph Explanation (Boxplot):")
print("- The Colored Boxes: Represent where the majority (middle $50\\%$) of Starbucks stores are clustered.")
print("- The Horizontal Line inside the box: Shows the median (average) location.")
print("- The Black Dots: These represent OUTLIERS! Extreme or isolated geographic coordinates.")
print("- Insight: Shows if 'Licensed' stores are spread wider than 'Company Owned'.")


# ==========================================
# 5. Correlation Matrix
# ==========================================
plt.figure(figsize=(6, 4))
numeric_matrix = df[['Latitude', 'Longitude']].dropna().corr()
sns.heatmap(numeric_matrix, annot=True, cmap='coolwarm', fmt=".2f", vmin=-1, vmax=1)

plt.title('Starbucks Coordinate Dependency Matrix', fontsize=12, fontweight='bold')

# Saving Graph 3 to the Task-2 folder
graph3_path = os.path.join(script_dir, '3_coordinate_correlation_heatmap.png')
plt.savefig(graph3_path, bbox_inches='tight', dpi=300)
print(f"💾 Graph 3 saved successfully at: {graph3_path}")

print("\n📊 Graph 3 Open ho raha hai... (Agle code ke liye window close kijiye)")
plt.show()

print("\n📊 Graph Explanation (Correlation):")
print("- Deep Red Color ($+1.00$): Perfect positive correlation.")
print("- Lighter Colors / Blue Shades: Weaker or negative correlation.")
print("- Inside the Boxes: Exact mathematical relationship between Latitude and Longitude.")


# ==========================================
# 6. Pairplot Pattern Recognition
# ==========================================
g = sns.pairplot(df, hue='Ownership Type', palette='husl', diag_kind='kde')
g.fig.suptitle('Global Starbucks Expansion Pattern Recognition', y=1.02, fontsize=14, fontweight='bold')

# Saving Graph 4 to the Task-2 folder
graph4_path = os.path.join(script_dir, '4_expansion_pattern_pairplot.png')
g.savefig(graph4_path, bbox_inches='tight', dpi=300)
print(f"💾 Final Graph saved successfully at: {graph4_path}")

print("\n📊 Final Graph (Pairplot) Open ho raha hai... (Analysis Complete karne ke liye close kijiye)")
plt.show()

print("\n📊 Graph Explanation (Pairplot):")
print("- Diagonal Curves (Mountains): Show highest density of stores for each ownership type.")
print("- Scatter Dots (Grid): Show geographical overlapping of different store types.")
print("- Insight: Helps identify regional dominance of specific business models.")
print("\n✅ Task 2 Analysis Successfully Completed!")