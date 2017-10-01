from unittest import TestCase
from q04_chi2_test.build import chi2_test

class TestChi2_test(TestCase):
    def test_chi2_test(self):
        pval, result = chi2_test()
        self.assertAlmostEqual(pval, 0.36760293775391745)
        self.assertFalse(result)
