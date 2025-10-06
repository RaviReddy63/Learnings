"""
Symmetric Tree (Easy)
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
Example 1:
Input: root = [1,2,2,3,4,4,3]

      1
     / \
    2   2
   / \ / \
  3  4 4  3

Output: true
Example 2:
Input: root = [1,2,2,null,3,null,3]

      1
     / \
    2   2
     \   \
      3   3

Output: false
Example 3:
Input: root = [1]
Output: true
Hint: A tree is symmetric if:

The left subtree is a mirror reflection of the right subtree

To check if two trees are mirrors:

Their root values are equal
The left subtree of one matches the right subtree of the other
The right subtree of one matches the left subtree of the other
"""

def symmetric_tree(root):

    if not root:
        return True

    def symmetry(root1, root2):
        if not root1 and not root2:
            return True
        elif not root1 or not root2:
            return False
        
        if root1.val != root2.val:
            return False
        
        left = symmetry(root1.left, root2.right)
        right = symmetry(root1.right, root2.left)

        if left == False or right == False:
            return False
        else:
            return True
        
    return symmetry(root.left, root.right)
