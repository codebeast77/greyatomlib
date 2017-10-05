# Default imports
from sklearn.feature_selection import SelectFromModel
from sklearn.ensemble import RandomForestClassifier
import pandas as pd

data = pd.read_csv('data/house_prices_multivariate.csv')


# Your solution code here

def select_from_model(dataframe, predictors, target):
    dummy = dataframe.copy()
    model = RandomForestClassifier()

    sfm = SelectFromModel(model)
    sfm = sfm.fit(dummy[predictors], dummy[target])

    dataset_new = sfm.transform(dummy[predictors])
    feature_idx = sfm.get_support()
    feature_name = dataframe.columns[feature_idx]

    return list(feature_name)
