def palindrome_partitioning(text):
    result = []

    def backtrack(start, path):
        if start == len(text):
            result.append(path[:])
            return

        for end in range(start + 1, len(text) + 1):
            part = text[start:end]

            if part == part[::-1]:
                path.append(part)
                backtrack(end, path)
                path.pop()

    backtrack(0, [])
    return result


text = "aab"

print("Palindrome partitions:")
for partition in palindrome_partitioning(text):
    print(partition)
