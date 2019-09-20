from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses == 0 or len(prerequisites) == 0:
            return True

        degrees = [0 for i in range(numCourses)]
        edges = {i: [] for i in range(numCourses)}
        
        for i, j in prerequisites: # [0, 1] means from 1 -> 0
            edges[j].append(i) # note: j -> i
            degrees[i] += 1
        
        visited_nodes = []
        start_nodes = [n for n in range(numCourses) if degrees[n] == 0]
        queue = deque(start_nodes)

        while queue:
            head = queue.popleft()
            visited_nodes.append(head)
            for neighbor in edges[head]:
                degrees[neighbor] -= 1
                if degrees[neighbor] == 0:
                    queue.append(neighbor)
        
        return len(visited_nodes) == numCourses
            