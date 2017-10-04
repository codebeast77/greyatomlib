from sklearn.model_selection import cross_val_score
import numpy as np
np.random.seed(9)

def cross_validation(model,X,y):
    scores = cross_val_score(model, X, y, scoring="neg_mean_squared_error", cv=5)
    return scores.mean()