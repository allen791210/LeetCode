#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar  9 16:32:38 2017

@author: Mac

242. Valid Anagram
Given two strings s and t, write a function to determine if t is an anagram of s.

For example,
s = "anagram", t = "nagaram", return true.
s = "rat", t = "car", return false.

Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?

"""
import collections

class Solution(object):
    def isAnagram(self, s, t):
        """
            :type s: str
            :type t: str
            :rtype: bool
            """
        if len(s) == len(t):
            return collections.Counter(s) == collections.Counter(t)
        else:
            return False

s = 'anagram'
t = 'nagaram'    
test = Solution()
res = test.isAnagram(s,t)
print (res)
