import pandas
import seaborn
import matplotlib.pyplot as plt

data = pandas.read_csv('app_stats.csv')
payments = list(data['payments'])
installs = list(data['installs'])
conversions = []
for index in range(len(payments)):
    conversions.append(payments[index] / installs[index])
print(data)
seaborn.barplot(x='week_number', y=conversions, data=data)
plt.show()
