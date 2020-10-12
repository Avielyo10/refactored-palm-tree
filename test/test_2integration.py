import unittest
import random
from strategies.complete_search import CompleteStrategy
from strategies.dp import DP

NUM_OF_JOBS = 8
NUM_OF_TESTS = 10000
arrays = []
for i in range(0, NUM_OF_TESTS):
    a_array = random.sample(range(1, 300), NUM_OF_JOBS)
    b_array = random.sample(range(1, 300), NUM_OF_JOBS)
    arrays.append((a_array, b_array))


class TestIntegration(unittest.TestCase):
    def test_dynamic(self):
        for a_array, b_array in arrays:
            complete_search_strategy_dynamic = CompleteStrategy(
                "Complete Search Strategy", a_array, b_array, NUM_OF_JOBS)
            dp_strategy_dynamic = DP(
                "DP Strategy", a_array, b_array, NUM_OF_JOBS)
            with self.subTest():
                complete_search_strategy_dynamic.solve()
                dp_strategy_dynamic.solve()
                
                self.assertEqual(
                    complete_search_strategy_dynamic.cmax, dp_strategy_dynamic.cmax)
                self.assertEqual(
                    complete_search_strategy_dynamic.correct_order, dp_strategy_dynamic.correct_order)


if __name__ == '__main__':
    unittest.main()
