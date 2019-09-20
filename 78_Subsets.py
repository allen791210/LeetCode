"""
Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""
"""
因为 nums = [] 的时候如果 target = 0 的话，存在且仅存在一种方案，应该return [[]] 作为结果。
但是如果 target != 0 就是 return []
not nums 可能是 nums = None 也可能是 nums = [].
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if nums == []:
            return [[]]
        
        nums.sort()
        results = []
        self.dfs(nums, 0, [], results)
        
        return results

    def dfs(self, nums, start_idx, tmp_subsets, results):
        results.append(list(tmp_subsets)) # Notice: need "DEEP COPY"

        for i in range(start_idx, len(nums)): # Loop range: "from start_idx"
            tmp_subsets.append(nums[i])
            self.dfs(nums, i + 1, tmp_subsets, results)
            tmp_subsets.pop()


