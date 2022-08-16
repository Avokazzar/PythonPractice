import pandas
import seaborn
import matplotlib.pyplot as plt

data = pandas.read_csv('app_stats.csv')
print(data)
seaborn.barplot(x='week_number', y='installs', data=data)
plt.show()
