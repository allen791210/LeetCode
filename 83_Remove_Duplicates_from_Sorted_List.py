# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
"""
Input: 1->1->2->3->3
Output: 1->2->3
"""
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur = head
        while cur != None:
            pre = cur
            cur = cur.next
            while cur != None and cur.val == pre.val:
                cur = cur.next
            pre.next = cur

        return head