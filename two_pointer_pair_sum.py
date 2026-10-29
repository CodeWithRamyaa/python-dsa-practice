def find_pair(numbers, target):
left = 0
right = len(numbers) - 1

while left < right:
    total = numbers[left] + numbers[right]

    if total == target:
        return numbers[left], numbers[right]
    elif total < target:
        left += 1
    else:
        right -= 1

return None

numbers = list(map(int, input("Enter sorted numbers: ").split()))
target = int(input("Enter target sum: "))

result = find_pair(numbers, target)

if result:
print("Pair found:", result)
else:
print("No pair found.")
