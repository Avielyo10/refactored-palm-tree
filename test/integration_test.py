import random
import time
from strategies.complete_search import CompleteStrategy
from strategies.dp import DP

NUM_OF_JOBS = 8
NUM_OF_TESTS = 10000
SUCCESS = 0
FAILURES = 0

for test_number in range(1, NUM_OF_TESTS + 1):
    print(f"Running test #{test_number}")
    a_array = random.sample(range(1, 300), NUM_OF_JOBS)
    b_array = random.sample(range(1, 300), NUM_OF_JOBS)

    complete_search_strategy = CompleteStrategy(
        "Complete Search Strategy", a_array, b_array, NUM_OF_JOBS)
    dp_strategy = DP("DP Strategy", a_array, b_array, NUM_OF_JOBS)

    start = time.process_time()
    complete_search_strategy.solve()
    mid = time.process_time()
    dp_strategy.solve()
    end = time.process_time()

    dp_correct_order = dp_strategy.correct_order
    cs_correct_order = complete_search_strategy.correct_order

    print(f"{complete_search_strategy.name}: {cs_correct_order}")
    print(f"{dp_strategy.name}: {dp_correct_order}")
    print(f"Process time of {complete_search_strategy.name}: {mid-start}")
    print(f"Process time of {dp_strategy.name}: {end-mid}")

    if dp_strategy.cmax == complete_search_strategy.cmax:
        SUCCESS += 1
        print(f"Test #{test_number}: \033[92m\33[1mSUCCESS\33[0m")
    else:
        FAILURES += 1
        print(f"Test #{test_number}: \033[91m\33[1mFAILED\33[0m")

    print("-"*80)

print(f"SUCCESS: \033[92m\33[1m{SUCCESS}\33[0m/{NUM_OF_TESTS}, FAILURES: \033[91m\33[1m{FAILURES}\33[0m/{NUM_OF_TESTS}")
