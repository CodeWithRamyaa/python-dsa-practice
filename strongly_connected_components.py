def strongly_connected_components(graph):
    visited = set()
    order = []

    def dfs(node):
        visited.add(node)

        for neighbour in graph[node]:
            if neighbour not in visited:
                dfs(neighbour)

        order.append(node)

    for node in graph:
        if node not in visited:
            dfs(node)

    reversed_graph = {node: [] for node in graph}

    for node in graph:
        for neighbour in graph[node]:
            reversed_graph[neighbour].append(node)

    visited.clear()
    components = []

    def reverse_dfs(node, component):
        visited.add(node)
        component.append(node)

        for neighbour in reversed_graph[node]:
            if neighbour not in visited:
                reverse_dfs(neighbour, component)

    for node in reversed(order):
        if node not in visited:
            component = []
            reverse_dfs(node, component)
            components.append(component)

    return components


graph = {
    0: [1],
    1: [2],
    2: [0, 3],
    3: [4],
    4: [5],
    5: [3]
}

print("Strongly connected components:")
for component in strongly_connected_components(graph):
    print(component)
