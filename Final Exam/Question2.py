import pandas as pd
import matplotlib.pyplot as plt

desired_width = 320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 10)
df = pd.read_csv('SchData2013.csv', low_memory=False)
#---------------------

print(df.shape)
print(df.info())
print(df.describe())
#---------------------

#---------------------

# Fill missing values in int64 columns with the mean value for that column
int64_columns = df.select_dtypes(include=['int64']).columns
df[int64_columns] = df[int64_columns].fillna(df.mean())

# Fill missing values in float64 columns with the mean value for that column
float64_columns = df.select_dtypes(include=['float64']).columns
df[float64_columns] = df[float64_columns].fillna(df.mean())

print(df['PatientInRoomMin'].isnull().sum())
print(df['SchCreateDays'].isnull().sum())
#---------------------


# #---------------------
df = df.drop('CaseMonth', axis=1)
df = df.dropna()
cat_cols = [col for col in df.columns if df[col].dtype == 'object']
df = df.drop(cat_cols, axis=1)
df = df.reset_index(drop=True)
print(df.info())
# #---------------------
diced_df = df[(df["SurgicalArea"] == "HHOR") & (df["SSSNo"] == 9) & (df["PatientType"] == 2)]

# calculate the mean and median of PatientInRoomMin for the diced dataframe
mean = diced_df["PatientInRoomMin"].mean()
median = diced_df["PatientInRoomMin"].median()

print(diced_df.head(10))
print("Mean of PatientInRoomMin: {:.2f}".format(mean))
print("Median of PatientInRoomMin: {:.2f}".format(median))

# create a boxplot for PatientInRoomMin
diced_df.boxplot(column=["PatientInRoomMin"])
plt.show()

# calculate the IQR and remove outliers
Q1 = diced_df["PatientInRoomMin"].quantile(0.25)
Q3 = diced_df["PatientInRoomMin"].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5*IQR
upper_bound = Q3 + 1.5*IQR
diced_df = diced_df[(diced_df["PatientInRoomMin"] >= lower_bound) & (diced_df["PatientInRoomMin"] <= upper_bound)]

# create a boxplot for PatientInRoomMin after removing outliers
diced_df.boxplot(column=["PatientInRoomMin"])
plt.show()
