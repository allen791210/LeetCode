"""
"123"
"132"
"213"
"231"
"312"
"321"
Input: n = 3, k = 3
Output: "213"
"""
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        if n == 0 or k == 0:
            return ""
        
        fac = [1]
        for i in range(1, n + 1):
            fac.append(fac[-1] * i)
        
        # X=a_{n}(n-1)!+a_{n-1}(n-2)!+....+a_{1}(0)!
        elegible = [i for i in range(1, n + 1)]
        per = []
        k -= 1
        for i in range(1, n + 1):
            digit = k // fac[n - i] # n-1! -> n-2! ->...0 !
            per.append(elegible[digit])
            del elegible[digit]
            k -= digit * fac[n - i]
        return "".join([str(x) for x in per])