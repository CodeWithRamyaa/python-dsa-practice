def factorial(n):
    if n < 0:
        return None

    if n == 0 or n == 1:
        return 1

    return n * factorial(n - 1)


number = int(input("Enter a number: "))

result = factorial(number)

if result is None:
    print("Factorial is not defined for negative numbers.")
else:
    print("Factorial:", result)
