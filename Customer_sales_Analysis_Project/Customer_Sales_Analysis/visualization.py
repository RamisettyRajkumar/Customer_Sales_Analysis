import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('../data/cleaned_data.csv')

sns.barplot(x='Zone', y='Cancer_Cases', data=df)
plt.title("Cancer Cases per Zone")
plt.show()