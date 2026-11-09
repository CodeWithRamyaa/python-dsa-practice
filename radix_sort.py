def counting_sort(arr, exp):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for num in arr:
        index = (num // exp) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    return output


def radix_sort(arr):
    if not arr:
        return []

    if any(num < 0 for num in arr):
        raise ValueError("Only non-negative integers are supported")

    arr = arr[:]
    maximum = max(arr)
    exp = 1

    while maximum // exp > 0:
        arr = counting_sort(arr, exp)
        exp *= 10

    return arr


numbers = [170, 45, 75, 90, 802, 24, 2, 66]

print("Sorted array:", radix_sort(numbers))
