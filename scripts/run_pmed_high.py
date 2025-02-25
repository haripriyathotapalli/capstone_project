import numpy as np
from solvers.pmed_high_solver import PmedHighSolver
from solvers.utils import generate_cost_matrix

if __name__ == "__main__":
    n = 50  # Number of nodes
    p = 5  # Number of facilities
    alpha = 0.2  # Penalty factor
    max_time = 100.0  # Maximum execution time

    cost_matrix = generate_cost_matrix(n)
    solver = PmedHighSolver(p, alpha, n, cost_matrix, max_time)
    best_solution, best_fitness, exec_time = solver.solve()

    print("Best Solution:", best_solution)
    print("Best Fitness:", best_fitness)
    print("Execution Time:", exec_time)
