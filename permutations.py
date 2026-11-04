def generate_permutations(numbers):
    result = []

    def backtrack(start):
        if start == len(numbers):
            result.append(numbers.copy())
            return

        for i in range(start, len(numbers)):
            numbers[start], numbers[i] = numbers[i], numbers[start]

            backtrack(start + 1)

            numbers[start], numbers[i] = numbers[i], numbers[start]

    backtrack(0)
    return result


numbers = list(map(int, input("Enter numbers: ").split()))

print("Permutations:")

for permutation in generate_permutations(numbers):
    print(permutation)
