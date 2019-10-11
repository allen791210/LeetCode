class Solution:
    def countSteppingNumbers(self, low: int, high: int) -> List[int]:
        if low >= high:
            return []
        
        results = []
        digits = len(str(low))
        highest_digit = int(str(low)[0])
        _low = n = highest_digit * 10**(digits - 1)
        while _low <= n <= high:
            digits = len(str(n))
            highest_digit = int(str(n)[0])
            self.getStepNum(digits, highest_digit, low, high, results) # KEY: use dfs
            n += 10**(digits - 1)
            
        return results
            
    def getStepNum(self, digits, number, low, high, results):
        if len(str(number)) == digits:
            if low <= number <= high: 
                results.append(number)
            return
            
        lowest_digit = number % 10
        if lowest_digit - 1 >= 0:
            self.getStepNum(digits, number * 10 + lowest_digit - 1, low, high, results)
        if lowest_digit + 1 <= 9:
            self.getStepNum(digits, number * 10 + lowest_digit + 1, low, high, results)
        
        