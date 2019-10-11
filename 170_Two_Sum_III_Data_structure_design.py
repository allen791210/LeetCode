"""
add(1); add(3); add(5);
find(4) -> true
find(7) -> false
"""
class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.num_dict = {}

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        # complexity insert a number into a sorted array O(N), array need to move itself
        if number in self.num_dict:
            self.num_dict[number] += 1
        else:
            self.num_dict[number] = 1

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for key in self.num_dict:
            # key: value - key == key and self.num_dict[key] > 1 -> (value - key != key or self.num_dict[key] > 1)
            if value - key in self.num_dict and (value - key != key or self.num_dict[key] > 1):
                return True
            
        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)