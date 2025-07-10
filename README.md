# 🌾 DS_AgriData Explorer

**Domain**: Agriculture | **Tool Stack**: Python, Power BI, PostgreSQL

## 📌 Overview

This project presents an **Exploratory Data Analysis (EDA)** and interactive **Power BI Dashboard** based on district-level agricultural production data from India (ICRISAT). The goal is to identify patterns, regional variations, crop trends, and the relationship between area and yield for various crops such as rice, wheat, oilseeds, and more.

---

## 📁 Files Included

- `agri_data_clean_and_upload..py` – Python script for data cleaning and loading into PostgreSQL.
- `agri_eda_visuals.ipynb` – Jupyter Notebook containing detailed EDA visualizations using Matplotlib and Seaborn.
- `agridata.pbix` – Power BI dashboard with SQL-based visuals and analytical insights.
- `cleaned_agri_data.xlsx` – Output of the cleaned dataset ready for visualization and analysis.

---

## 🔍 Exploratory Data Analysis (EDA) Highlights

### 📊 Bar / Line / Pie Visualizations

- Top 7 **Rice Producing States** – Bar Plot  
- Top 5 **Wheat Producing States** – Bar + Pie Chart (with %)
- Top 5 **Oilseed Producing States** – Bar Plot
- Top 7 **Sunflower Producing States**
- India's **Sugarcane Production** – Last 50 Years (Line Plot)
- **Rice vs Wheat Production** – Last 50 Years (Line Plot)
- **Rice Production by West Bengal Districts** – Regional Bar Chart
- **Top 10 Wheat Production Years** from Uttar Pradesh
- **Millet Production Trends** – Last 50 Years
- **Sorghum Production** (Kharif & Rabi) – By Region
- Top 7 States – **Groundnut Production**
- **Soybean Production & Yield Efficiency** – Top 5 States
- Oilseed Production by State
- **Impact of Cultivated Area** on Production (Rice, Wheat, Maize)
- **Rice vs Wheat Yield** – Statewise Comparison

---

## 📈 Power BI Dashboard Insights

### 🔎 Questions Answered:

1. **Year-wise Trend** of Rice Production (Top 3 States)
2. **Top 5 Districts** by Wheat Yield Growth (Last 5 Years)
3. **States with Highest Growth** in Oilseed Production (5-Year Rate)
4. **District-wise Correlation**: Area vs. Production (Rice, Wheat, Maize)
5. **Annual Cotton Production Trends** – Top 5 States
6. **Top Groundnut Producing Districts** (2020)
7. **Average Maize Yield per Year** across all States
8. **Total Area Cultivated for Oilseeds** – Statewise
9. **Top Rice Yielding Districts**
10. **Wheat vs. Rice Production** – Top 5 States Over 10 Years

---

## 🧹 Data Preparation

- Source: ICRISAT - District Level Agricultural Data
- Cleaned via: `pandas` (Python)
  - Null handling, column renaming, type conversion
- Stored in: PostgreSQL for scalable querying via Power BI

---

## 🚀 How to Run

1. **Clean Data Locally**:
   - Run `agri_data_clean_and_upload..py` to clean and upload data to PostgreSQL.
2. **Perform EDA**:
   - Open `agri_eda_visuals.ipynb` in Jupyter Notebook and run cells.
3. **Power BI Dashboard**:
   - Open `agridata.pbix` with Power BI Desktop to explore visual insights.

---

## 🛠 Tools & Technologies

- **Python** – Data Cleaning, EDA
- **Pandas**, **Seaborn**, **Matplotlib**
- **Power BI** – Interactive Dashboard
- **PostgreSQL** – Data Storage
- **SQL** – Queries for calculated insights

---

## 🙌 Acknowledgements

- Data Source: [ICRISAT](https://www.icrisat.org/)
- Dashboard Tools: Microsoft Power BI
- Backend DB: PostgreSQL

---



