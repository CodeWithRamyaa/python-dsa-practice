def second_smallest(numbers):
smallest = None
second = None

for number in numbers:
    if smallest is None or number < smallest:
        second = smallest
        smallest = number
    elif number != smallest and (
        second is None or number < second
    ):
        second = number

return second

numbers = list(map(int, input("Enter numbers: ").split()))

result = second_smallest(numbers)

if result is None:
print("Second-smallest distinct element does not exist.")
else:
print("Second-smallest element:", result)
