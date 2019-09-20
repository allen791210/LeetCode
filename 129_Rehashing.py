"""
C++/Java: if you directly calculate -4 % 3 you will get -1. You can use function: a % b = (a % b + b) % b to make it is a non negative integer.
Python: you can directly use -1 % 3, you will get 2 automatically.

Input : [null, 21->9->null, 14->null, null]
Output : [null, 9->null, null, null, null, 21->null, 14->null, null]

Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param hashTable: A list of The first node of linked list
    @return: A list of The first node of linked list which have twice size
    """
    def addListNode(self, num, idx, NewHashTbl):
        node = NewHashTbl[idx]
        while node.next != None:
            node = node.next
        node.next = ListNode(num)

    def addNode(self, num, NewHashTbl):
        idx = num % len(NewHashTbl)
        if NewHashTbl[idx] == None:
            NewHashTbl[idx] = ListNode(num)
        else:
            self.addListNode(num, idx, NewHashTbl)

    def rehashing(self, hashTable):
        if len(hashTable) == 0:
            return []

        size = len(hashTable) * 2
        NewHashTbl = [None] * size
        for node in hashTable:
            while node != None:
                self.addNode(node.val, NewHashTbl) # use "node.val" instead of node because node.next is uncertain
                node = node.next

        return NewHashTbl
    