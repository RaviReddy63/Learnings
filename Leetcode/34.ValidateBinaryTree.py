"""
Validate Binary Search Tree (Medium)
Given the root of a binary tree, determine if it is a valid binary search tree (BST).
A valid BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Example 1:
Input: root = [2,1,3]

    2
   / \
  1   3

Output: true
Example 2:
Input: root = [5,1,4,null,null,3,6]

      5
     / \
    1   4
       / \
      3   6

Output: false
Explanation: The root node's value is 5 but its right child's value is 4.
Example 3:
Input: root = [5,4,6,null,null,3,7]

      5
     / \
    4   6
       / \
      3   7

Output: false
Explanation: Node 3 is in the right subtree of 5, but 3 < 5, violating BST property.
Hint: It's not enough to just check if left.val < root.val < right.val. You need to ensure ALL nodes in the left subtree are less than root, and ALL nodes in the right subtree are greater than root.
Think about passing a valid range (min, max) for each node!
This is a classic BST problem! Give it a try! 🌳✓RetryClaude can make mistakes. Please double-check responses.
"""

def validate_binary_tree(root):
    def validate(node, min_val, max_val):
        if not node:
            return True
        if node.val <= min_val or node.val >= max_val:
            return False
        return (validate(node.left, min_val, node.val) and 
                validate(node.right, node.val, max_val))
    
    return validate(root, float('-inf'), float('inf'))

    
        
    
