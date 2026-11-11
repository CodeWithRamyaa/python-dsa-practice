def find_median(nums1, nums2):
    arr = sorted(nums1 + nums2)

    if not arr:
        return None

    n = len(arr)
    mid = n // 2

    if n % 2 == 1:
        return arr[mid]

    return (arr[mid - 1] + arr[mid]) / 2


nums1 = [1, 3]
nums2 = [2, 4]

print("Median:", find_median(nums1, nums2))
