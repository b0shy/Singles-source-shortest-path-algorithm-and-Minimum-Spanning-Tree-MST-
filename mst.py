import sys

# This script implements Kruskal's algorithm to find the Minimum Spanning Tree (MST) of an undirected graph.

class UnionFind:
    def __init__(self, nodes):
        self.parent = {n: n for n in nodes}
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)
        if root_u != root_v:
            self.parent[root_v] = root_u
            return True
        return False

def read_graph(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    
    num_nodes, num_edges, graph_type = lines[0].split()
    if graph_type != 'U':
        raise ValueError("MST only works on undirected graphs.")
    
    edges = []
    nodes = set()
    for line in lines[1:]:
        parts = line.split()
        if len(parts) != 3:
            continue
        u, v, w = parts
        edges.append((int(w), u, v))
        nodes.update([u, v])
    
    return edges, nodes

def kruskal(edges, nodes):
    edges.sort()
    uf = UnionFind(nodes)
    mst = []
    total_cost = 0

    for weight, u, v in edges:
        if uf.union(u, v):
            mst.append((u, v, weight))
            total_cost += weight
    
    return mst, total_cost

def main(filename):
    edges, nodes = read_graph(filename)
    mst, cost = kruskal(edges, nodes)

    print("MST Edges:")
    for u, v, w in mst:
        print(f"{u} - {v} (weight {w})")
    print(f"Total cost: {cost}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python mst.py <filename>")
    else:
        main(sys.argv[1])
