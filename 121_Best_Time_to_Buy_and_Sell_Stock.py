"""
Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""
# record min_val
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        max_profit = 0
        min_val = float('inf')
        for price in prices:
            min_val = min(min_val, price)
            max_profit = max(max_profit, price - min_val)

        return max_profit

# Kadane's Algorithm
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        cur_profit = 0
        
        for i in range(1, len(prices)):
            cur_profit += prices[i] - prices[i - 1]
            cur_profit = max(0, cur_profit)
            max_profit = max(max_profit, cur_profit)
        
        return max_profit

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        max_profit = 0
        min_val = float('inf')
        max_val = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                min_val = min(prices[i - 1], min_val)
                max_val = max(prices[i], max_val)
                max_profit = max(max_val - min_val, max_profit)
            else:
                if prices[i] < min_val:
                    min_val, max_val = prices[i], prices[i]

        return max_profit