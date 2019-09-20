"""
Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if nums == []:
            return [[]]

        results = []
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
            
            visited[i] = True
            temp_permutation.append(nums[i])
            self.dfs(nums, visited, temp_permutation, results)
            temp_permutation.pop()
            visited[i] = False
