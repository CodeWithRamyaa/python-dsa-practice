from collections import Counter

def minimum_window(s, t):
    if not s or not t:
        return ""

    required = Counter(t)
    window = {}
    left = 0
    formed = 0
    required_count = len(required)

    best_length = float('inf')
    best_start = 0

    for right, char in enumerate(s):
        window[char] = window.get(char, 0) + 1

        if char in required and window[char] == required[char]:
            formed += 1

        while formed == required_count:
            length = right - left + 1

            if length < best_length:
                best_length = length
                best_start = left

            left_char = s[left]
            window[left_char] -= 1

            if (
                left_char in required
                and window[left_char] < required[left_char]
            ):
                formed -= 1

            left += 1

    if best_length == float('inf'):
        return ""

    return s[best_start:best_start + best_length]


s = "ADOBECODEBANC"
t = "ABC"

print("Minimum window substring:", minimum_window(s, t))
