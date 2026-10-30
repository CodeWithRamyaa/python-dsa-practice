def is_sorted(numbers):
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i + 1]:
            return False

    return True


numbers = list(map(int, input("Enter numbers: ").split()))

if is_sorted(numbers):
    print("Array is sorted.")
else:
    print("Array is not sorted.")
