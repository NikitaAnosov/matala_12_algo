import bisect
from typing import List

def compute_budget_binary_search(total_budget: float, citizen_votes: List[List[float]], tol: float = 1e-6,
                                 max_iter: int = 100) -> List[float]:
    """
    Compute the aggregated budget using the generalized-median algorithm
    with piecewise-linear functions via binary search on the threshold lambda.
    """
    num_citizens = len(citizen_votes)
    num_projects = len(citizen_votes[0])

    # Helper: for a given lambda, compute budgets per project
    def budgets_at_threshold(lmbd: float) -> List[float]:
        # p_j = sum_i min(d_ij, lambda)
        return [
            sum(min(votes[j], lmbd) for votes in citizen_votes)
            for j in range(num_projects)
        ]

    # Binary search bounds for lambda
    low, high = 0.0, max(max(row) for row in citizen_votes)

    for _ in range(max_iter):
        mid = (low + high) / 2
        p = budgets_at_threshold(mid)
        total = sum(p)
        if abs(total - total_budget) <= tol:
            break
        if total > total_budget:
            high = mid
        else:
            low = mid

    # Final budgets
    final_lambda = (low + high) / 2
    result = budgets_at_threshold(final_lambda)

    # If tiny numerical drift, scale to exact budget
    scale = total_budget / sum(result) if sum(result) > 0 else 0
    return [x * scale for x in result]

# Example runs
if __name__ == "__main__":
    # Example 1: two citizens, three issues
    votes1 = [[100, 0, 0],
              [0, 0, 100]]
    print("Example 1 - Binary Search:", compute_budget_binary_search(100, votes1))
    # Example 2: three citizens, three issues
    votes2 = [[100, 0, 0],
              [50, 50, 0],
              [50, 50, 0]]
    print("Example 2 - Binary Search:", compute_budget_binary_search(100, votes2))
