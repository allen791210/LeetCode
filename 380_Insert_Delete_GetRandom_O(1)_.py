import random

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.random_list = []
        self.random_set = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.random_set:
            return False
        else:
            self.random_list.append(val)
            self.random_set[val] = len(self.random_list) - 1
            return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.random_set:
            # KEY: exchange the element with the last one
            idx, last = self.random_set[val], self.random_list[-1]
            self.random_list[idx] = last
            self.random_set[last] = idx
            self.random_list.pop()
            self.random_set.pop(val)
            return True
        else:
            return False
    
    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        i = random.randrange(len(self.random_list)) #KEY random.randrange()
        return self.random_list[i]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()