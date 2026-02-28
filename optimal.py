def min_cost_assignment(cost):
    n = len(cost)
    dp = [-1] * (1 << n)

    def solve(mask):
        worker = bin(mask).count("1")
        if worker == n:
            return 0

        if dp[mask] != -1:
            return dp[mask]

        min_cost = float('inf')

        for task in range(n):
            if not (mask & (1 << task)):
                new_mask = mask | (1 << task)
                total_cost = cost[worker][task] + solve(new_mask)
                min_cost = min(min_cost, total_cost)

        dp[mask] = min_cost
        return min_cost

    return solve(0)