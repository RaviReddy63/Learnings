"""
Number of Provinces:

Uses an adjacency matrix (n × n matrix where isConnected[i][j] shows if cities i and j are connected)
Graph is given explicitly
You traverse the graph structure directly

Number of Islands:

Uses a 2D grid where each cell is either land ('1') or water ('0')
Graph is implicit - you need to infer connections (islands are adjacent land cells)
You traverse up/down/left/right to find connected land cells

Core algorithm: Both use DFS/BFS to count connected components, so the underlying logic is the same. The main difference is just how you access neighbors:

Provinces: Loop through isConnected[city] to find neighbors
Islands: Check 4 adjacent grid cells (up, down, left, right)

That's it! Same concept, different input format.RetryRR
"""

class Solution:
    def findCircleNum(self, isConnected):
        """
        DFS Solution
        Time: O(n²), Space: O(n)
        """
        n = len(isConnected)
        visited = [False] * n
        provinces = 0
        
        def dfs(city):
            visited[city] = True
            for neighbor in range(n):
                if isConnected[city][neighbor] == 1 and not visited[neighbor]:
                    dfs(neighbor)
        
        for city in range(n):
            if not visited[city]:
                dfs(city)
                provinces += 1
        
        return provinces


class SolutionBFS:
    def findCircleNum(self, isConnected):
        """
        BFS Solution
        Time: O(n²), Space: O(n)
        """
        from collections import deque
        
        n = len(isConnected)
        visited = [False] * n
        provinces = 0
        
        for city in range(n):
            if not visited[city]:
                queue = deque([city])
                visited[city] = True
                
                while queue:
                    curr = queue.popleft()
                    for neighbor in range(n):
                        if isConnected[curr][neighbor] == 1 and not visited[neighbor]:
                            visited[neighbor] = True
                            queue.append(neighbor)
                
                provinces += 1
        
        return provinces


class SolutionUnionFind:
    def findCircleNum(self, isConnected):
        """
        Union-Find Solution
        Time: O(n²·α(n)), Space: O(n)
        """
        n = len(isConnected)
        parent = list(range(n))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            root_x, root_y = find(x), find(y)
            if root_x != root_y:
                parent[root_x] = root_y
        
        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j] == 1:
                    union(i, j)
        
        return len(set(find(i) for i in range(n)))


# Test cases
if __name__ == "__main__":
    sol = Solution()
    
    # Test 1
    isConnected1 = [[1,1,0],
                    [1,1,0],
                    [0,0,1]]
    print(f"Test 1: {sol.findCircleNum(isConnected1)}")  # Output: 2
    
    # Test 2
    isConnected2 = [[1,0,0],
                    [0,1,0],
                    [0,0,1]]
    print(f"Test 2: {sol.findCircleNum(isConnected2)}")  # Output: 3
    
    # Test 3
    isConnected3 = [[1,1,1],
                    [1,1,1],
                    [1,1,1]]
    print(f"Test 3: {sol.findCircleNum(isConnected3)}")  # Output: 1