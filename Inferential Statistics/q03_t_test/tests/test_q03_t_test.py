from unittest import TestCase
from q03_t_test.build import t_test

class TestT_test(TestCase):
    def test_t_test(self):
        pval, result = t_test()
        self.assertAlmostEqual(pval, 0.51158698884870502)
        self.assertFalse(result)