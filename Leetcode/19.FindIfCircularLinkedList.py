"""
Linked List - Linked List Cycle
Given the head of a linked list, determine if the linked list has a cycle in it. A cycle exists if you can reach a node again by continuously following the next pointer.
Return true if there is a cycle, false otherwise.
Example 1:

Input: head = [3,2,0,-4], with tail connecting back to index 1
Output: true

Example 2:

Input: head = [1,2], no cycle
Output: false

Hint: Think about the "fast and slow pointer" technique (also called Floyd's Cycle Detection or the "tortoise and hare" algorithm).

"""

class ListNode:
    def __init__(self, val = 0):
        self.val = val
        self.next = None

def find_circular_ll(head):
    if not head or not head.next:
        return False
    
    slow = head
    fast = head

    while fast and fast.next:
        if slow.next == fast.next.next:
            return True
        slow = slow.next
        fast = fast.next.next

    return False

if __name__=="__main__":


    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    # node5.next = node3
    print (find_circular_ll(node1))

