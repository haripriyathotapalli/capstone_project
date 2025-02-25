import numpy as np

def naive_bayes(solution, p_len, n, num_hr, HR_sel_cnt, node_cnt, HR_Lkh):
    """
    Naïve Bayes classifier for facility selection.

    Parameters:
    - solution: List of selected facility indices
    - p_len: Number of facilities
    - n: Number of nodes
    - num_hr: Number of heuristics
    - HR_sel_cnt: List storing heuristic selection counts
    - node_cnt: Matrix tracking occurrences of nodes
    - HR_Lkh: List of likelihood values for each heuristic

    Returns:
    - Selected heuristic index
    """

    probabilities = np.zeros(num_hr)

    for hr in range(num_hr):
        if HR_sel_cnt[hr] > 0:
            likelihood = 1.0
            for fac in solution:
                likelihood *= (node_cnt[hr][fac] + 1) / (HR_sel_cnt[hr] + n)
            probabilities[hr] = likelihood * HR_Lkh[hr]

    probabilities /= probabilities.sum() if probabilities.sum() > 0 else 1

    selected_hr = np.argmax(probabilities)
    
    return selected_hr
