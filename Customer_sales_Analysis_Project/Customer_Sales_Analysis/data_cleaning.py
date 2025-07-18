import pandas as pd

# Load Excel data
df = pd.read_excel('../data/raw_data.xlsx')

# Drop duplicates, fill missing values if any
df = df.drop_duplicates()
df.fillna(0, inplace=True)

# Save cleaned data
df.to_csv('../data/cleaned_data.csv', index=False)
print("✅ Data cleaned and saved.")