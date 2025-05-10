# Python Data Visualization Using Pandas, Matplotlib, and Seaborn Package Libraries --------------------------- #
# Data Visualization Using Pandas ----------------------------------------------------------------------------- #
import pandas as pd                                     # import Pandas dataframes/series
import matplotlib.pyplot as plt                         # import plotting libraries
desired_width = 400                                     # creates value and assigns 400 spaces
pd.set_option('display.width', desired_width)           # sets run window width
df = pd.read_csv(r'single_family_home_values.csv')      # reads Zillow file
df2 = df.sort_values(['estimated_value','yearBuilt','rooms','bedrooms'], ascending=(0,0,0,0)) # sorts df on listed cols
# plt.show spins a deprecation warning to ignore -------# Pandas built-in charts using .plot()
df2.plot.scatter(x='squareFootage', y='estimated_value', s=50)   # scatter to detect independence/correlation
plt.show()
df2.boxplot('estimated_value')                                   # use bloxplot to detect outliers
plt.show()
df2.plot(x='rooms', y='estimated_value')                         # plot X vs Y line chart for relationships
plt.show()
df2.plot(x='rooms', y='bedrooms')                                # as rooms increase, # bedrooms increase
plt.show()
df2.plot(x='yearBuilt', y='bedrooms')                            # bedrooms have decreased over time
plt.show()
# use .plot(kind="?") for following charts ------------------------------- #
df2.bedrooms.plot(kind='bar')                                    # vertical bar chart ~ number of bedrooms
plt.show()
df2.rooms.plot(kind='barh')                                      # horizontal bar chart ~ number of rooms
plt.show()
df2.yearBuilt.plot(kind='hist')                                  # frequency histogram of yearBuilt
plt.show()
df3 = df.groupby('zipcode').estimated_value.median().reset_index()         # .rest_index shifts pd series to df
df3.columns = ('zipcode','zipcode_median_value')                           # names columns in df3
df3.zipcode_median_value.plot(kind='pie',table=True)             # pie chart ~ zipcode median value
plt.show()
df2.rooms.plot(kind='kde')
plt.show()
# density chart of rooms
df4 = pd.merge(df, df3, on='zipcode', how='left')                          # merge df and df3 to have zipcode_median_val
df5 = df4[['zipcode','estimated_value','zipcode_median_value']]            # df slice
df6 = df5.sort_values(['zipcode','estimated_value'], ascending=(0,0))      # df6 is sorted by zipcode by estimated_value
df6.plot(kind='area', x='zipcode', y='estimated_value')
plt.show()
df2.plot.hexbin(x='rooms', y='estimated_value', gridsize=25)
plt.show()
# ----------------------------------------------------------- # End of file for Pandas Visualization

