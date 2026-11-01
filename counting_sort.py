def counting_sort(arr):
    if not arr:
        return arr

    if any(number < 0 for number in arr):
        raise ValueError("Only non-negative integers are supported.")

    maximum = max(arr)
    count = [0] * (maximum + 1)

    for number in arr:
        count[number] += 1

    result = []

    for number in range(len(count)):
        result.extend([number] * count[number])

    return result


numbers = list(map(int, input("Enter numbers: ").split()))

print("Sorted array:", counting_sort(numbers))
