"""
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
"""
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_dict = {}
        for n in nums:
            nums_dict[n] = nums_dict.get(n, 0) + 1
        
        sorted_nums = sorted(nums_dict.items(), key=lambda kv: kv[1], reverse = True)
        results = [k for k, v in sorted_nums]

        return results[:k]