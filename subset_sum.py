def subset_sum(numbers, target):
    dp = [False] * (target + 1)
    dp[0] = True

    for number in numbers:
        for i in range(target, number - 1, -1):
            dp[i] = dp[i] or dp[i - number]

    return dp[target]


numbers = list(map(int, input("Enter numbers: ").split()))
target = int(input("Enter target sum: "))

if target < 0 or any(number < 0 for number in numbers):
    print("Enter non-negative numbers and target.")
else:
    if subset_sum(numbers, target):
        print("Subset with target sum exists.")
    else:
        print("Subset with target sum does not exist.")
