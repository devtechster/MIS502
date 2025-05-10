
import pandas as pd
import numpy as np
import seaborn as sn
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.model_selection import train_test_split

desired_width = 40
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 20)
dataframe = pd.read_csv(r'combinedData.csv', low_memory=False)
#---------------------------------
print(dataframe.head(2))
print(dataframe.tail(5))
print(dataframe.shape)
print(dataframe.info())
print(dataframe.describe())
sn.boxplot(dataframe.age)
plt.show()
sn.boxplot(dataframe.rating)
plt.show()
#---------------------------------
# groupByMovie = dataframe.groupby('movieId')
# groupsByTitle = dataframe.groupby('title')
# print(groupByMovie.head(1))
# print(groupsByTitle.head(1))
#---------------------------------

# moderateMoviesDF = dataframe[(dataframe.rating>1) & (dataframe.rating<5)]
# print('moderateMoviesDF',moderateMoviesDF['movieId'].nunique())
#
# flopMoviesDF = dataframe[(dataframe.rating==1)]
# print('flopMoviesDF',flopMoviesDF['movieId'].nunique())
#
# twoStareMoviesDF = dataframe[(dataframe.rating==2)]
# print('twoStareMoviesDF',twoStareMoviesDF['movieId'].nunique())
#
# threeStarMoviesDF = dataframe[(dataframe.rating==3)]
# print('threeStarMoviesDF',threeStarMoviesDF['movieId'].nunique())
#
# fourStarMoviesDF = dataframe[(dataframe.rating==4)]
# print('fourStarMoviesDF',fourStarMoviesDF['movieId'].nunique())
#
# superhitMoviesDF = dataframe[(dataframe.rating==5)]
# print('superhitMoviesDF',superhitMoviesDF['movieId'].nunique())


# # Data Mining - classification & regression - LinearRegression()----------------
# dataframe.fillna(0, inplace = True)
# X= dataframe[['movieId','userId','age']]
# y= dataframe.rating
# dataframe['rating_class'] = dataframe.rating.apply(lambda x: 'low' if x < 2 else 'high')
# print(dataframe.rating_class.value_counts())
# y2=dataframe.rating_class
#
# log = LogisticRegression()
# print(log.fit(X,y2))
# print(log.score(X,y2))
# X_train, X_test, y2_train, y2_test = train_test_split(X,y2)
# print(X_train.shape, y2_train.shape, X_test.shape, y2_test.shape)
# print(log.fit(X_train, y2_train))
# print(log.score(X_test, y2_test))
# # Data Mining - classification & regression - LinearRegression() ends----------------------
#


import pandas as pd
import numpy as np
import seaborn as sn
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.model_selection import train_test_split

desired_width = 40
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns', 20)
df = pd.read_csv(r'combinedData.csv', low_memory=False)

sn.pairplot(data=df, hue='age')
plt.show()
