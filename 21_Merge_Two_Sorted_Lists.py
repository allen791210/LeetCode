# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
"""
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        tail = dummmy
        while l1 != None and l2 != None:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next

        while l1 != None:
            tail.next = l1
            l1 = l1.next
            tail = tail.next
        
        while l2 != None:
            tail.next = l2
            l2 = l2.next
            tail = tail.next

        return dummy.next




            

            

        