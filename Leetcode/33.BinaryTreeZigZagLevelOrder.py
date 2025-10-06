"""
Binary Tree Zigzag Level Order Traversal (Medium)
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).
Example 1:
Input: root = [3,9,20,null,null,15,7]

      3
     / \
    9  20
      /  \
     15   7

Output: [[3],[20,9],[15,7]]

Level 0: [3]        (left to right)
Level 1: [20,9]     (right to left)
Level 2: [15,7]     (left to right)
Example 2:
Input: root = [1,2,3,4,null,null,5]

        1
       / \
      2   3
     /     \
    4       5

Output: [[1],[3,2],[4,5]]

Level 0: [1]      (left to right)
Level 1: [3,2]    (right to left)
Level 2: [4,5]    (left to right)
Example 3:
Input: root = [1]
Output: [[1]]
Example 4:
Input: root = []
Output: []
Hint: This is similar to normal level order traversal, but you need to reverse every other level. You can:

Do regular BFS level order traversal
Check if the level number is odd/even
Reverse the list for odd levels (or append in reverse order)
"""

def zigzag_level_order(root):
    if not root:
        return []
    i = 0
    output = []
    def level_order(root, i):
        if not root:
            return None
        if len(output) != i+1:
            output.append([])
        if i%2 == 0:
            output[i].append(root.val)
        else:
            output[i].insert(0,root.val)
        i += 1
        level_order(root.left, i)
        level_order(root.right, i)
    level_order(root, i)
    return output

