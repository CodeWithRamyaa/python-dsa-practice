def max_area(height):
    left = 0
    right = len(height) - 1
    maximum = 0

    while left < right:
        width = right - left
        area = width * min(height[left], height[right])

        maximum = max(maximum, area)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1

    return maximum


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

print("Maximum water area:", max_area(height))
