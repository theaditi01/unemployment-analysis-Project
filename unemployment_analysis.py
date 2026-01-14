import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 
# DATASET 1: Unemployment in India
# 
df_india = pd.read_csv("Unemployment in India.csv")  
df_india.columns = df_india.columns.str.strip()  

print("First dataset columns:")
print(df_india.columns)

# Convert Date column to datetime
df_india['Date'] = pd.to_datetime(df_india['Date'])

# Region-wise average unemployment rate
region_avg = df_india.groupby('Region')['Estimated Unemployment Rate (%)'].mean()

# Bar chart
plt.figure(figsize=(12,6))
region_avg.sort_values().plot(kind='bar')
plt.title("Average Unemployment Rate by Region (India)")
plt.xlabel("Region")
plt.ylabel("Unemployment Rate (%)")
plt.tight_layout()
plt.show()


# 
# DATASET 2: Unemployment Rate upto Nov 2020
# 
df_2020 = pd.read_csv("Unemployment_Rate_upto_11_2020.csv")  
df_2020.columns = df_2020.columns.str.strip()

print("\nSecond dataset columns:")
print(df_2020.columns)

# Convert Date column to datetime
df_2020['Date'] = pd.to_datetime(df_2020['Date'])

# Line plot
plt.figure(figsize=(12,6))
sns.lineplot(data=df_2020, x='Date', y='Estimated Unemployment Rate (%)')
plt.title("Unemployment Rate Trend (Upto Nov 2020)")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate (%)")
plt.tight_layout()
plt.show()

print("\nBoth datasets analysed successfully!")