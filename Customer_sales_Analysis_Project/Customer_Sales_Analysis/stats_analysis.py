import pandas as pd
import numpy as np
from scipy.stats import ttest_ind

df = pd.read_csv('../data/cleaned_data.csv')

mean = df['Cancer_Cases'].mean()
median = df['Cancer_Cases'].median()
mode = df['Cancer_Cases'].mode()[0]
std = df['Cancer_Cases'].std()

# T-test: Zone A vs Others
zone_a = df[df['Zone'] == 'A']['Cancer_Cases']
others = df[df['Zone'] != 'A']['Cancer_Cases']
_, p_value = ttest_ind(zone_a, others)

print(f"📊 Mean: {mean}")
print(f"📊 Median: {median}")
print(f"📊 Mode: {mode}")
print(f"📊 Standard Deviation: {std}")
print(f"📊 P-Value (Zone A vs Others): {p_value}")