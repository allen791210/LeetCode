"""
Definition for a Directed graph node
class DirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""

from collections import deque
class Solution:
    """
    @param: graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        indegree = self.get_indegree(graph)
        
        topo_order = []
        start_nodes = [n for n in indegree if indegree[n] == 0] # use "for loop" initialize
        queue = deque(start_nodes)

        while queue:
            head = queue.popleft()
            topo_order.append(head.label)
            for neighbor in head.neighbors:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return topo_order

    def get_indegree(self, graph):
        keys = [n for n in graph]
        results = dict.fromkeys(keys, 0) # dict.fromkeys() to initialize dict
        for node in graph:
            for neighbor in node.neighbors:
                results[neighbor] += 1
        
        return results