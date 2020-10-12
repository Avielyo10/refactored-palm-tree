from strategies.base_strategy import Strategy, formula
from itertools import permutations


class CompleteStrategy(Strategy):
    def solve(self):
        best_perm = range(0, self.num_of_jobs)
        self.cmax = self.calc_cmax(range(0, self.num_of_jobs))

        for perm in permutations(range(0, self.num_of_jobs)):
            curr_cmax = self.calc_cmax(perm)
            if curr_cmax < self.cmax:
                self.cmax = curr_cmax
                best_perm = perm

        for index in best_perm:
            self.correct_order.append(
                (self.a_array[index], self.b_array[index]))

    def calc_cmax(self, perm):
        cmax = 0
        for i in perm:
            cmax += formula(self.a_array[i], self.b_array[i], cmax)
        return cmax
