def formula(x, y, t):
    return x + y*t


class Strategy:
    def __init__(self, name, a_array, b_array, num_of_jobs):
        self.name = name
        self.a_array = a_array
        self.b_array = b_array
        self.num_of_jobs = num_of_jobs
        self.correct_order = []
        self.cmax = 0

    def solve(self):
        print("Not implemented yet")
