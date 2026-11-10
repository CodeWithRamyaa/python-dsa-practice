def solve_maze(maze):
    n = len(maze)

    if n == 0 or any(len(row) != n for row in maze):
        return None

    solution = [[0] * n for _ in range(n)]

    def solve(row, col):
        if row == n - 1 and col == n - 1:
            solution[row][col] = 1
            return True

        if (
            0 <= row < n
            and 0 <= col < n
            and maze[row][col] == 1
            and solution[row][col] == 0
        ):
            solution[row][col] = 1

            if solve(row + 1, col):
                return True

            if solve(row, col + 1):
                return True

            solution[row][col] = 0

        return False

    if solve(0, 0):
        return solution

    return None


maze = [
    [1, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 1, 0, 0],
    [1, 1, 1, 1]
]

result = solve_maze(maze)

if result:
    print("Path found:")
    for row in result:
        print(row)
else:
    print("No path found")
