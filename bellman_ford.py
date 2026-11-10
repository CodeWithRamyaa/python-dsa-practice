def bellman_ford(vertices, edges, source):
    distance = [float('inf')] * vertices
    distance[source] = 0

    for _ in range(vertices - 1):
        updated = False

        for u, v, weight in edges:
            if distance[u] != float('inf'):
                new_distance = distance[u] + weight

                if new_distance < distance[v]:
                    distance[v] = new_distance
                    updated = True

        if not updated:
            break

    for u, v, weight in edges:
        if (
            distance[u] != float('inf')
            and distance[u] + weight < distance[v]
        ):
            return None

    return distance


vertices = 5

edges = [
    (0, 1, -1),
    (0, 2, 4),
    (1, 2, 3),
    (1, 3, 2),
    (1, 4, 2),
    (3, 2, 5),
    (3, 1, 1),
    (4, 3, -3)
]

result = bellman_ford(vertices, edges, 0)

if result is None:
    print("Negative weight cycle detected")
else:
    print("Shortest distances:", result)
