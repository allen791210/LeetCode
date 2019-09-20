"""
Input:
pattern = "abab"
str = "redblueredblue"
Output: true
Explanation: "a"->"red","b"->"blue"
"""
class Solution:
    """
    @param pattern: a string,denote pattern string
    @param str: a string, denote matching string
    @return: a boolean
    """
    def wordPatternMatch(self, pattern, str):
        return self.dfs(pattern, str, {}, set())
    
    # used words to identify pattern like abab, jkjkjkjk
    def dfs(self, pattern, str, dict_pattern, used_words):
        """
        if len(pattern) == 0 and len(str) == 0:
            return True
        if len(pattern) == 0 and len(str) > 0:
            return False
        """
        if not pattern:
            return not str
            
        char = pattern[0]
        if char in dict_pattern:
            word = dict_pattern[char] # use a variable name for it
            #if target != str[:len(target)]: # use str.startswith(word)
            if not str.startswith(word):
                return False
            else:
                return self.dfs(pattern[1:], str[len(word):], dict_pattern, used_words) # return following dfs results
        else:
            for i in range(1, len(str) + 1):
                word = str[:i]
                if word in used_words: # used_words avoids duplicates
                    continue
                
                dict_pattern[char] = word
                used_words.add(word)
                if self.dfs(pattern[1:], str[i:], dict_pattern, used_words): # if cond
                    return True
                
                dict_pattern.pop(char) # backtracking
                used_words.remove(word)
        return False