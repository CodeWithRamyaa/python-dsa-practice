def find_common_elements(list1, list2):
common = []


for number in list1:
    if number in list2 and number not in common:
        common.append(number)

return common


list1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 50, 60, 70]

print("First list:", list1)
print("Second list:", list2)
print("Common elements:", find_common_elements(list1, list2))
