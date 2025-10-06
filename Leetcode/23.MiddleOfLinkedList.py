"""
Middle of the Linked List
Given the head of a singly linked list, return the middle node of the linked list.
If there are two middle nodes, return the second middle node.
Example 1:
Input: head = [1,2,3,4,5]
Output: [3,4,5]
(The middle node is 3)
Example 2:
Input: head = [1,2,3,4,5,6]
Output: [4,5,6]
(Two middle nodes: 3 and 4, return the second one which is 4)
Example 3:
Input: head = [1]
Output: [1]
Hint: Use the slow and fast pointer technique again! When the fast pointer reaches the end, 
where will the slow pointer be? 🤔
This is similar to the cycle detection problem - great practice for the two-pointer pattern! 
Give it a try! 🐢🐇RetryClaude can make mistakes. Please double-check responses. Sonnet 4.5
"""

def middle_of_linkedList(head):
    slow = head
    fast = head

    while fast:
        slow = slow.next
        fast = fast.next

    return slow