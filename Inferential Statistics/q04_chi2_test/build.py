import pandas as pd
import scipy.stats as stats

df = pd.read_csv('data/house_pricing.csv')

def chi2_test(df=df):
    price = pd.qcut(df['SalePrice'], 3, labels = ['High', 'Medium', 'Low'])
    freqtab = pd.crosstab(df['LandSlope'], price)
    chi2,pval,dof,expected = stats.chi2_contingency(freqtab)
    return pval, pval < 0.05