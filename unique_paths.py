def unique_paths(rows, cols):
    if rows <= 0 or cols <= 0:
        return 0

    dp = [[1] * cols for _ in range(rows)]

    for i in range(1, rows):
        for j in range(1, cols):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[rows - 1][cols - 1]


print("Unique paths:", unique_paths(3, 3))
