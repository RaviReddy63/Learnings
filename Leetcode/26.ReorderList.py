"""
Reorder List
You are given the head of a singly linked-list. The list can be represented as:
L0 → L1 → L2 → ... → Ln-1 → Ln
Reorder the list to be in the following form:
L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → ...
You may not modify the values in the list's nodes. Only nodes themselves may be changed.
Example 1:
Input: head = [1,2,3,4]
Output: [1,4,2,3]
Example 2:
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
Example 3:
Input: head = [1]
Output: [1]
Hint: This combines multiple techniques:

Find the middle (slow/fast pointers)
Reverse the second half
Merge the two halves by alternating nodes

This is like a "boss fight" problem that uses everything you've learned! Give it a shot! 🔥Retry
"""

def reorderList(head):
    if not head or not head.next:
        return
    
    # Step 1: Find the middle
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    # Step 2: Reverse the second half
    prev = None
    curr = slow
    
    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp
    
    # Step 3: Merge the two halves
    first = head
    second = prev  # prev is head of reversed second half
    
    while second.next:  # second half might be longer by 1
        # Save next pointers
        temp1 = first.next
        temp2 = second.next
        
        # Reorder
        first.next = second
        second.next = temp1
        
        # Move pointers
        first = temp1
        second = temp2

    