def two_sum(numbers, target):
seen = {}


for i, number in enumerate(numbers):
    complement = target - number

    if complement in seen:
        return [seen[complement], i]

    seen[number] = i

return []


numbers = [2, 7, 11, 15]
target = int(input("Enter the target: "))

result = two_sum(numbers, target)

if result:
print("Indices:", result)
print("Numbers:", numbers[result[0]], "and", numbers[result[1]])
else:
print("No pair found")
