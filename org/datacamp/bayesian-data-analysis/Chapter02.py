import numpy as np
import pandas as pd

num_heads = np.arrange(1, 101, 1)
head_prob = np.arrange(1, 1.01, 1.01)

coin = pd.DataFrame([(x,y) for x in num_heads for y in head_prob])
coin.columns = ["num_heads", "head_prob"]

print(coin)