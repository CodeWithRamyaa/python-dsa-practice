import heapq

def kth_largest(arr, k):
    if k < 1 or k > len(arr):
        return None

    heap = []

    for num in arr:
        heapq.heappush(heap, num)

        if len(heap) > k:
            heapq.heappop(heap)

    return heap[0]


numbers = [3, 2, 1, 5, 6, 4]
k = 2

print("Kth largest element:", kth_largest(numbers, k))
