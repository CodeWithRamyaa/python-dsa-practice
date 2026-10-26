def character_frequency(text):
frequency = {}

for char in text:
    if char in frequency:
        frequency[char] += 1
    else:
        frequency[char] = 1

return frequency

text = input("Enter a string: ")

result = character_frequency(text)

print("Character frequency:")

for char, count in result.items():
print(char, ":", count)
