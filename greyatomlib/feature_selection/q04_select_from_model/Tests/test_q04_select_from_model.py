import sys, os

sys.path.append(os.path.join(os.path.dirname(os.curdir)))

import pandas as pd

data = pd.read_csv('data/house_prices_multivariate.csv')

from unittest import TestCase
from q04_select_from_model.build import select_from_model


class TestSelect_from_model(TestCase):
    def test_select_from_model(self):
        predictors = list(data.columns.values)[:-1]
        target = 'SalePrice'
        expected = ['LotFrontage',
                    'LotArea',
                    'YearBuilt',
                    'YearRemodAdd',
                    'MasVnrArea',
                    'BsmtFinSF1',
                    'BsmtUnfSF',
                    'TotalBsmtSF',
                    '1stFlrSF',
                    '2ndFlrSF',
                    'GrLivArea',
                    'TotRmsAbvGrd',
                    'GarageYrBlt',
                    'GarageArea',
                    'WoodDeckSF',
                    'OpenPorchSF',
                    'YrSold']

        self.assertEqual(select_from_model(data, predictors, target), expected)
