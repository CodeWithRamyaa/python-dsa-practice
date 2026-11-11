def largest_rectangle(heights):
    stack = []
    maximum = 0

    for i in range(len(heights) + 1):
        current = heights[i] if i < len(heights) else 0

        while stack and heights[stack[-1]] > current:
            height = heights[stack.pop()]

            width = i if not stack else i - stack[-1] - 1

            maximum = max(maximum, height * width)

        stack.append(i)

    return maximum


heights = [2, 1, 5, 6, 2, 3]

print("Largest rectangle area:", largest_rectangle(heights))
