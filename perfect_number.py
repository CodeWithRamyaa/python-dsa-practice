def is_perfect_number(number):
if number < 2:
return False


divisor_sum = 1

for i in range(2, int(number ** 0.5) + 1):
    if number % i == 0:
        divisor_sum += i

        other_divisor = number // i

        if other_divisor != i:
            divisor_sum += other_divisor

return divisor_sum == number


number = int(input("Enter a positive integer: "))

if is_perfect_number(number):
print(number, "is a perfect number.")
else:
print(number, "is not a perfect number.")
