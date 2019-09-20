"""
board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
"""
PATH = [(1, 0),
        (0, 1),
        (-1, 0),
        (0, -1)
]
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        char = word[0]
        visited = set()
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] == char:
                    visited.add((row, col))
                    if self.dfs_word(board, word[1:], (row, col), visited):
                        return True
                    visited.remove((row, col))
        return False
        
    def dfs_word(self, board, word, start_idx, visited):
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
                visited.add((row + i, col + j))
                if self.dfs_word(board, word[1:], (row + i, col + j), visited):
                    return True
                visited.remove((row + i, col + j))
        return False