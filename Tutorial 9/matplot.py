# Data Visualization Using Matplotlib ---------------------------------------------------------------------------#
# ----------------------------------------------------------- # Scatter plot using a data frame data
import pandas as pd                                           # import Pandas dataframes/series
import matplotlib.pyplot as plt                               # import plotting libraries
import matplotlib                                             # import matplotlib charts
desired_width = 400                                           # creates value and assigns 400 spaces
pd.set_option('display.width', desired_width)                 # sets run window width
data = pd.read_csv('iris.csv')                                # reads iris data file
X = data['swid']                                              # assigns swid column to X
Y = data['slen']                                              # assigns slen column to Y
print(type(data), type(X), type(Y))                           # displays data frame type, X type, and  Y type
print(data.head(5))                                           # displays top 5 rows of data
plt.scatter(X, Y)                                             # plots a scatter diagram using X and Y
plt.title('Scatterplot:  Iris data septal width vs length')   # assigning plt.title variable
plt.xlabel('septal width (cm)')                               # assigning plt.xlabel variable
plt.ylabel('septal length (cm)')                              # assigning plt.ylabel variable
plt.savefig('scatter.png')                                    # saves graphic as a PNG file name scatter.png
plt.show()                                                    # displays scatter plot
# ----------------------------------------------------------- # End of Matplotlib scatter plot example
