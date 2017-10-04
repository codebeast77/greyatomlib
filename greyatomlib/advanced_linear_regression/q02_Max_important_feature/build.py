# Default imports
from greyatomlib.advanced_linear_regression.q01_load_data.build import load_data


def Max_important_feature(data_set, target_varilable="SalePrice", n=4):
    data_set, X_train, X_test, y_train, y_test = load_data('data/house_prices_multivariate.csv')
    cor = data_set.corr()[target_varilable]
    return cor.sort_values(ascending = False)[1:n+1].index.values
