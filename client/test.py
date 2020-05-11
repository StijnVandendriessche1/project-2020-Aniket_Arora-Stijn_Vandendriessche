import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


data = pd.read_csv("../data/fake.csv")
print(data.columns)

fig = plt.figure()
sns.countplot(x='country', data=data)
fig.show()

fig = plt.figure()
sns.countplot(x='author', data=data, order=data.author.value_counts().iloc[:5].index)
fig.show()
