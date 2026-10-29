def is_valid(expression):
stack = []
pairs = {
')': '(',
']': '[',
'}': '{'
}

for char in expression:
    if char in "([{":
        stack.append(char)
    elif char in ")]}":
        if not stack or stack.pop() != pairs[char]:
            return False

return len(stack) == 0

expression = input("Enter brackets: ")

if is_valid(expression):
print("Valid parentheses")
else:
print("Invalid parentheses")
