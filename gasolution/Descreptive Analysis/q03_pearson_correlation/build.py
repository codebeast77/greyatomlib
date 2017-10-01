# Default Imports
from gasolution import pandas as pd

dataframe_1 = pd.read_csv('data/house_prices_multivariate.csv')
house_price = dataframe_1.loc[:, 'SalePrice']

dataframe_2 = pd.read_csv('data/house_prices_copy.csv').loc[:, 'SalePrice']
weight_of_nasa_space_shuttle = dataframe_2.loc[:, 'SalePrice']

# Return the correlation value between the SalePrice column for the two loaded datasets
def correlation():
    '''Enter code here'''

    return dataframe_1.SalePrice.corr(dataframe_2.SalePrice, method='pearson')
print(correlation())
