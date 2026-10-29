def find_longest_word(sentence):
words = sentence.split()

if not words:
    return None

longest = words[0]

for word in words[1:]:
    if len(word) > len(longest):
        longest = word

return longest

sentence = input("Enter a sentence: ")

result = find_longest_word(sentence)

if result is None:
print("No words found.")
else:
print("Longest word:", result)
print("Length:", len(result))
