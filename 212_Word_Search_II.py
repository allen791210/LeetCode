"""
Input: 
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]

Output: ["eat","oath"]
"""
DIRECTIONS = [(1, 0),
        (0, 1),
        (-1, 0),
        (0, -1)
]
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        words_set = set(words)
        results = []
        prefix_set = set()
        for word in words:
            for i in range(len(word)):
                prefix_set.add(word[:i + 1])

        for i in range(len(board)):
            for j in range(len(board[0])):
                self.dfs(board, i, j, board[i][j], words_set, prefix_set, set([(i, j)]), results) 
        
        return results
    
    def dfs(self, board, x, y, word, words_set, prefix_set, visited, results):
        if word not in prefix_set:
            return
        
        # NO Return -> Because there maybe words with same prefix like aa, aab, need to keep seaching
        if word in words_set and word not in results: # check if word in results or use set for results
            results.append(word)

        for i, j in DIRECTIONS:
            _x = x + i
            _y = y + j
            if 0 <= _x < len(board) and 0 <= _y < len(board[0]) and (_x, _y) not in visited:
                visited.add((_x, _y))
                self.dfs(board, _x, _y, word + board[_x][_y], words_set, prefix_set, visited, results)
                visited.remove((_x, _y))

PATH = [(1, 0),
        (0, 1),
        (-1, 0),
        (0, -1)
]
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        visited = set()
        memo = {}
        results = []
        
        for i in range(len(words)):
            char = words[i][0]
            visited.clear()
            for row in range(len(board)):
                for col in range(len(board[0])):
                    if board[row][col] == char:
                        if char in results or words[i] in results:
                            continue
                        visited.add((row, col))
                        if self.dfs_word(board, words[i][1:], (row, col), visited, memo):
                            memo[words[i]] = (row, col)
                            results.append(words[i])
                        visited.remove((row, col))
        return results
        
    def dfs_word(self, board, word, start_idx, visited, memo):
        if len(word) == 0:
            return True

        char = word[0]
        row = start_idx[0]
        col = start_idx[1]
        row_length = len(board)
        col_length = len(board[0]) 
        
        for i, j in PATH:
            if 0 <= row + i < row_length and 0 <= col + j < col_length and board[row + i][col + j] == char:
                if (row + i, col + j) in visited:
                    continue
                if word in memo and (row + i, col + j) == memo[word]:
                    return True
                visited.add((row + i, col + j))
                if self.dfs_word(board, word[1:], (row + i, col + j), visited, memo):
                    memo[word] = True
                    return True
                visited.remove((row + i, col + j))
        return False

"""
CASE:
[["a","a"]]
["a"]

[["a","a"]]
["aa"]

[["a","b"],["c","d"]]
["ab","cb","ad","bd","ac","ca","da","bc","db","adcb","dabc","abb","acb"]
"""