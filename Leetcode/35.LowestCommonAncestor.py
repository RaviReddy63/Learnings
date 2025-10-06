"""
Lowest Common Ancestor of a Binary Search Tree (Medium)
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.
The lowest common ancestor is defined as the lowest node in the tree that has both nodes as descendants (a node can be a descendant of itself).
Example 1:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8

        6
       / \
      2   8
     / \ / \
    0  4 7  9
      / \
     3   5

Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.
Example 2:
Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4

        6
       / \
      2   8
     / \ / \
    0  4 7  9
      / \
     3   5

Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself.
"""

def lowestCommonAncestor(root, p, q):
    while root:
        if p.val < root.val and q.val < root.val:
            root = root.left
        elif p.val > root.val and q.val > root.val:
            root = root.right
        else:
            return root