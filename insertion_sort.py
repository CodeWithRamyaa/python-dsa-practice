def insertion_sort(numbers):
for i in range(1, len(numbers)):
key = numbers[i]
j = i - 1

    while j >= 0 and numbers[j] > key:
        numbers[j + 1] = numbers[j]
        j -= 1

    numbers[j + 1] = key

return numbers

numbers = [12, 11, 13, 5, 6]

print("Original list:", numbers)

sorted_numbers = insertion_sort(numbers)

print("Sorted list:", sorted_numbers)
