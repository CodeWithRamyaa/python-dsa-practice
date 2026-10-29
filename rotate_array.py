def rotate_array(arr, k):
    if not arr:
        return arr

    k = k % len(arr)
    return arr[-k:] + arr[:-k] if k else arr


numbers = list(map(int, input("Enter array elements: ").split()))
k = int(input("Enter number of rotations: "))

result = rotate_array(numbers, k)

print("Rotated array:", result)
