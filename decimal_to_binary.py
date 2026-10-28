def decimal_to_binary(number):
if number == 0:
return "0"


binary = ""

while number > 0:
    remainder = number % 2
    binary = str(remainder) + binary
    number //= 2

return binary

number = int(input("Enter a decimal number: "))

if number < 0:
print("Please enter a non-negative number.")
else:
print("Binary:", decimal_to_binary(number))
