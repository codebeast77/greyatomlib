import pandas as pd
import sys, os

sys.path.append(os.path.join(os.path.dirname(os.curdir)))

from unittest import TestCase

from greyatomlib.feature_selection.q01_plot_corr.build import plot_corr

data = pd.read_csv('data/house_prices_multivariate.csv')


class TestPlot_corr(TestCase):
    def test_plot_corr(self):
        plt = plot_corr(data)
        self.assertTrue(True)
