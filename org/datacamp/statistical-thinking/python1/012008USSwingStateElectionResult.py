import matplotlib.pyplot as plt
import pandas as pd

df_swing = pd.read_csv('2008_swing_states.csv')
print(df_swing)
_ = plt.hist(df_swing['dem_share'])

plt.show()
