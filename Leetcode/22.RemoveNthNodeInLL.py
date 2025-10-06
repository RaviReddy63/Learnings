"""
Remove Nth Node From End of List
Given the head of a linked list, remove the nth node from the end of the list and return its head.
Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
(Remove the 2nd node from the end, which is 4)
Example 2:
Input: head = [1], n = 1
Output: []
Example 3:
Input: head = [1,2], n = 1
Output: [1]
Hint: Use the two-pointer technique! Move one pointer n steps ahead first, 
then move both pointers together until the first pointer reaches the end. This way, 
the second pointer will be right before the node to remove.
"""

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

def remove_nth_node(head, n):
    dummy = ListNode(0)
    dummy.next = head

    first = dummy
    second = dummy

    for i in range(n+1):
        first = first.next

    while first:
        first = first.next
        second = second.next
    
    second.next = second.next.next

    return dummy.next

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
    head =  (remove_nth_node(node1, 2))

    while head:
        print (head.val)
        head = head.next