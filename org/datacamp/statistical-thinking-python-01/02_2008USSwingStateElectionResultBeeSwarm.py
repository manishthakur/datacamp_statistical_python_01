import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_csv('../data/iris.csv')
df.head()

# Create bee swarm plot with Seaborn's default settings
df.head()
sns.swarmplot(x='variety', y='petal.length', data=df)

# Label the axes
plt.xlabel('variety')
plt.ylabel('petal length')

# Show the plot
plt.show()
