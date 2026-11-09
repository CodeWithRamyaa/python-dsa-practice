class UnionFind:
    def __init__(self, size):
        self.parent = list(range(size))

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x == root_y:
            return False

        self.parent[root_y] = root_x
        return True


def kruskal(vertices, edges):
    uf = UnionFind(vertices)
    mst = []
    total_weight = 0

    for weight, u, v in sorted(edges):
        if uf.union(u, v):
            mst.append((u, v, weight))
            total_weight += weight

    if len(mst) != vertices - 1:
        return None, None

    return mst, total_weight


edges = [
    (10, 0, 1),
    (6, 0, 2),
    (5, 0, 3),
    (15, 1, 3),
    (4, 2, 3)
]

mst, total = kruskal(4, edges)

if mst is None:
    print("Graph is disconnected")
else:
    print("Minimum Spanning Tree:", mst)
    print("Total weight:", total)
