def fractional_knapsack(items, capacity):
    items.sort(key=lambda x: x[0] / x[1], reverse=True)

    total_value = 0

    for value, weight in items:
        if capacity <= 0:
            break

        if weight <= capacity:
            total_value += value
            capacity -= weight
        else:
            total_value += value * (capacity / weight)
            capacity = 0

    return total_value


n = int(input("Enter number of items: "))

items = []

for i in range(n):
    value = float(input("Enter value: "))
    weight = float(input("Enter weight: "))

    if weight <= 0 or value < 0:
        raise ValueError("Weight must be positive and value non-negative.")

    items.append((value, weight))

capacity = float(input("Enter capacity: "))

if capacity < 0:
    print("Capacity cannot be negative.")
else:
    print("Maximum value:", fractional_knapsack(items, capacity))
