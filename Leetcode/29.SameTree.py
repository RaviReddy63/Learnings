"""
Here's your next binary tree problem:
Same Tree (Easy)
Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
Example 1:
Input: p = [1,2,3], q = [1,2,3]
    1         1
   / \       / \
  2   3     2   3
Output: true
Example 2:
Input: p = [1,2], q = [1,null,2]
    1         1
   /           \
  2             2
Output: false
Example 3:
Input: p = [1,2,1], q = [1,1,2]
    1         1
   / \       / \
  2   1     1   2
Output: false
Hint: Use recursion! Two trees are the same if:

Their root values are equal
Their left subtrees are the same
Their right subtrees are the same

Don't forget to handle the base cases (null nodes)!
Give i
"""

def same_tree(root1, root2):

    if not root1 and not root2:
        return True
    elif not root1 or not root2:
        return False
    elif root1.val != root2.val:
        return False
    
    left = same_tree(root1.left, root2.left)
    right = same_tree(root1.right, root2.right)

    if left == False or right == False:
        return False
    elif left == True and right == True:
        return True
