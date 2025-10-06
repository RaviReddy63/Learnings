"""
Add Two Numbers
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807
(2 → 4 → 3 represents 342 in reverse)
(5 → 6 → 4 represents 465 in reverse)
(7 → 0 → 8 represents 807 in reverse)
Example 2:
Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:
Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
Explanation: 9999999 + 9999 = 10009998

"""

def add_numbers(headA, headB):
    if headA.val == 0 and not headA.next:
        return headB
    if headB.val == 0 and not headB.next:
        return headA
    
    
    dummy = ListNode(0)

    head = dummy

    sumA = 0
    sumB = 0

    i = 0

    while headA:
        sumA = headA.val*10**i + sumA
        headA = headA.next
        i += 1

    i = 0

    while headB:
        sumB = headB.val*10**i + sumB
        headB = headB.next
        i += 1

    sum = sumA + sumB

    while sum != 0:
        num = sum%10
        dummy1 = ListNode(num)
        dummy.next = dummy1
        dummy = dummy.next
        sum = sum//10

    return head.next