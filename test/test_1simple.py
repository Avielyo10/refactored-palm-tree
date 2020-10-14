import unittest
from strategies.complete_search import CompleteStrategy
from strategies.greedy import Greedy

complete_search_strategy = CompleteStrategy(
    "Complete Search Strategy", [3, 2], [1, 3], 2)
greedy_strategy = Greedy("Greedy Strategy", [3, 2], [1, 3], 2)

complete_search_strategy.solve()
greedy_strategy.solve()


class TestCompleteStrategy(unittest.TestCase):
    def test_cmax(self):
        self.assertEqual(complete_search_strategy.cmax, 7, "Should be 7")

    def test_correct_order(self):
        self.assertEqual(
            complete_search_strategy.correct_order, [(2, 3), (3, 1)])


class Testgreedy(unittest.TestCase):
    def test_cmax(self):
        self.assertEqual(greedy_strategy.cmax, 7, "Should be 7")

    def test_correct_order(self):
        self.assertEqual(greedy_strategy.correct_order, [(2, 3), (3, 1)])


if __name__ == '__main__':
    unittest.main()
