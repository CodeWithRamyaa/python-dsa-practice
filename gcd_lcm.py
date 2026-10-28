def calculate_gcd(a, b):
while b != 0:
a, b = b, a % b
return abs(a)

def calculate_lcm(a, b):
if a == 0 or b == 0:
return 0


return abs(a * b) // calculate_gcd(a, b)


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

gcd = calculate_gcd(num1, num2)
lcm = calculate_lcm(num1, num2)

print("GCD:", gcd)
print("LCM:", lcm)
