import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


df_swing = pd.read_csv('../data/2008_swing_states.csv')

# Compute number of data points: n_data
n_data = len(df_swing)
# Number of bins is the square root of number of data points: n_bins
n_bins = np.sqrt(n_data)
# Convert number of bins to integer: n_bins
n_bins = int(n_bins)

# setting bin size
bin_edges = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Set default Seaborn style
sns.set()

# Plot the histogram
_ = plt.hist(df_swing['dem_share'], bins=n_bins)

# set label
_ = plt.xlabel('percent of vote for Obama')
_ = plt.ylabel('number of countries')

plt.show()
