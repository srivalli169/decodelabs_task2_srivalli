import pandas as pd
import numpy as np

# Load Dataset
df = pd.read_excel(r"C:\week2Decode\week1\Cleaned_Dataset.xlsx")

# ===============================
# DATASET OVERVIEW
# ===============================
print("Dataset Shape:", df.shape)
print("\nColumns:")
print(df.columns)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:", df.duplicated().sum())

# ===============================
# BASIC STATISTICS
# ===============================
numeric_cols = ['Quantity', 'UnitPrice', 'ItemsInCart', 'TotalPrice']

print("\nDescriptive Statistics")
print(df[numeric_cols].describe())

print("\nMean")
print(df[numeric_cols].mean())

print("\nMedian")
print(df[numeric_cols].median())

# ===============================
# PRODUCT ANALYSIS
# ===============================
print("\nTop Products")
print(df['Product'].value_counts())

# ===============================
# PAYMENT METHOD ANALYSIS
# ===============================
print("\nPayment Method Distribution")
print(df['PaymentMethod'].value_counts())

# ===============================
# ORDER STATUS ANALYSIS
# ===============================
print("\nOrder Status Distribution")
print(df['OrderStatus'].value_counts())

# ===============================
# REFERRAL SOURCE ANALYSIS
# ===============================
print("\nReferral Source Distribution")
print(df['ReferralSource'].value_counts())

# ===============================
# SALES TREND BY YEAR
# ===============================
df['Date'] = pd.to_datetime(df['Date'])

sales_by_year = df.groupby(df['Date'].dt.year)['TotalPrice'].sum()

print("\nSales Trend By Year")
print(sales_by_year)

# ===============================
# OUTLIER DETECTION
# ===============================
print("\nOutlier Detection (IQR Method)")

for col in numeric_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)

    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    outliers = df[(df[col] < lower) | (df[col] > upper)]

    print(f"{col}: {len(outliers)} outliers")

# ===============================
# KEY INSIGHTS
# ===============================
print("\n========== KEY INSIGHTS ==========")

print("Average Quantity:",
      round(df['Quantity'].mean(), 2))

print("Average Order Value:",
      round(df['TotalPrice'].mean(), 2))

print("Most Ordered Product:",
      df['Product'].value_counts().idxmax())

print("Most Used Payment Method:",
      df['PaymentMethod'].value_counts().idxmax())

print("Top Referral Source:",
      df['ReferralSource'].value_counts().idxmax())

print("\nEDA Completed Successfully!")