# Definition for singly-linked list.
"""
Input: 1->2->3->3->4->4->5
Output: 1->2->5
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head

        pre = dummy # pre points to dummy
        cur = head # cur points to head
        while cur and cur.next:
            if cur.val == cur.next.val:
                while cur and cur.next and cur.val == cur.next.val:
                    cur = cur.next
                cur = cur.next # pass ALL duplicates
                pre.next = cur
            else:
                pre = cur #
                cur = cur.next #

        return dummy.next