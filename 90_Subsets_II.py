"""
Input: [1,2,2]
Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if nums == []:
            return [[]]
        nums.sort() # KEY: remove duplicate -> sort first
        results = []
        self.dfs(nums, 0, [], results)

        return results

    def dfs(self, nums, start_idx, tmp_subsets, results):        
        results.append(tmp_subsets)

        for i in range(start_idx, len(nums)):
            if i != start_idx and nums[i - 1] == nums[i]:
                continue
            self.dfs(nums, i + 1, tmp_subsets + [nums[i]], results)