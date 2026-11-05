def build_prefix_sum(arr):
    prefix = [0]

    for num in arr:
        prefix.append(prefix[-1] + num)

    return prefix


def range_sum(prefix, left, right):
    if left < 0 or right >= len(prefix) - 1 or left > right:
        return None

    return prefix[right + 1] - prefix[left]


arr = [2, 4, 6, 8, 10]
prefix = build_prefix_sum(arr)

print("Sum from index 1 to 3:", range_sum(prefix, 1, 3))
