from strategies.base_strategy import Strategy, formula
from itertools import permutations


class CompleteStrategy(Strategy):
    def solve(self):
        best_perm = range(0, self.num_of_jobs)
        total_cmax = self.calc_cmax(best_perm)

        for perm in permutations(range(0, self.num_of_jobs)):
            curr_cmax = self.calc_cmax(perm)
            if curr_cmax < total_cmax:
                total_cmax = curr_cmax
                best_perm = perm

        for index in best_perm:
            self.correct_order.append(
                (self.a_array[index], self.b_array[index]))
        self.cmax = total_cmax

    def calc_cmax(self, perm):
        cmax = 0
        for i in perm:
            cmax += formula(self.a_array[i], self.b_array[i], cmax)
        return cmax
