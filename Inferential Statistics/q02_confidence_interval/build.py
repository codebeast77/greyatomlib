import numpy as np
import pandas as pd
import math
import scipy.stats as stats

df = pd.read_csv('data/house_pricing.csv')

np.random.seed(10)
sample = np.random.choice(a= df['GrLivArea'], size = 500)

def confidence_interval(sample=sample):
    sample_mean = sample.mean()
    z_critical = stats.norm.ppf(q = 0.95)  # Get the z-critical value*
    stdev = sample.std()  # Get the population standard deviation

    standard_error = z_critical * (stdev/math.sqrt(sample.shape[0]))

    confidence_interval = (sample_mean - standard_error,
                       sample_mean + standard_error)
    return confidence_interval