def climbing_stairs(n):
    if n <= 0:
        return 0

    if n == 1:
        return 1

    first = 1
    second = 2

    for i in range(3, n + 1):
        first, second = second, first + second

    return second


n = int(input("Enter number of stairs: "))

print("Number of ways:", climbing_stairs(n))
