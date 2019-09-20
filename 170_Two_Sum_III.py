class TwoSum:
    """
    @param number: An integer
    @return: nothing
    """
    def add(self, number):
        self.nums = []
        if self.nums == []:
            self.nums.append(number)

        start = 0
        end = len(self.nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if self.nums[mid] == number:
                self.nums.insert(mid, number)
            elif self.nums[mid] > number:
                end = mid
            else:
                start = mid
        
        if self.nums[end] < number:
            self.nums.insert(end + 1, number)
        else:
            self.nums.insert(start + 1, number)
        print(self.nums)
    """
    @param value: An integer
    @return: Find if there exists any pair of numbers which sum is equal to the value.
    """
    def find(self, value):
        left = 0
        right = len(self.nums) - 1
        while left < right:
            if self.nums[left] + self.nums[right] == value:
                return True
            elif self.nums[left] + self.nums[right] > value:
                right -= 1
            else:
                left += 1
        
        return False


        self.idx_dict = {}
        for i in range(len(self.nums)):
            complement = value - self.nums[i]
            if complement in self.idx_dict:
                return True
            else:
                self.idx_dict[self.nums[i]] = i
        
        return False


