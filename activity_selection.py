def activity_selection(activities):
    activities.sort(key=lambda x: x[1])

    selected = []
    last_end = float('-inf')

    for start, end in activities:
        if start >= last_end:
            selected.append((start, end))
            last_end = end

    return selected


n = int(input("Enter number of activities: "))

activities = []

for i in range(n):
    start = int(input("Enter start time: "))
    end = int(input("Enter end time: "))
    activities.append((start, end))

selected = activity_selection(activities)

print("Selected activities:", selected)
print("Maximum activities:", len(selected))
