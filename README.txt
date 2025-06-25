Project 2: Graph Algorithms in Python

This project contains two Python programs:

shortest_path.py — Finds the shortest path from a given source node to all other nodes in a graph (using Dijkstra's algorithm).

mst.py — Finds the Minimum Spanning Tree (MST) of an undirected graph (using Kruskal's algorithm).

Both programs take input from a .txt file that describes the graph.

How to Set Up and Run
1. Prerequisites
Make sure you have Python 3 installed on your computer.

2. Folder Structure
Your folder should look like this:

project2/
├── shortest_path.py (Dijkstra's algorithm)
├── mst.py (Kruskal's algorithm)
└── input_graphs/ (Folder with input graph files)
  ├── undirected1.txt
  ├── undirected2.txt
  ├── directed1.txt
  └── directed2.txt

3. Input File Format
Each input file should follow this format:

<number of nodes> <number of edges> <D or U>
<Node1> <Node2> <Weight>
<Node1> <Node2> <Weight>
...
<Source Node> (optional, only for shortest_path.py)

Example:

6 10 U
A B 1
A C 2
B C 1
B D 3
B E 2
C D 1
C E 2
D E 4
D F 3
E F 3
A

Explanation:

"6 10 U" means 6 nodes, 10 edges, and an Undirected graph.

Each of the next lines defines an edge and its weight.

The last line ("A") is the source node for the shortest path program.

4. How to Run shortest_path.py
To run Dijkstra’s algorithm on a graph file:

python shortest_path.py input_graphs/undirected1.txt

This program will display the shortest path from the source node to all other nodes, along with the total cost of each path.

Example output:

Source: A
Path to B: A -> B | Cost: 1
Path to C: A -> C | Cost: 2
Path to D: A -> B -> D | Cost: 4
...

5. How to Run mst.py
To run the Minimum Spanning Tree algorithm:

python mst.py input_graphs/undirected1.txt

Important: This program only works for undirected graphs. If you try to use a directed graph, the program will show an error.

Example output:

MST Edges:
A - B (weight 1)
B - C (weight 1)
C - D (weight 1)
...
Total cost: 12

6. Tips and Warnings
Input files must be formatted correctly with no extra blank lines.

Edge weights must be integers.

Node names should be simple (like A, B, C).

The final source node line is optional and only used by shortest_path.py.

Do not run mst.py with a directed graph input.

7. Sample Commands
To run shortest_path.py with a directed graph:

python shortest_path.py input_graphs/directed1.txt

To run mst.py with a second undirected graph:

python mst.py input_graphs/undirected2.txt