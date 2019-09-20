"""
MovingAverage m = new MovingAverage(3);
m.next(1) = 1 // return 1.00000
m.next(10) = (1 + 10) / 2 // return 5.50000
m.next(3) = (1 + 10 + 3) / 3 // return 4.66667
m.next(5) = (10 + 3 + 5) / 3 // return 6.00000
"""
from collections import deque

class MovingAverage:
    """
    @param: size: An integer
    """
    def __init__(self, size):
        self.size = size
        self.queue = deque([])
        self.sum = 0.0
    """
    @param: val: An integer
    @return:  
    """
    def next(self, val):
        if len(self.queue) == self.size:
            self.sum -= self.queue.popleft()

        self.queue.append(val)
        self.sum += val
        
        return self.sum / len(self.queue)

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param = obj.next(val)