def house_robber(money):
    if not money:
        return 0

    if any(amount < 0 for amount in money):
        raise ValueError("Amounts must be non-negative.")

    previous = 0
    current = 0

    for amount in money:
        previous, current = current, max(
            current,
            previous + amount
        )

    return current


money = list(map(int, input("Enter house amounts: ").split()))

print("Maximum amount:", house_robber(money))
