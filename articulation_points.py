def articulation_points(graph):
    timer = 0
    visited = set()
    discovery = {}
    low = {}
    result = set()

    def dfs(node, parent):
        nonlocal timer

        visited.add(node)
        discovery[node] = low[node] = timer
        timer += 1
        children = 0

        for neighbour in graph[node]:
            if neighbour == parent:
                continue

            if neighbour not in visited:
                children += 1
                dfs(neighbour, node)

                low[node] = min(low[node], low[neighbour])

                if parent is not None and low[neighbour] >= discovery[node]:
                    result.add(node)

            else:
                low[node] = min(low[node], discovery[neighbour])

        if parent is None and children > 1:
            result.add(node)

    for node in graph:
        if node not in visited:
            dfs(node, None)

    return sorted(result)


graph = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1, 3],
    3: [2, 4, 5],
    4: [3],
    5: [3]
}

print("Articulation points:", articulation_points(graph))
