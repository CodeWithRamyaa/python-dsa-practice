def binary_search(arr, left, right, target):
    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def exponential_search(arr, target):
    n = len(arr)

    if n == 0:
        return -1

    if arr[0] == target:
        return 0

    index = 1

    while index < n and arr[index] < target:
        index *= 2

    return binary_search(
        arr, index // 2, min(index, n - 1), target
    )


arr = [2, 4, 8, 16, 32, 64, 128]
target = 32

print("Element found at index:", exponential_search(arr, target))
