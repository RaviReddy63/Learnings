"""
Clone Graph (Medium)
Given a reference of a node in a connected undirected graph, return a deep copy (clone) of the graph.
Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.
pythonclass Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
Test case format:
For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an adjacency list.
An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes the set of neighbors of a node in the graph.
The given node will always be the first node with val = 1. You must return the copy of the given node as a reference to the cloned graph.
Example 1:
Input: adjList = [[2,4],[1,3],[2,4],[1,3]]

Graph:
  1 --- 2
  |     |
  4 --- 3

Output: [[2,4],[1,3],[2,4],[1,3]]
Explanation: 
Node 1's neighbors are nodes 2 and 4.
Node 2's neighbors are nodes 1 and 3.
Node 3's neighbors are nodes 2 and 4.
Node 4's neighbors are nodes 1 and 3.
Example 2:
Input: adjList = [[]]

Graph: 1 (single node with no neighbors)

Output: [[]]
Example 3:
Input: adjList = []
Output: []
Explanation: Empty graph, return null/None
Example 4:
Input: adjList = [[2],[1]]

Graph: 1 --- 2

Output: [[2],[1]]
Hint:

You need to create new Node objects (not just copy references!)
Use a hash map to track original node → cloned node mapping
Can use DFS or BFS
The tricky part: clone nodes AND their neighbor connections
"""


class Node:
    def __init__(self, val=0, neighbours= None):
        self.val = val
        self.neighbours = [neighbours if neighbours is not None else []] 

class SolutionDFS:
    def copy_graph(self, node):
        if not node:
            return None
        
        visited = {}
        
        def dfs(node):
            if node in visited:
                return visited[node]

            clone = Node(node)

            visited[node] = clone

            for neighbour in node.neighbours:
                clone.neighbours.append(dfs(neighbour))

            return clone
        
        return dfs(Node)
    
from collections import deque
    
class SolutionBFS:
    def copy_graph(self, node):
        if not node:
            return None
        
        visited = {}

        visited[node] = Node(node.val)

        queue = deque([node])

        while queue:
            curr = queue.popleft()
            for neighbour in curr.neighbours:
                if neighbour not in visited:
                    visited[neighbour] = Node(neighbour.val)
                    queue.append(neighbour)
                visited[curr].neighbours.append(visited[neighbour])
        return visited[node]


            

            
            
