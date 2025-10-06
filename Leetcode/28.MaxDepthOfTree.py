"""
Maximum Depth of Binary Tree (Easy - Great starter!)
Given the root of a binary tree, return its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
Node structure:
pythonclass TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
Example 1:
Input: root = [3,9,20,null,null,15,7]
    3
   / \
  9  20
    /  \
   15   7
Output: 3
Example 2:
Input: root = [1,null,2]
    1
     \
      2
Output: 2
Example 3:
Input: root = []
Output: 0
"""

def MaxDepth(root):
    if not root:
        return 0
    
    leftDepth = MaxDepth(root.left)
    rightDepth = MaxDepth(root.right)

    return 1+max(leftDepth, rightDepth)
