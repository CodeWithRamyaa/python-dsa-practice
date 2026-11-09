def has_cycle(graph):
    visited = set()

    def dfs(node, parent):
        visited.add(node)

        for neighbour in graph[node]:
            if neighbour not in visited:
                if dfs(neighbour, node):
                    return True
            elif neighbour != parent:
                return True

        return False

    for node in graph:
        if node not in visited:
            if dfs(node, None):
                return True

    return False


graph = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1, 3],
    3: [2]
}

print("Cycle detected:", has_cycle(graph))
