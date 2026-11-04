def solve_n_queens(n):
    solutions = []
    board = [-1] * n

    def backtrack(row, columns, diagonals1, diagonals2):
        if row == n:
            solutions.append(board.copy())
            return

        for col in range(n):
            d1 = row - col
            d2 = row + col

            if (col in columns or
                d1 in diagonals1 or
                d2 in diagonals2):
                continue

            board[row] = col

            backtrack(
                row + 1,
                columns | {col},
                diagonals1 | {d1},
                diagonals2 | {d2}
            )

            board[row] = -1

    backtrack(0, set(), set(), set())
    return solutions


n = int(input("Enter board size: "))

if n <= 0:
    print("Enter a positive board size.")
else:
    solutions = solve_n_queens(n)

    print("Number of solutions:", len(solutions))

    if solutions:
        print("First solution:")

        for row in solutions[0]:
            print(" ".join(
                "Q" if col == row else "."
                for col in range(n)
            ))
