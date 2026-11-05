def product_except_self(arr):
    n = len(arr)
    result = [1] * n

    prefix = 1

    for i in range(n):
        result[i] = prefix
        prefix *= arr[i]

    suffix = 1

    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= arr[i]

    return result


arr = [1, 2, 3, 4]
print("Product except self:", product_except_self(arr))
