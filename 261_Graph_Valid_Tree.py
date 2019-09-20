from collections import defaultdict
from queue import Queue

class Solution:
    """
    @param n: An integer
    @param edges: a list of undirected edges
    @return: true if it's a valid tree, or false
    """
    def validTree(self, n, edges):
        if len(edges) != n - 1:
            return False
        
        edge_dict = defaultdict(list) # use defaultdict to avoid key error
        visited = {}
        
        for i, j in edges:
            edge_dict[i].append(j) # append
            edge_dict[j].append(i)

        queue = Queue()
        queue.put(0)
        visited[0] = True
        while not queue.empty():
            curr = queue.get()
            visited[curr] = True
            for node in edge_dict[curr]:
                if node not in visited:
                    queue.put(node)
        
        return len(visited) == n