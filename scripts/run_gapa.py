import numpy as np
from solvers.gapa_solver import GapaSolver
from solvers.utils import generate_cost_matrix

if __name__ == "__main__":
    n = 50  # Number of nodes
    p = 5  # Number of facilities
    alpha = 0.2  # Penalty factor

    cost_matrix = generate_cost_matrix(n)
    solver = GapaSolver(p, alpha, n, cost_matrix)
    best_solution, best_fitness = solver.run()

    print("Best Solution:", best_solution)
    print("Best Fitness:", best_fitness)
