
# Data Visualization Using Seaborn -------------------------- # ---------------------------------------------- #
# ----------------------------------------------------------- # Using Panda Data Frames with Seaborn
import pandas as pd
import seaborn as sn
import matplotlib.pyplot as plt
df = pd.read_csv(r'single_family_home_values.csv')                                         # zillow file
df2 = df[(df.estimated_value <= 1000000) & (df.lastSaleAmount <= 1000000)]                 # slice df to remove outliers
# ---------------------------------------------------------------------------------------- # display box chart
# plt.show returns a matplotlib deprecation warning you may ignore # --------------------- #
sn.boxplot(df2.estimated_value).set_title('Box Plot ~ Estimated Home Value w/o outliers')
plt.show()
# ---------------------------------------------------------------------------------------- # display pair chart
c_title = 'Pair Plot ~ Estimated Value vs. Last Sale by Zip'
 # no room on chart
sn.pairplot(df2[['lastSaleAmount', 'estimated_value', 'zipcode']], hue='zipcode')
plt.show()
# ---------------------------------------------------------------------------------------- # display strip chart
sn.stripplot(x=df2.zipcode, y=df.estimated_value).set_title("Strip Plot ~ Estimated Home Value by Zip")
plt.show()
# ---------------------------------------------------------------------------------------- # display violin chart
sn.violinplot(x=df2.zipcode, y=df2.estimated_value).set_title("Violin Plot ~ Estimated Home Value by Zip")
plt.show()
# ---------------------------------------------------------------------------------------- # End of Seaborn examples