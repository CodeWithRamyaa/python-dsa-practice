def swap_numbers(a, b):
a, b = b, a
return a, b

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

print("Before swapping:", num1, num2)

num1, num2 = swap_numbers(num1, num2)

print("After swapping:", num1, num2)
