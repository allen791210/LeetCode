class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        if not arr1 or not arr2 or not arr3:
            return []
        
        results = []
        l1, l2, l3 = 0, 0, 0
        while l1 < len(arr1) and l2 < len(arr2) and l3 < len(arr3):
            if arr1[l1] == arr2[l2] == arr3[l3]:
                results.append(arr1[l1])
                l1, l2, l3 = l1 + 1, l2 + 1, l3 + 1
            else:
                min_val = min(arr1[l1], arr2[l2], arr3[l3])
                if arr1[l1] == min_val:
                    l1 += 1
                elif arr2[l2] == min_val:
                    l2 += 1
                else:
                    l3 += 1      
        
        return results