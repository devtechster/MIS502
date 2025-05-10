import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
desired_width = 320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 18)
df = pd.read_csv('SchData2013.csv', low_memory=False)
print(df.info())

# Identify int64 and float64 variables
int_vars = df.select_dtypes(include=['int64']).columns
float_vars = df.select_dtypes(include=['float64']).columns
print('Int Variables:', int_vars)
print('Float Variables:', float_vars)
df = df.drop('CaseMonth', axis=1)
df = df.dropna()
# Identify all numeric columns
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
#AND
# Replace missing values with column mean
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
#verifying if there is no null values in any columns
print(df.isnull().sum())


df2 = df[numeric_cols]
print(df2.info())

corr_matrix = df2.corr()
print(corr_matrix)

# Create a heatmap using Seaborn
sns.set(font_scale=0.8)
sns.heatmap(corr_matrix, cmap="coolwarm", annot=True, annot_kws={"size": 5})
plt.title("Correlation Matrix Heatmap")
plt.xticks(rotation=45)
plt.yticks(rotation=0)
plt.tight_layout()

# Save the plot to disk
plt.savefig("correlation_heatmap.png")