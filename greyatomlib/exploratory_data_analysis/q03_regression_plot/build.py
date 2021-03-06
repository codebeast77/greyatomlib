import matplotlib.pyplot as plt
import seaborn as sns

from greyatomlib import pandas_project as pd

data = pd.read_csv('data/house_prices_multivariate.csv')

def regression_plot(variable1, variable2):
    return sns.jointplot(variable1, variable2, data=data, kind='reg')
