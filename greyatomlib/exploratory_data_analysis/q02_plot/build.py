import matplotlib.pyplot as plt
import seaborn as sns

from greyatomlib import pandas as pd

data = pd.read_csv('data/house_prices_multivariate.csv')

def plot(num_cols):
    facet = None
    for i in range(0,len(num_cols),2):
        if len(num_cols) > i+1:
            plt.figure(figsize=(10,4))
            plt.subplot(121)
            sns.boxplot(facet, num_cols[i],data = data)
            plt.subplot(122)
            sns.boxplot(facet, num_cols[i+1],data = data)
            plt.tight_layout()
            plt.show()

        else:
            sns.boxplot(facet, num_cols[i],data = train)