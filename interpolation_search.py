def interpolation_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high and arr[low] <= target <= arr[high]:

        if arr[low] == arr[high]:
            return low if arr[low] == target else -1

        position = low + (
            (target - arr[low]) * (high - low)
            // (arr[high] - arr[low])
        )

        if arr[position] == target:
            return position

        if arr[position] < target:
            low = position + 1
        else:
            high = position - 1

    return -1


arr = [10, 20, 30, 40, 50, 60, 70]
target = 50

print("Element found at index:", interpolation_search(arr, target))
