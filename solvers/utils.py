import numpy as np

def quicksort(arr):
    """Sorts an array using quicksort algorithm."""
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksort(left) + middle + quicksort(right)

def find_fitness(cost_matrix, solution, alpha):
    """Computes the fitness of a given solution."""
    n = cost_matrix.shape[0]
    primary_cost = sum(min(cost_matrix[i, solution]) for i in range(n))
    penalty_cost = sum(np.random.rand() * alpha * primary_cost for _ in range(n))
    return primary_cost + penalty_cost

def generate_cost_matrix(n, min_val=1, max_val=100):
    """Generates a random cost matrix of size (n x n)."""
    return np.random.randint(min_val, max_val, (n, n))
