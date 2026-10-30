def right_rotate(arr, k):
    if not arr:
        return arr

    k = k % len(arr)
    return arr[-k:] + arr[:-k] if k else arr


numbers = list(map(int, input("Enter numbers: ").split()))
k = int(input("Enter rotations: "))

print("Right rotated array:", right_rotate(numbers, k))
