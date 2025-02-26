import numpy as np
import time

class PmedHighSolver:
    def __init__(self, p, alpha, n, cost_matrix, max_time):
        self.p = p
        self.alpha = alpha
        self.n = n
        self.max_time = max_time
        self.cost_matrix = np.array(cost_matrix)
        self.solution = []

    def find_fitness(self, solution):
        primary_cost = sum(min(self.cost_matrix[i, solution]) for i in range(self.n))
        penalty_cost = sum(np.random.rand() * self.alpha * primary_cost for _ in range(self.n))
        return primary_cost + penalty_cost

    def solve(self):
        start_time = time.time()

        # Initial solution
        self.solution = np.argpartition(self.cost_matrix.sum(axis=1), self.p)[:self.p].tolist()
        best_solution = self.solution[:]
        best_fitness = self.find_fitness(best_solution)

        # Apply heuristic selection (if Naïve Bayes is used)
        selected_hr = 0  # Default heuristic (modify as needed)
        print(f"Selected Heuristic: {selected_hr}")

        for _ in range(10):  # Iterative improvement
            new_solution = self.solution[:]
            np.random.shuffle(new_solution)
            new_fitness = self.find_fitness(new_solution)

            if new_fitness < best_fitness:
                best_fitness = new_fitness
                best_solution = new_solution[:]

        end_time = time.time()
        exec_time = end_time - start_time  # ✅ Add execution time

        return best_solution, best_fitness, exec_time  # ✅ Ensure 3 values are returned
