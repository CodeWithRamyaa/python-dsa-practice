def power(base, exponent):
    if exponent == 0:
        return 1

    if exponent < 0:
        return 1 / power(base, -exponent)

    return base * power(base, exponent - 1)


base = float(input("Enter base: "))
exponent = int(input("Enter exponent: "))

if base == 0 and exponent < 0:
    print("Undefined result.")
else:
    print("Result:", power(base, exponent))
