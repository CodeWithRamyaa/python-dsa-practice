def maximum_subarray_sum(numbers):
if not numbers:
return None

current_sum = numbers[0]
maximum_sum = numbers[0]

for number in numbers[1:]:
    current_sum = max(number, current_sum + number)
    maximum_sum = max(maximum_sum, current_sum)

return maximum_sum

numbers = list(map(int, input("Enter numbers: ").split()))

result = maximum_subarray_sum(numbers)

if result is None:
print("Please enter at least one number.")
else:
print("Maximum subarray sum:", result)
