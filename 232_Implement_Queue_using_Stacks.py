"""
MyQueue queue = new MyQueue();

queue.push(1);
queue.push(2);  
queue.peek();  // returns 1
queue.pop();   // returns 1
queue.empty(); // returns false
"""
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.inStack = []
        self.outStack = []

    def adust(self):
        while self.inStack:
            self.outStack.append(self.inStack.pop())

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.inStack.append(x)        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        self.adust()
        return self.outStack.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        self.adust()
        return self.outStack[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        self.adust()
        return not self.outStack

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()