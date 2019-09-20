# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        
        fast, slow = head.next, head # fast = head.next, to choose the left one
        while fast is not None and fast.next is not None: # Note: 需要判斷fast & fast.next
            slow = slow.next
            fast = fast.next.next
        
        return slow