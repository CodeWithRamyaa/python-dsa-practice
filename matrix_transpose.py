def transpose_matrix(matrix):
rows = len(matrix)
columns = len(matrix[0])

transpose = []

for j in range(columns):
    new_row = []

    for i in range(rows):
        new_row.append(matrix[i][j])

    transpose.append(new_row)

return transpose

rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))

matrix = []

for i in range(rows):
row = list(map(int, input(f"Enter row {i + 1}: ").split()))

if len(row) != columns:
    print("Error: Enter the correct number of elements.")
    raise SystemExit

matrix.append(row)

print("Original matrix:")

for row in matrix:
print(row)

print("Transpose matrix:")

for row in transpose_matrix(matrix):
print(row)
