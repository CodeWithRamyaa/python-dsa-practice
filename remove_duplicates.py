def remove_duplicates(numbers):
unique_numbers = []


for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)

return unique_numbers

numbers = [10, 20, 10, 30, 20, 40, 50, 30]

print("Original list:", numbers)

result = remove_duplicates(numbers)

print("List without duplicates:", result)
