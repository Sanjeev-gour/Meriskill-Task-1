
import pandas as pd
import seaborn as sns

from matplotlib import pyplot as plt

df = pd.read_csv("ObesityDataSet.csv")

print(df.head(5))

plt.figure(figsize=(12,6))
sns.histplot(df.NObeyesdad,kde=True)

plt.xticks(rotation=20)

plt.xlabel('Age')
plt.ylabel('Height')


plt.show()








