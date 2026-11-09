def job_sequencing(jobs):
    jobs.sort(key=lambda x: x[2], reverse=True)

    max_deadline = max(job[1] for job in jobs)
    slots = [None] * max_deadline
    total_profit = 0

    for job_id, deadline, profit in jobs:
        for slot in range(min(deadline, max_deadline) - 1, -1, -1):
            if slots[slot] is None:
                slots[slot] = job_id
                total_profit += profit
                break

    return slots, total_profit


jobs = [
    ("A", 2, 100),
    ("B", 1, 19),
    ("C", 2, 27),
    ("D", 1, 25),
    ("E", 3, 15)
]

schedule, profit = job_sequencing(jobs)

print("Job schedule:", schedule)
print("Maximum profit:", profit)
