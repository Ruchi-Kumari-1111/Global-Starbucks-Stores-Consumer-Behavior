# ☕ Global Starbucks Stores & Consumer Behavior (EDA)

## 📌 Project Objective
The goal of this task is to perform Exploratory Data Analysis (EDA) on the Global Starbucks Store Locations dataset. Using Python (`pandas`, `seaborn`, `matplotlib`), this project uncovers business expansion patterns, geographical distributions, and structural anomalies.

---

## 📊 1. Data Summary & High-Level Statistics
First, we analyzed the raw structure of the dataset to understand Starbucks' global reach.
* **Top 3 Countries with Highest Store Density:**
  1. US (United States)
  2. CN (China)
  3. CA (Canada)
* **Primary Ownership Models:** `Company Owned`, `Licensed`, `Joint Venture`, and `Franchise`.

---

## 📈 2. Global Distribution of Ownership Types
To understand Starbucks' business model, I plotted the distribution of store ownerships globally.

*(Drop your Cell 3 Histogram Screenshot Here)*
![Distribution Graph]()

**📝 Key Insights:**
* **Dark Bars:** Represent the highest store counts, clearly showing that **Company Owned** and **Licensed** stores are the backbone of Starbucks' global operations.
* **Light Bars:** Indicate lower frequencies for Joint Ventures and Franchises.

---

## 🌍 3. Geographical Spread & Outlier Detection
Using Boxplots, I analyzed the `Longitude` data to find spatial anomalies and see how different ownership types spread across the globe.

*(Drop your Cell 4 Boxplot Screenshot Here)*
![Boxplot Graph]()

**📝 Key Insights:**
* **The Box (Middle 50%):** Shows the primary geographical clustering of stores.
* **The Black Dots (Outliers):** These represent stores located in extreme or isolated geographic coordinates, indicating strategic outposts far from standard clusters.

---

## 🗺️ 4. Coordinate Dependency Matrix
To see if there's any mathematical correlation between North/South (`Latitude`) and East/West (`Longitude`) expansion, I plotted a correlation heatmap.

*(Drop your Cell 5 Heatmap Screenshot Here)*
![Correlation Heatmap]()

**📝 Key Insights:**
* **Red/Warm Tones:** Indicate positive correlation.
* **Blue/Cool Tones:** Indicate negative or weak correlation.
* The exact numerical values inside the matrix reveal how Starbucks navigates geographical boundaries for its new store openings.

---

## 🔍 5. Global Expansion Patterns (Pairplot Analysis)
Finally, I created a complex pairplot grid to visually recognize overlapping market expansion patterns based on ownership types.

*(Drop your Cell 6 Pairplot Screenshot Here)*
![Pairplot Grid]()

**📝 Key Insights:**
* **Diagonal Curves (Density):** Show exactly where the concentration of stores peaks for each ownership type.
* **Scatter Dots (Grid):** Demonstrate the geographic overlapping of different store types, proving whether Company Owned and Licensed stores compete in the same regions or operate in distinct zones.

---

## 🛠️ Tools & Technologies Used
* **Python** (Pandas, Numpy)
* **Data Visualization** (Matplotlib, Seaborn)
* **Environment** (Jupyter Notebook / VS Code)

> *This project was completed as part of the AI & ML Internship.*
