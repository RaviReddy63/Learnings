"""
Invert Binary Tree (Easy)
Given the root of a binary tree, invert the tree, and return its root.
Inverting means swapping the left and right children of every node in the tree.
Example 1:
Input: root = [4,2,7,1,3,6,9]

Before:
     4
   /   \
  2     7
 / \   / \
1   3 6   9

After:
     4
   /   \
  7     2
 / \   / \
9   6 3   1

Output: [4,7,2,9,6,3,1]
Example 2:
Input: root = [2,1,3]

Before:
  2
 / \
1   3

After:
  2
 / \
3   1

Output: [2,3,1]
Example 3:
Input: root = []
Output: []
Hint: Think recursively! For each node:

Swap its left and right children
Recursively invert the left subtree
Recursively invert the right subtree
"""

def invert_binary_tree(root):
    if not root:
        return None
    
    temp = root.left
    root.left = root.right
    root.right = temp
    
    invert_binary_tree(root.left)
    invert_binary_tree(root.right)