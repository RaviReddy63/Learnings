"""
Find if Path Exists in Graph (Easy)
There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1. The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi.
Given edges, source, and destination, return true if there is a valid path from source to destination, or false otherwise.
Example 1:
Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
Output: true

Explanation: 
Graph looks like:
0 -- 1
|    |
+----2

There are two paths from 0 to 2:
- 0 → 1 → 2
- 0 → 2
Example 2:
Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], source = 0, destination = 5
Output: false

Explanation:
Graph has two separate components:
0 -- 1
|
2

3 -- 5
|    |
+----4

There is no path from 0 to 5 (they're in different connected components)
Example 3:
Input: n = 1, edges = [], source = 0, destination = 0
Output: true

Explanation: Single node, source equals destination
Example 4:
Input: n = 2, edges = [[0,1]], source = 0, destination = 1
Output: true
Hint:

Build an adjacency list from the edges
Use DFS or BFS starting from source
Check if you can reach destination
Keep track of visited nodes to avoid cycles
"""

# DFS method
def find_path_dfs(n, edges, source, destination):
    if source == destination:
        return True
    
    graph = {i:[] for i in range(n)}

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    visited = set()

    def find_path(node):
        if node == destination:
            return True
        
        visited.add(node)
        
        for neighbour in graph[node]:
            if neighbour not in visited:
                if find_path(neighbour):
                    return True

        return False
    return (find_path(source))

#BFS METHOD
from collections import deque

def find_path_bfs(n, edges, source, destination):
    if source == destination:
        return True
    
    graph = {i:[] for i in range(n)}

    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    queue = deque([source])
    visited = set()

    while queue:
        node = queue.popleft()

        if node == destination:
            return True

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)
    return False
