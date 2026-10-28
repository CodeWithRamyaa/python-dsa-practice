def binary_to_decimal(binary):
decimal = 0


for digit in binary:
    if digit not in "01":
        return None

    decimal = decimal * 2 + int(digit)

return decimal

binary = input("Enter a binary number: ")

result = binary_to_decimal(binary)

if result is None or binary == "":
print("Please enter a valid binary number.")
else:
print("Decimal:", result)
