"""
Input: [1,1,2]
Output:
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        if nums == []:
            return [[]]

        results = []
        nums.sort() # KEY STEP: remove duplicates -> sort first
        visited = [False] * len(nums) # Note: use "visited" to memorize visited nodes
        self.dfs(nums, visited, [], results)

        return results

    def dfs(self, nums, visited, temp_permutation, results): # 1. definition
        if len(temp_permutation) == len(nums): # 2. exit condition
            results.append(list(temp_permutation)) # Note: "deep copy" (list of "list" which is mutable)
            return
        
        for i in range(len(nums)): # 3. decomposition
            if visited[i]:
                continue
            # # KEY STEP: i > 0 to avoid "single case [1]" "not visited[i - 1]" 代表該重複數被重複使用時(重新當成第一個數)
            if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:  # e.g. 1, 1, 2
                continue

            visited[i] = True
            temp_permutation.append(nums[i])
            self.dfs(nums, visited, temp_permutation, results)
            temp_permutation.pop()
            visited[i] = False
