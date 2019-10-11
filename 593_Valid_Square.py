"""
Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
Output: True
"""

class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        if p1 == p2 == p3 == p4:
            return False
        
        cord = [p1, p2, p3, p4]
        cord.sort()
        p1, p2, p3, p4 = cord[0], cord[1], cord[2], cord[3]

        vec_p2p1 = [(p1[1] - p2[1]), (p1[0] - p2[0])]
        vec_p2p4 = [(p4[1] - p2[1]), (p4[0] - p2[0])]
        dot_product = vec_p2p1[0] * vec_p2p4[0] + vec_p2p1[1] * vec_p2p4[1] # 90
        
        dist_p2p1 = (p1[1] - p2[1])**2 + (p1[0] - p2[0])**2
        dist_p2p4 = (p4[1] - p2[1])**2 + (p4[0] - p2[0])**2
        dist_p1p3 = (p1[1] - p3[1])**2 + (p1[0] - p3[0])**2
        dist_p3p4 = (p3[1] - p4[1])**2 + (p3[0] - p4[0])**2 # same length

        return dot_product == 0 and dist_p2p1 == dist_p2p4 == dist_p1p3 == dist_p3p4