def maximum_sum_subarray(arr, k):
    if k < 1 or k > len(arr):
        return None

    current_sum = sum(arr[:k])
    max_sum = current_sum

    for i in range(k, len(arr)):
        current_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, current_sum)

    return max_sum


arr = [2, 1, 5, 1, 3, 2]
k = 3

print("Maximum subarray sum:", maximum_sum_subarray(arr, k))
