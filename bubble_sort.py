def bubble_sort(numbers):
n = len(numbers)

for i in range(n):
    for j in range(0, n - i - 1):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

return numbers

numbers = [64, 34, 25, 12, 22, 11, 90]

print("Original list:", numbers)

sorted_numbers = bubble_sort(numbers)

print("Sorted list:", sorted_numbers)
