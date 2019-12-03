

# Some imports to explore the datasets
import pandas as pd
import scipy as sc
import matplotlib.pylab as pl
import seaborn as sns # You might need to install this (e.g., sudo pip install seaborn)

data = pd.read_csv("../Data/ThermRespData.csv")
print("Loaded {} columns.".format(len(data.columns.values)))

