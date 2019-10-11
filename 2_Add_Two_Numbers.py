# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
"""
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        dummy = cur_node = ListNode(0)
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            cur_node.next = ListNode(carry % 10)
            cur_node = cur_node.next
            carry //= 10

        return dummy.next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2:
            return None
        if not l1:
            return l2
        if not l2:
            return l1
        
        dummy = ListNode(0)
        dummy.next = l1
        l1_ptr, l2_ptr = l1, l2
        
        while l1_ptr and l2_ptr:
            l1_ptr.val = l1_ptr.val + l2_ptr.val
            if l1_ptr.val >= 10:
                l1_ptr.val -= 10
                if l1_ptr.next:
                    l1_ptr.next.val += 1
                else:
                    l1_ptr.next = ListNode(1)
            pre = l1_ptr
            l1_ptr = l1_ptr.next
            l2_ptr = l2_ptr.next
        
        while l1_ptr: # l2_ptr is None
            if l1_ptr.val >= 10:
                l1_ptr.val -= 10
                if l1_ptr.next:
                    l1_ptr.next.val += 1
                else:
                    l1_ptr.next = ListNode(1)
            l1_ptr = l1_ptr.next

        if l2_ptr: # l1_ptr is None
            pre.next = l2_ptr

        return dummy.next
