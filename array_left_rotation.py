def left_rotate(arr, k):
    if not arr:
        return arr

    k = k % len(arr)
    return arr[k:] + arr[:k]


numbers = list(map(int, input("Enter numbers: ").split()))
k = int(input("Enter rotations: "))

print("Left rotated array:", left_rotate(numbers, k))
