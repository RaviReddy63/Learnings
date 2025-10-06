"""
Binary Tree Level Order Traversal (Medium)
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).
Example 1:
Input: root = [3,9,20,null,null,15,7]

      3
     / \
    9  20
      /  \
     15   7

Output: [[3],[9,20],[15,7]]
Example 2:
Input: root = [1]
Output: [[1]]
Example 3:
Input: root = []
Output: []
Hint: This requires Breadth-First Search (BFS) instead of the DFS (recursive) approach you've been using. Use a queue!
Algorithm:

Use a queue, start with root
For each level:

Process all nodes currently in the queue
Add their children to the queue for the next level
Collect values for current level
"""

def level_order_traversal(root):
    if not root:
        return []
    
    i = 0
    output = []
    def level_order(root, i, output):
        if not root:
            return None
        if len(output) != i+1:
            output.append([])
        output[i].append(root.val)
        i += 1
        level_order(root.left, i, output)
        level_order(root.right, i, output)

    level_order(root, i, output)
    return output
    