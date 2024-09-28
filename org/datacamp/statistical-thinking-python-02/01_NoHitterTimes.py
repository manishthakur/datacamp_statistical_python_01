import matplotlib.pyplot as plt
import numpy as np

nohitter_times = [843, 1613, 1101, 215, 684, 814, 278, 324, 161, 219, 545, 715, 966, 624]

# Seed random number generator
print(nohitter_times)
np.random.seed(42)

# Compute mean no-hitter time: tau
tau = np.mean(nohitter_times)
print('nohitter_times mean ', tau)

# Draw out of an exponential distribution with parameter tau: inter_nohitter_time
inter_nohitter_time = np.random.exponential(tau, 100000)
print('inter_nohitter_time mean ', np.mean(inter_nohitter_time))
# print(inter_nohitter_time)

# Plot the PDF and label axes
_ = plt.hist(inter_nohitter_time, bins=50, normed=True, histtype='step')
_ = plt.xlabel('Games between no-hitters')
_ = plt.ylabel('PDF')

# Show the plot
plt.show()
