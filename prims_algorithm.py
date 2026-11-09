import heapq

def prims_algorithm(graph, start):
    visited = set()
    min_heap = [(0, start, None)]
    mst = []
    total_weight = 0

    while min_heap:
        weight, node, parent = heapq.heappop(min_heap)

        if node in visited:
            continue

        visited.add(node)

        if parent is not None:
            mst.append((parent, node, weight))
            total_weight += weight

        for neighbour, edge_weight in graph[node]:
            if neighbour not in visited:
                heapq.heappush(
                    min_heap,
                    (edge_weight, neighbour, node)
                )

    if len(visited) != len(graph):
        return None, None

    return mst, total_weight


graph = {
    0: [(1, 10), (2, 6), (3, 5)],
    1: [(0, 10), (3, 15)],
    2: [(0, 6), (3, 4)],
    3: [(0, 5), (1, 15), (2, 4)]
}

mst, total = prims_algorithm(graph, 0)

if mst is None:
    print("Graph is disconnected")
else:
    print("Minimum Spanning Tree:", mst)
    print("Total weight:", total)
