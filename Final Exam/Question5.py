import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score
from sklearn.neighbors import KNeighborsRegressor

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
# Identify all numeric columns
numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns
#AND
# Replace missing values with column mean
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].mean())
#verifying if there is no null values in any columns
print(df.isnull().sum())
df = df.drop('CaseMonth', axis=1)
df = df.dropna()

#----------Linear Regression-------
num_cols = ['SSSNo', 'PatientType', 'SchedulePriority', 'PatientAge', 'ScheduledCaseDuration',
            'TotalSurgeryMin', 'PatientInRoomMin', 'SetUpMin', 'SchCreateDays']
data = df[num_cols]
X_train, X_test, y_train, y_test = train_test_split(data.iloc[:, :-1], data.iloc[:, -1], test_size=0.2, random_state=42)
# Create a linear regression object
reg = LinearRegression()
# Fit the model using the training data
reg.fit(X_train, y_train)
# Make predictions on the test data
y_pred = reg.predict(X_test)
print("R-squared:", r2_score(y_test, y_pred))
print("Mean Absolute Error:", mean_absolute_error(y_test, y_pred))
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))

#-------------K means clustering analysis---------
# Split the dataset into training and testing sets
X = df[['SSSNo', 'PatientType', 'SchedulePriority', 'PatientAge', 'ScheduledCaseDuration', 'TotalSurgeryMin',
        'PatientInRoomMin', 'SetUpMin']]
y = df['SchCreateDays']
X_train2, X_test2, y_train2, y_test2 = train_test_split(X, y, test_size=0.2, random_state=0)
# Apply KMeans clustering to the data
kmeans = KMeans(n_clusters=3, random_state=0)
kmeans.fit(X_train2)
# Predict the clusters for the test data
y_pred = kmeans.predict(X_test2)
# Evaluate the clustering performance using adjusted rand score
print('Adjusted Rand Score:', adjusted_rand_score(y_test2, y_pred))
#----------------------------------------------


# Apply KNN Regression to the data -----------------
knn = KNeighborsRegressor(n_neighbors=5)
knn.fit(X_train, y_train)
# Predict the values for the test data
y_pred = knn.predict(X_test)
# Evaluate the model performance using R2 score, mean absolute error, and root mean squared error
print('R2 Score:', r2_score(y_test, y_pred))
print('Mean Absolute Error:', mean_absolute_error(y_test, y_pred))
print('Root Mean Squared Error:', mean_squared_error(y_test, y_pred, squared=False))
#----------------------------------------------

