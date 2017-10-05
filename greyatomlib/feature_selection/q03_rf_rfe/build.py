# Default imports
import pandas as pd

data = pd.read_csv('data/house_prices_multivariate.csv')

from sklearn.feature_selection import RFE
from sklearn.ensemble import RandomForestClassifier


# Your solution code here
def rf_rfe(dataframe, predictors, target):
    dummy = dataframe.copy()
    model = RandomForestClassifier()

    rfe = RFE(model, round(len(predictors) / 2, 0))
    rfe = rfe.fit(dummy[predictors], dummy[target])
    top_features = []

    for i in range(len(rfe.ranking_)):
        if rfe.ranking_[i] == 1:
            top_features.append(predictors[i])

    return top_features

