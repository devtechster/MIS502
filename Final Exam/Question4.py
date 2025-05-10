import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

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

# Slice X
X = df.loc[:, ['SSSNo', 'PatientType', 'SchedulePriority', 'PatientAge',
               'ScheduledCaseDuration', 'TotalSurgeryMin', 'PatientInRoomMin', 'SetUpMin']]

# Slice y
y = df.loc[:, ['SchCreateDays']]

# Split X and y into training and test data subsets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Fit a linear regression model on the training data
reg = LinearRegression().fit(X_train, y_train)

# Predict y values for test data
y_pred = reg.predict(X_test)

# Calculate the R2 score, MAE, MSE, and RMSE
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = mean_squared_error(y_test, y_pred, squared=False)

print("R2 Score:", r2)
print("Mean Absolute Error (MAE):", mae)
print("Mean Squared Error (MSE):", mse)
print("Root Mean Squared Error (RMSE):", rmse)

# Scatterplot of X variables and y
for col in X.columns:
    fig, ax = plt.subplots()
    ax.scatter(X_test[col], y_test)
    ax.set_xlabel(col)
    ax.set_ylabel('SchCreateDays')
    plt.show()