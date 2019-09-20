class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minStack = [] # KEY: use "minStack"

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        if len(self.minStack) == 0:
            self.minStack.append(x)
        else:
            self.minStack.append(min(x, self.minStack[-1])) # KEY: compare x with minStack[-1]

    def pop(self):
        """
        :rtype: None
        """
        ret = self.stack.pop()
        self.minStack.pop()

        return ret

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.minStack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()