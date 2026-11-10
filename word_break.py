def word_break(text, word_dict):
    words = set(word_dict)
    dp = [False] * (len(text) + 1)
    dp[0] = True

    for i in range(1, len(text) + 1):
        for j in range(i):
            if dp[j] and text[j:i] in words:
                dp[i] = True
                break

    return dp[len(text)]


text = "leetcode"
dictionary = ["leet", "code"]

print("Can be segmented:", word_break(text, dictionary))
