import pandas as pd
import scipy.stats as stats

df = pd.read_csv('data/house_pricing.csv')

def t_test(df=df):
    t_statistic, p_value = stats.ttest_1samp(a= df[df['Neighborhood'] == 'OldTown']['GrLivArea'],               # Sample data
                     popmean= df['GrLivArea'].mean())  # Pop mean
    return p_value, p_value < 0.05