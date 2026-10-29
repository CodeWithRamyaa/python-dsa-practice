def binary_search(numbers, target, left, right):
if left > right:
return -1

mid = (left + right) // 2

if numbers[mid] == target:
    return mid
elif numbers[mid] > target:
    return binary_search(numbers, target, left, mid - 1)
else:
    return binary_search(numbers, target, mid + 1, right)

numbers = list(map(int, input("Enter sorted numbers: ").split()))
target = int(input("Enter number to search: "))

index = binary_search(numbers, target, 0, len(numbers) - 1)

if index == -1:
print("Element not found.")
else:
print("Element found at index:", index)
