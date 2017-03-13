# -*- coding: utf-8 -*-
"""
Created on Thu Dec 22 16:48:54 2016

@author: user
"""

class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int] children
        :type s: List[int] cookie
        :rtype: int
        """
        g.sort()
        s.sort()
        s.reverse()
        g.reverse()
        result = 0
        
        for i in s:
            if len(g)>0 and len(s)>0:
                if i < g[-1]:
                    break
                for j in range(len(g)):
                    if i >= g[j]:
                        g.pop(j)
                        result += 1
                        break
                
                
        print(result)
        return result


test = Solution()
test.findContentChildren(g,s)