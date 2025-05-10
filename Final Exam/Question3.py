import pandas as pd
import matplotlib.pyplot as plt

desired_width = 400
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 10)
df = pd.read_csv('SchData2013.csv', low_memory=False)
print(df.info())

df2 = df.groupby('SurgicalSpecialty')['ScheduledCaseDuration'].median().reset_index()
df2.columns = ['SurgicalSpecialty', 'ScheduledCaseDurationMedian']

merged_df = pd.merge(df, df2, on='SurgicalSpecialty')
filtered_df = merged_df[(merged_df['SurgicalSpecialty'] == 'URO') & (merged_df['TotalSurgeryMin'] <= 250)]

print("Mean of TotalSurgeryMin:", filtered_df['TotalSurgeryMin'].mean())
print("Median of TotalSurgeryMin:", filtered_df['TotalSurgeryMin'].median())

plt.boxplot(filtered_df['TotalSurgeryMin'])
plt.title("Boxplot of TotalSurgeryMin")
plt.show()