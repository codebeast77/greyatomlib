# Default imports
import pandas as pd
from sklearn.model_selection import train_test_split

def load_data(path, test_size=0.33):
        df = pd.read_csv(path)
        X = df.iloc[:, :-1]
        y = df.iloc[:, -1]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size)
        return df, X_train, X_test, y_train, y_test
