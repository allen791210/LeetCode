class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while len(str(num)) > 1:
            temp = 0
            str_int = str(num)
            
            for i in str_int:
                temp += int(i)
            num = temp

        #print num
        return num

#test = Solution()
#test.addDigits(1234)
