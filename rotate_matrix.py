def rotate_matrix(matrix):
    if not matrix:
        return []

    if any(len(row) != len(matrix[0]) for row in matrix):
        raise ValueError("Matrix must be rectangular")

    return [list(row) for row in zip(*matrix[::-1])]


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

rotated = rotate_matrix(matrix)

print("Rotated Matrix:")
for row in rotated:
    print(row)
