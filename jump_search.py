import math

def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))
    start = 0
    end = step

    while start < n and arr[min(end, n) - 1] < target:
        start = end
        end += step

        if start >= n:
            return -1

    for i in range(start, min(end, n)):
        if arr[i] == target:
            return i

    return -1


arr = [10, 20, 30, 40, 50, 60, 70]
target = 40

print("Element found at index:", jump_search(arr, target))
