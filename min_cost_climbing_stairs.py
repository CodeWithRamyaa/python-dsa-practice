def min_cost_climbing_stairs(cost):
    n = len(cost)

    if n <= 1:
        return 0

    dp = [0] * (n + 1)

    for i in range(2, n + 1):
        dp[i] = min(
            dp[i - 1] + cost[i - 1],
            dp[i - 2] + cost[i - 2]
        )

    return dp[n]


cost = [10, 15, 20]

print("Minimum cost:", min_cost_climbing_stairs(cost))
