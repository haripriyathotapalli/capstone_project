import numpy as np
from solvers.naive_bayes import naive_bayes  # Import Naïve Bayes function

class PmedLowSolver:
    def __init__(self, p, alpha, n, cost_matrix, max_time, num_hr=5):
        self.p = p
        self.alpha = alpha
        self.n = n
        self.max_time = max_time
        self.cost_matrix = np.array(cost_matrix)
        self.solution = []
        self.num_hr = num_hr
        self.HR_sel_cnt = np.zeros(num_hr)
        self.node_cnt = np.zeros((num_hr, n))
        self.HR_Lkh = np.random.rand(num_hr)

    def find_fitness(self, solution):
        primary_cost = sum(min(self.cost_matrix[i, solution]) for i in range(self.n))
        penalty_cost = sum(np.random.rand() * self.alpha * primary_cost for _ in range(self.n))
        return primary_cost + penalty_cost

    def solve(self):
        # Initial solution
        self.solution = np.argpartition(self.cost_matrix.sum(axis=1), self.p)[:self.p].tolist()
        
        # Apply Naïve Bayes to choose heuristic
        selected_hr = naive_bayes(self.solution, self.p, self.n, self.num_hr, 
                                  self.HR_sel_cnt, self.node_cnt, self.HR_Lkh)
        
        print(f"Selected Heuristic: {selected_hr}")
        return self.solution, self.find_fitness(self.solution)
