import bisect
from typing import List

def compute_budget_efficient(total_budget: float, citizen_votes: List[List[float]]) -> List[float]:
    """
    Compute the aggregated budget using an exact method without binary search.
    Runs in O(n*m log(n*m)) by exploiting piecewise-linear structure.
    """
    # Flatten all proposals and sort
    flat = [d for votes in citizen_votes for d in votes]
    flat.sort()

    # Prefix sums over flattened proposals
    prefix = [0.0]
    for val in flat:
        prefix.append(prefix[-1] + val)

    total_pairs = len(flat)
    N = total_pairs

    # Find the correct interval for lambda
    lambda_val = 0.0
    for idx, low in enumerate(flat):
        # Count how many proposals > low
        pos = bisect.bisect_right(flat, low)
        count_high = N - pos
        sum_le = prefix[pos]
        # Sum of min(d, low)
        sum_min_low = sum_le + low * count_high

        # No proposals above low => cannot increase further
        if count_high == 0:
            break

        # Candidate lambda in [low, next_flat_value]
        candidate = low + (total_budget - sum_min_low) / count_high

        # Determine next breakpoint
        next_val = flat[idx + 1] if idx + 1 < N else None

        if next_val is None or candidate <= next_val:
            lambda_val = candidate
            break

    # Compute final budgets
    num_projects = len(citizen_votes[0])
    result = [
        sum(min(votes[j], lambda_val) for votes in citizen_votes)
        for j in range(num_projects)
    ]
    # Scale to ensure sum equals exactly total_budget
    scale = total_budget / sum(result) if sum(result) > 0 else 0
    return [x * scale for x in result]

# Example runs
if __name__ == "__main__":
    # Example 1: two citizens, three issues
    votes1 = [[100, 0, 0],
              [0, 0, 100]]
    print("Example 1 - Efficient Method:", compute_budget_efficient(100, votes1))

    # Example 2: three citizens, three issues
    votes2 = [[100, 0, 0],
              [50, 50, 0],
              [50, 50, 0]]
    print("Example 2 - Efficient Method:", compute_budget_efficient(100, votes2))
