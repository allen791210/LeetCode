# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
"""
Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6
"""
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return None

        return self.mergeRangeLists(0, len(lists) - 1, lists)

    def mergeRangeLists(self, start, end, lists):
        if start == end:
            return lists[start]
        
        mid = (start + end) // 2
        left = self.mergeRangeLists(start, mid, lists)
        right = self.mergeRangeLists(mid + 1, end, lists)
        
        return self.mergeTwoLists(left, right)


    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        tail = dummy
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