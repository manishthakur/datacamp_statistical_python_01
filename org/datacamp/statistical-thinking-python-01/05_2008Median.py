import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df_swing = pd.read_csv('../data/2008_swing_states.csv')

x = np.sort(df_swing['dem_share'])
y = np.arange(1, len(x) + 1) / len(x)

plt.plot(x, y, marker='.', linestyle='none')
# Label the axes
plt.xlabel('percent of vote for Obama')
plt.ylabel('ECDF')

plt.margins(0.02)
plt.show()

