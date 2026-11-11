def quick_select(arr, k):
    if k < 1 or k > len(arr):
        return None

    arr = arr[:]
    target = k - 1

    def partition(left, right):
        pivot = arr[right]
        i = left

        for j in range(left, right):
            if arr[j] <= pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1

        arr[i], arr[right] = arr[right], arr[i]
        return i

    left, right = 0, len(arr) - 1

    while left <= right:
        pivot_index = partition(left, right)

        if pivot_index == target:
            return arr[pivot_index]
        elif pivot_index < target:
            left = pivot_index + 1
        else:
            right = pivot_index - 1


numbers = [7, 10, 4, 3, 20, 15]
k = 3

print("Kth smallest element:", quick_select(numbers, k))
