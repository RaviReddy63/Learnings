"""
Intersection of Two Linked Lists
Given the heads of two singly linked lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.
Example 1:
Input: 
listA = [4,1,8,4,5]
listB = [5,6,1,8,4,5]
       
    4 -> 1
            \
             8 -> 4 -> 5
            /
    5 -> 6 -> 1

Output: Node with value 8 (the intersection node)
Example 2:
Input:
listA = [1,9,1,2,4]
listB = [3,2,4]

    1 -> 9 -> 1
                \
                 2 -> 4
                /
    3

Output: Node with value 2
Example 3:
Input:
listA = [2,6,4]
listB = [1,5]

No intersection
Output: null
Note: The lists physically intersect - they share the same nodes in memory, not just the same values!
Hint: Think about what happens if you traverse both lists. Can you use two pointers that eventually meet at the intersection point?

"""

def IntersectionNode(headA, headB):
    if not headA or not headB:
        return None
    
    pointerA = headA
    pointerB = headB

    while pointerA != pointerB:
        pointerA = pointerA.next if pointerA else headB
        pointerB = pointerB.next if pointerB else headA

    return pointerA
        

    