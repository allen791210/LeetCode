"""
Input: pattern = "abba", str = "dog cat cat dog"
Output: true
"""
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        word_dict = {}
        str_list = str.split(" ")
        used_words = []

        if len(pattern) != len(str_list):
            return False

        for i in range(len(pattern)):
            if pattern[i] not in word_dict:
                if str_list[i] in used_words: # KEY: ab "dog dog" or use two maps
                    return False
                word_dict[pattern[i]] = str_list[i]
                used_words.append(str_list[i])
            else:
                if str_list[i] != word_dict[pattern[i]]:
                    return False

        return True