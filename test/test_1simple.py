import unittest
from strategies.complete_search import CompleteStrategy
from strategies.dp import DP

complete_search_strategy = CompleteStrategy(
    "Complete Search Strategy", [3, 2], [1, 3], 2)
dp_strategy = DP("DP Strategy", [3, 2], [1, 3], 2)

complete_search_strategy.solve()
dp_strategy.solve()


class TestCompleteStrategy(unittest.TestCase):
    def test_cmax(self):
        self.assertEqual(complete_search_strategy.cmax, 7, "Should be 7")

    def test_correct_order(self):
        self.assertEqual(
            complete_search_strategy.correct_order, [(2, 3), (3, 1)])


class TestDP(unittest.TestCase):
    def test_cmax(self):
        self.assertEqual(dp_strategy.cmax, 7, "Should be 7")

    def test_correct_order(self):
        self.assertEqual(dp_strategy.correct_order, [(2, 3), (3, 1)])


if __name__ == '__main__':
    unittest.main()
