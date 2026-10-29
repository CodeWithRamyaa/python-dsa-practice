def move_zeros(numbers):
result = [n for n in numbers if n != 0]
zero_count = len(numbers) - len(result)
result.extend([0] * zero_count)
return result

numbers = list(map(int, input("Enter numbers: ").split()))

print("Result:", move_zeros(numbers))
