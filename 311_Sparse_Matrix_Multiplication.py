"""
     |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                  | 0 0 1 |

Time: n * m * k
Space:
"""

class Solution:
    """
    @param A: a sparse matrix
    @param B: a sparse matrix
    @return: the result of A * B
    """
    def multiply(self, A, B):
        n, m = len(A), len(A[0])
        k = len(B[0])

        result = [[0] * k for _ in range(n)] # col -> row

        for i in range(n):
            for j in range(m):
                if A[i][j] != 0:
                    for p in range(k):
                        result[i][p] += A[i][j] * B[j][p]
        
        return result
        
