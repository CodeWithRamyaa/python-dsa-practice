def merge_sorted_lists(list1, list2):
merged = []
i = 0
j = 0


while i < len(list1) and j < len(list2):
    if list1[i] <= list2[j]:
        merged.append(list1[i])
        i += 1
    else:
        merged.append(list2[j])
        j += 1

merged.extend(list1[i:])
merged.extend(list2[j:])

return merged


list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]

print("First list:", list1)
print("Second list:", list2)
print("Merged list:", merge_sorted_lists(list1, list2))
