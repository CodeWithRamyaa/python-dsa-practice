def linear_search(numbers, target):
for index in range(len(numbers)):
if numbers[index] == target:
return index

```
return -1
```

numbers = [10, 20, 30, 40, 50]

target = int(input("Enter the number to search: "))

result = linear_search(numbers, target)

if result != -1:
print("Element found at index:", result)
else:
print("Element not found")

