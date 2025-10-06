"""
Merge Two Sorted Lists
You are given the heads of two sorted linked lists list1 and list2.
Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.
Example 1:
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:
Input: list1 = [], list2 = []
Output: []
Example 3:
Input: list1 = [], list2 = [0]
Output: [0]
Hint: You can use a dummy node to make it easier to build the merged list. 
Compare the values from both lists and attach the smaller node to your result.
"""

def mergeTwoLists(list1, list2):
    # Create a dummy node to simplify edge cases
    dummy = ListNode(0)
    current = dummy
    
    # Traverse both lists
    while list1 and list2:
        if list1.val <= list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next
    
    # Attach the remaining nodes (one list is exhausted)
    if list1:
        current.next = list1
    else:
        current.next = list2
    
    return dummy.next  # Skip the dummy node


