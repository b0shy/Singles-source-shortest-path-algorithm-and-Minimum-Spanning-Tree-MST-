import heapq
import sys
from collections import defaultdict

# This script implements Dijkstra's algorithm to find the shortest paths
# from a source node to all other nodes in a weighted graph.

def read_graph(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    
    num_nodes, num_edges, graph_type = lines[0].split()
    graph_type = graph_type.upper()
    is_directed = graph_type == 'D'
    
    graph = defaultdict(list)
    nodes = set()
    
    for line in lines[1:-1]:
        u, v, w = line.split()
        w = int(w)
        graph[u].append((v, w))
        nodes.update([u, v])
        if not is_directed:
            graph[v].append((u, w))
    
    source = lines[-1]
    return graph, source, nodes

def dijkstra(graph, source):
    distances = {node: float('inf') for node in graph}
    previous = {node: None for node in graph}
    distances[source] = 0
    pq = [(0, source)]

    while pq:
        curr_dist, u = heapq.heappop(pq)
        for v, weight in graph[u]:
            distance = curr_dist + weight
            if distance < distances[v]:
                distances[v] = distance
                previous[v] = u
                heapq.heappush(pq, (distance, v))
    
    return distances, previous

def reconstruct_path(prev, target):
    path = []
    while target:
        path.append(target)
        target = prev[target]
    return path[::-1]

def main(filename):
    graph, source, nodes = read_graph(filename)
    distances, previous = dijkstra(graph, source)

    print(f"Source: {source}")
    for node in sorted(nodes):
        if node == source:
            continue
        path = reconstruct_path(previous, node)
        cost = distances[node]
        if cost == float('inf'):
            print(f"No path to {node}")
        else:
            print(f"Path to {node}: {' -> '.join(path)} | Cost: {cost}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python shortest_path.py <filename>")
    else:
        main(sys.argv[1])