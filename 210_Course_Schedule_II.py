from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if numCourses == 0:
            return []

        degrees = [0 for _ in range(numCourses)]
        edges = {i: [] for i in range(numCourses)}
        order = []
        
        for i, j in prerequisites:
            degrees[i] += 1 # 被指向的node degree + 1
            edges[j].append(i) # edge 對應關係 j -> i
        
        start_nodes = [n for n in range(numCourses) if degrees[n] == 0]
        queue = deque(start_nodes)
        while queue:
            head = queue.popleft()
            order.append(head)
            for neighbor in edges[head]:
                degrees[neighbor] -= 1
                if degrees[neighbor] == 0:
                    queue.append(neighbor)

        return order if len(order) == numCourses else [] # Note: if no solution return []

# use queue object
import queue
class Solution:
    def findOrder(self, numCourses, prerequisites):
        if numCourses == 0:
            return []

        degrees = [0 for _ in range(numCourses)]
        edges = {i: [] for i in range(numCourses)}
        order = []
        
        for i, j in prerequisites:
            degrees[i] += 1 # 被指向的node degree + 1
            edges[j].append(i) # edge 對應關係 j -> i
        
        q = queue.Queue(numCourses) # "queue.Queue(maxsize)"
        start_nodes = [n for n in range(numCourses) if degrees[n] == 0]
        for node in start_nodes:
            q.put(node)
        while not q.empty(): # use empty() to check
            head = q.get()
            order.append(head)
            for neighbor in edges[head]:
                degrees[neighbor] -= 1
                if degrees[neighbor] == 0:
                    q.put(neighbor)
        
        return order if len(order) == numCourses else [] # Note: if no solution return []