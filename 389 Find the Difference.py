import collections

class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        ds = collections.Counter(s)
        dt = collections.Counter(t)
        return (dt-ds).keys().pop()
        #print dt-ds


#s= 'abccd'
#t= 'abccde'
#test = Solution()
#test.findTheDifference(s,t)
