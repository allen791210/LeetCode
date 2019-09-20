# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """
"""
Input: [1,[4,[6]]]
Output: [1,4,6]
Explanation: By calling next repeatedly until hasNext returns false, 
             the order of elements returned by next should be: [1,4,6].
"""
class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.next_elem = None
        self.stack = nestedList[::-1] # stack causes inverted order

    def next(self):
        """
        :rtype: int
        """
        if self.next_elem is None:
            self.hasNext()
        
        result, self.next_elem = self.next_elem, None
        
        return result
    
    # KEY: isInteger(), getInteger(), getList()
    def hasNext(self):
        """
        :rtype: bool
        """
        if self.next_elem:
            return True
        
        while self.stack:
            top = self.stack.pop()
            if top.isInteger(): # use "isInteger()"
                self.next_elem = top.getInteger()
                return True
            else:
                for elem in reversed(top.getList()): # need to use "getList()"
                    self.stack.append(elem)

        return False

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())