

import pandas as pd
from sqlalchemy import create_engine

# Load the Excel file

df = pd.read_excel(r'E:\AgriEDA\ICRISAT-District Level Data.xlsx', sheet_name='ICRISAT-District Level Data')

# Show first 5 rows of the data
print("🔹 First 5 rows of data:")
print(df.head())

# Show original column names
print("\n🔹 Original Column Names:")
print(df.columns.tolist())

# Clean column names (make all lowercase, remove spaces and brackets)
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(' ', '_')
    .str.replace('(', '', regex=False)
    .str.replace(')', '', regex=False)
)

# Show cleaned column names
print("\n🔹 Cleaned Column Names:")
print(df.columns.tolist())

# Show info like column types and missing values
print("\n🔹 Data Summary:")
print(df.info())

# Check how many missing values in each column
print("\n🔹 Missing Values (count):")
print(df.isnull().sum())

# Show % of missing data in each column
print("\n🔹 Missing Values (%):")
missing_percent = df.isnull().mean() * 100
print(missing_percent)

# List of columns that should be numbers
numeric_columns = [
    "rice_area_1000_ha", "rice_production_1000_tons", "rice_yield_kg_per_ha",
    "wheat_area_1000_ha", "wheat_production_1000_tons", "wheat_yield_kg_per_ha",
    "oilseeds_area_1000_ha", "oilseeds_production_1000_tons", "oilseeds_yield_kg_per_ha",
    "sugarcane_production_1000_tons", "cotton_yield_kg_per_ha"
]

# Convert these columns to numbers (handle errors safely)
for col in numeric_columns:
    if col in df.columns:
        df[col] = pd.to_numeric(df[col], errors="coerce")

# Drop rows where Year or District Name is missing
df = df.dropna(subset=["year", "dist_name"])

# Save the cleaned data to a new Excel file
df.to_excel("cleaned_agri_data.xlsx", index=False)
print("\n✅ Cleaned data saved as 'cleaned_agri_data.xlsx'")

# Show the number of rows and columns after cleaning
print("\n🔹 Cleaned Data Shape:", df.shape)

# Show cleaned column names again
print("🔹 Final Columns:", df.columns.tolist())

user = 'postgres'
password ='admin123'
host = 'localhost'            # or use IP/domain
port = '5432'
database = 'test'
table_name = "agri_data_cleaned"      # name of the table to be created/replaced

# Create the connection string and engine
engine = create_engine(f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}")

# Push to PostgreSQL
df.to_sql(name=table_name, con=engine, if_exists='replace', index=False)
print(f"\n✅ Table '{table_name}' uploaded to database '{database}'")
