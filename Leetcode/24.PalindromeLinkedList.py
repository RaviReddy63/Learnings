"""
Palindrome Linked List
Given the head of a singly linked list, return true if it is a palindrome or false otherwise.
Example 1:
Input: head = [1,2,2,1]
Output: true
Example 2:
Input: head = [1,2]
Output: false
Example 3:
Input: head = [1,2,3,2,1]
Output: true
Follow-up: Can you solve it in O(n) time and O(1) space?
Hint: Combine multiple techniques you've learned:

Find the middle of the list (slow/fast pointers)
Reverse the second half
Compare the first half with the reversed second half
"""


def isLLPalindrome(head):
    slow = head
    fast = head

    while fast:
        slow = slow.next
        fast = fast.next.next
    prev = None
    curr = slow

    while curr:
        temp = curr.next
        curr.next = prev
        prev = curr
        curr = temp

    first_half = head
    second_half = prev

    while second_half:
        if first_half.val != second_half.val:
            return False
        first_half = first_half.next
        second_half = second_half.next

    return True
