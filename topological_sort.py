from collections import deque

def topological_sort(graph):
    indegree = {node: 0 for node in graph}

    for node in graph:
        for neighbour in graph[node]:
            indegree[neighbour] += 1

    queue = deque(
        node for node in graph if indegree[node] == 0
    )

    result = []

    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbour in graph[node]:
            indegree[neighbour] -= 1

            if indegree[neighbour] == 0:
                queue.append(neighbour)

    if len(result) != len(graph):
        return None

    return result


graph = {
    5: [2, 0],
    4: [0, 1],
    2: [3],
    3: [1],
    0: [],
    1: []
}

print("Topological order:", topological_sort(graph))
