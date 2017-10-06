# Default Imports
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from greyatomlib.logistic_regression_project.q01_oulier_removal.build import outlier_removal


## Write your solution Here
def data_cleaning(data):
    loan_data = pd.read_csv('data/loan_prediction_uncleaned.csv')
    loan_data = loan_data.drop('Loan_ID', 1)
    loan_data = outlier_removal(loan_data)
    X = loan_data.iloc[:, :-1]
    y = loan_data.iloc[:, 11]
    # Splitting the dataset into the Training set and Test set
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.25, random_state = 0)
    # Imputing Missing Value in Numerical variable
    X_train[['LoanAmount']] = X_train[['LoanAmount']].fillna(X_train.mean(), inplace=True)
    X_test[['LoanAmount']] = X_test[['LoanAmount']].fillna(X_train.mean(), inplace=True)
    # Imputing Missing Value in Categorical variable
    X_train[['Gender', 'Married', 'Dependents', 'Self_Employed','Loan_Amount_Term','Credit_History']] = X_train[['Gender', 'Married', 'Dependents', 'Self_Employed','Loan_Amount_Term','Credit_History']] .apply(lambda x:x.fillna(x.value_counts().index[0]))
    X_test[['Gender', 'Married', 'Dependents', 'Self_Employed','Loan_Amount_Term','Credit_History']] = X_test[['Gender', 'Married', 'Dependents', 'Self_Employed','Loan_Amount_Term','Credit_History']] .apply(lambda x:x.fillna(x.value_counts().index[0]))
    # sqrt Transformation of data
    X_train[['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount']] = np.sqrt(X_train[['ApplicantIncome','CoapplicantIncome','LoanAmount']])
    X_test[['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount']] = np.sqrt(X_test[['ApplicantIncome','CoapplicantIncome','LoanAmount']])
    # Categorical Variable encoding
    cat_cols = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed', 'Property_Area']
    X_train = pd.get_dummies(X_train, columns = cat_cols, drop_first=True)
    X_test = pd.get_dummies(X_test, columns = cat_cols, drop_first=True)
    y_train = pd.Series(map(lambda x: dict(Y=1, N=0)[x], y_train.values.tolist()), y_train.index)
    y_test = pd.Series(map(lambda x: dict(Y=1, N=0)[x], y_test.values.tolist()), y_test.index)
    return X,y, X_train, X_test, y_train, y_test






