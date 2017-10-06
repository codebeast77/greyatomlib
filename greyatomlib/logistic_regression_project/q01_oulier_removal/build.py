# Outlier removal
import pandas as pd
loan_data = pd.read_csv('data/loan_prediction_uncleaned.csv')
loan_data = loan_data.drop('Loan_ID', 1)

#Write your Solution here
# Outlier Removal
def outlier_removal(loan_data):
    loan_data = loan_data.drop(loan_data[(loan_data['ApplicantIncome']> 15000)].index)
    loan_data = loan_data.drop(loan_data[(loan_data['CoapplicantIncome']> 5000)].index)
    loan_data = loan_data.drop(loan_data[(loan_data['LoanAmount']> 300)].index)
    return loan_data
