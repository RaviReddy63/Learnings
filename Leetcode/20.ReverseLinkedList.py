"""
Reverse Linked List
Given the head of a singly linked list, reverse the list and return the reversed list.
Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:
Input: head = [1,2]
Output: [2,1]
Example 3:
Input: head = []
Output: []
Hint: You can solve this either iteratively (using pointers) or recursively. The iterative approach uses three pointers: previous, current, and next.
This is a classic linked list problem that really helps you understand pointer manipulation! Give it a shot! 🔄
"""

class LinkedNode():
    def __init__(self, val):
        self.val = val
        self.next = None

def reverse_linked_list(head):
    prev = None
    curr = head

    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    return prev

if __name__=="__main__":
    node1 = LinkedNode(1)
    node2 = LinkedNode(2)
    node3 = LinkedNode(3)

    node1.next = node2
    node2.next = node3
    node3.next = None

    rev = reverse_linked_list(node1)

    while rev:
        print (rev.val)
        rev = rev.next