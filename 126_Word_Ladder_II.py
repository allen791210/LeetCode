"""
Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]
"""
from collections import deque
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordList.append(beginWord)
        wordList = set(wordList)
        if endWord not in wordList:
            return []
        
        distance = {}
        results = []
        # KEY: Do BFS from "End to Start"
        self.bfs(endWord, beginWord, distance, wordList)
        # Do FDS from start to end
        self.dfs(beginWord, endWord, distance, wordList, [beginWord], results)

        return results

    def bfs(self, beginWord, endWord, distance, wordList): # get distance from every word to target
        queue = deque([beginWord])
        distance[beginWord] = 0
        
        while queue:
            cur_word = queue.popleft()
            # if cur_word == endWord: # KEY: 不可提前返回，會造成部分node沒有遍歷，導致key error
                # return
            for next_word in self.getNextWord(cur_word, wordList):
                if next_word not in distance:
                    distance[next_word] = distance[cur_word] + 1
                    queue.append(next_word)
    
    def getNextWord(self, word, wordList):
        words = []
        for i in range(len(word)):
            for char in "abcdefghijklmnopqrstuvwxyz":
                if char != word[i]:
                    next_word = word[:i] + char + word[i + 1:]
                    if next_word in wordList:
                        words.append(next_word)

        return words

    def dfs(self, beginWord, endWord, distance, wordList, path, results):
        if beginWord == endWord:
            results.append(list(path)) # dfs need deep copy
            return
        
        for next_word in self.getNextWord(beginWord, wordList):
            if distance[next_word] == distance[beginWord] - 1: # KEY: choose the "shortest" path every time
                # path.append(next_word)
                self.dfs(next_word, endWord, distance, wordList, path + [next_word], results)
                # path.pop()