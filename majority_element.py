def majority_element(numbers):
    count = 0
    candidate = None

    for number in numbers:
        if count == 0:
            candidate = number

        if number == candidate:
            count += 1
        else:
            count -= 1

    if numbers.count(candidate) > len(numbers) // 2:
        return candidate

    return None


numbers = list(map(int, input("Enter numbers: ").split()))

result = majority_element(numbers)

if result is None:
    print("No majority element found.")
else:
    print("Majority element:", result)
