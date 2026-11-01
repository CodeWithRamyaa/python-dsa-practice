import heapq


def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0

    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, node = heapq.heappop(priority_queue)

        if current_distance > distances[node]:
            continue

        for neighbour, weight in graph[node]:
            distance = current_distance + weight

            if distance < distances[neighbour]:
                distances[neighbour] = distance
                heapq.heappush(
                    priority_queue,
                    (distance, neighbour)
                )

    return distances


graph = {
    'A': [('B', 4), ('C', 2)],
    'B': [('A', 4), ('C', 1), ('D', 5)],
    'C': [('A', 2), ('B', 1), ('D', 8)],
    'D': [('B', 5), ('C', 8)]
}

start = input("Enter starting vertex: ").upper()

if start in graph:
    result = dijkstra(graph, start)

    print("Shortest distances:")

    for node, distance in result.items():
        print(node, ":", distance)
else:
    print("Invalid starting vertex.")
