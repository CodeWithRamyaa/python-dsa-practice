def find_first(numbers, target):
    left = 0
    right = len(numbers) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2

        if numbers[mid] == target:
            result = mid
            right = mid - 1
        elif numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result


def find_last(numbers, target):
    left = 0
    right = len(numbers) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2

        if numbers[mid] == target:
            result = mid
            left = mid + 1
        elif numbers[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return result


numbers = list(map(int, input("Enter sorted numbers: ").split()))
target = int(input("Enter target: "))

first = find_first(numbers, target)
last = find_last(numbers, target)

print("First occurrence:", first)
print("Last occurrence:", last)
