# Task-2 ☕ Idea 2: Global Starbucks Stores & Consumer Behavior (EDA)

## Project Objective
The goal of this project is to perform a comprehensive **Exploratory Data Analysis (EDA)** on the Starbucks Global Dataset to uncover hidden patterns, trends, operational structures, and geographical anomalies using advanced descriptive statistics and data visualization tools.

* **Domain:** Business Analytics & Spatial Data Analysis
* **Tools Used:** Python, Pandas, NumPy, Matplotlib, Seaborn

---

## 📂 Repository Structure
```text
├── starbucks_eda.py                   # Main Python analysis script
├── starbucks_store_locations.csv       # Source Dataset
├── Screenshots/                       # Subfolder containing runtime outputs
│   ├── 1.png                          # Dataset Preview
│   ├── 2.png                          # Dataset General Info
│   ├── 3.png                          # Statistical Summary Table
│   ├── 4.png                          # Top Countries List
│   ├── 5.png                          # Ownership Distribution Counts
│   ├── 1_ownership_distribution.png   # Bar Chart Output
│   ├── 2_geographical_spread_boxplot.png # Boxplot Output
│   ├── 3_coordinate_correlation_heatmap.png # Heatmap Output
│   └── 4_expansion_pattern_pairplot.jpg # Pairplot Output
└── README.md                          # Project Documentation (This file)
```

---

## ⚙️ Data Preprocessing & Summary Statistics

### 1. Dataset Preview
When loading the dataset, the first 5 records were printed to inspect the primary structure, verifying properties like store names, categories, and geocodes.

```python
df.head()
```
![Dataset Preview](Screenshots/1.png)

### 2. General Dataset Structure
Using structural metadata inspections, the dataset was confirmed to hold **25,600 unique store entries** across 13 unique information columns.

```python
df.info()
```
![Dataset Info](Screenshots/2.png)

### 3. High-Level Summary Statistics
A comprehensive multi-variable summary table highlights boundaries, means, standard deviations, and quartile markers for numerical coordinates.

```python
df.describe(include='all')
```
![High Level Summary](Screenshots/3.png)

### 4. Market Penetration Check (Top 10 Countries)
An aggregation breakdown isolates which sovereign regions handle the densest operational clusters.

```python
df['Country'].value_counts().head(10)
```
![Top Countries List](Screenshots/4.png)
> **Key Metric:** The United States leadingly hosts **13,608 locations**, followed directly by China at **2,734 locations**.

---

## 📊 Visualizations & Business Inferences

### 1. Distribution of Ownership Models (Histogram/Countplot)
Tracks how ownership models differ across global corporate pipelines.

![Ownership Model Distribution](Screenshots/1_ownership_distribution.png)

* **Analysis Insight:** The chart visually demonstrates that **Company Owned** and **Licensed** stores serve as the core engines behind Starbucks' massive international expansion strategy, while franchises handle the minor share.
* **Data Split Reference:**
    ![Ownership Counts](Screenshots/5.png)

### 2. Geographical Spread Analysis & Outlier Detection (Boxplot)
Maps numerical longitude fields grouped by operational business frameworks to detect anomalies.

![Geographical Boxplot](Screenshots/2_geographical_spread_boxplot.png)

* **Analysis Insight:** The colored rectangular boxes highlight where the core 50% mass of store locations exist. The isolated individual black dots plotted far beyond the horizontal whiskers indicate **statistical outliers**—isolated stores operating in extreme regions or far-off islands separate from common corporate territories.

### 3. Coordinate Dependency Matrix (Heatmap)
Evaluates linear relationships between spatial coordinates.

![Correlation Heatmap](Screenshots/3_coordinate_correlation_heatmap.png)

* **Analysis Insight:** The heatmap yields a mild negative correlation score of **-0.28** between Latitude and Longitude. This mathematical value confirms that a store's horizontal axis position fluctuates independently from its vertical coordinates, showing no clustered global linear path.

### 4. Regional Expansion Patterns (Pairplot)
Combines multi-variable scatter grids and internal smooth kernel density plots to track global overlaps.

![Expansion Pairplot](Screenshots/4_expansion_pattern_pairplot.jpg)

* **Analysis Insight:** The smooth mountain curves cutting diagonally across the chart highlight the exact geographic peaks where regional store counts group tightest. The scattered data point spreads create an organic visual map of the globe, indicating clean geographic partitions among corporate ownership frameworks.
