def selection_sort(numbers):
n = len(numbers)

for i in range(n):
    min_index = i

    for j in range(i + 1, n):
        if numbers[j] < numbers[min_index]:
            min_index = j

    numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

return numbers

numbers = [29, 10, 14, 37, 13]

print("Original list:", numbers)

sorted_numbers = selection_sort(numbers)

print("Sorted list:", sorted_numbers)
