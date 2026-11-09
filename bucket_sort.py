def bucket_sort(arr):
    if not arr:
        return []

    bucket_count = len(arr)
    buckets = [[] for _ in range(bucket_count)]

    for num in arr:
        index = min(int(num * bucket_count), bucket_count - 1)
        buckets[index].append(num)

    result = []

    for bucket in buckets:
        bucket.sort()
        result.extend(bucket)

    return result


arr = [0.42, 0.32, 0.23, 0.52, 0.25, 0.47, 0.51]

print("Sorted array:", bucket_sort(arr))
