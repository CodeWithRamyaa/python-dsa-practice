def longest_consecutive(numbers):
    num_set = set(numbers)
    longest = 0

    for number in num_set:
        if number - 1 not in num_set:
            current = number
            count = 1

            while current + 1 in num_set:
                current += 1
                count += 1

            longest = max(longest, count)

    return longest


numbers = list(map(int, input("Enter numbers: ").split()))

print("Longest consecutive sequence length:",
      longest_consecutive(numbers))
