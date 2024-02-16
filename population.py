import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


df = pd.read_csv('input/ju22qv030000.csv', index_col="地域")

bulk_size = 6
groups = np.arange(len(df)) // bulk_size
plt.figure(figsize=(20, 5))
plt.rcParams['font.family'] = 'IPAexGothic'
for group, subdf in df.groupby(groups):
    subdf.T.plot()
    plt.tight_layout()
    plt.savefig(f"population_{group}.png")
