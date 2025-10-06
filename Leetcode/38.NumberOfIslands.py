"""
Number of Islands (Medium)
Given an m x n 2D binary grid which represents a map of '1's (land) and '0's (water), return the number of islands.
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Visualization:
1 1 1 1 0
1 1 0 1 0
1 1 0 0 0
0 0 0 0 0

All the 1's are connected (forming one island)
Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

Visualization:
1 1 0 0 0  <- Island 1
1 1 0 0 0  <- Island 1
0 0 1 0 0  <- Island 2
0 0 0 1 1  <- Island 3

Three separate islands
Example 3:
Input: grid = [
  ["1","0","1","0","1"],
  ["0","1","0","1","0"],
  ["1","0","1","0","1"]
]
Output: 9

Visualization (checkerboard pattern):
1 0 1 0 1
0 1 0 1 0
1 0 1 0 1

Each 1 is isolated (9 islands)

"""


class Solution:
    def numIslands(self, grid):
        if not grid or not grid[0]:
            return 0
        
        rows = len(grid)
        cols = len(grid[0])
        count = 0
        
        def dfs(r, c):
            # Base cases: out of bounds or water or already visited
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
                return
            
            # Mark current cell as visited by changing '1' to '0'
            grid[r][c] = '0'
            
            # Explore all 4 directions (up, down, left, right)
            dfs(r - 1, c)  # up
            dfs(r + 1, c)  # down
            dfs(r, c - 1)  # left
            dfs(r, c + 1)  # right
        
        # Traverse every cell in the grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':  # Found unvisited land
                    count += 1          # New island found!
                    dfs(r, c)           # Mark entire island as visited
        
        return count
