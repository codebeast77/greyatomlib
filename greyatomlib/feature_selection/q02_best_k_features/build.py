# Default imports

import pandas as pd

data = pd.read_csv('data/house_prices_multivariate.csv')


from sklearn.feature_selection import SelectPercentile
from sklearn.feature_selection import f_regression


def percentile_k_features(dataframe, predictors, target, k, model=None):

        if model is not None:
            pass
        else:
            model = f_regression

        dummy = dataframe.copy()

        X = dummy[predictors]
        y = dummy[target]

        skb = SelectPercentile(model, k)
        skb.fit_transform(X, y)
        scores = list(skb.scores_)

        top_k_index = sorted(range(len(scores)), key=lambda i: scores[i], reverse=True)[:k]
        top_k_predictors = [predictors[i] for i in top_k_index]

        return top_k_predictors
