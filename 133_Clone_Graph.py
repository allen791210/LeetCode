"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
from collections import deque
class Solution:
    def cloneGraph(self, node):
        if node is None:
            return None

        # use bfs algorithm to traverse the graph and get all nodes.
        nodes = self.getGraphNodes(node)

        mapping = {}
        # copy nodes, store the old->new mapping information in a hash map                    
        for n in nodes:
            mapping[n] = Node(n.val, [])
        
        # copy neighbors(edges)
        for n in nodes:
            for neighbor in n.neighbors:
                mapping[n].neighbors.append(mapping[neighbor]) # KEY: New edges' connection -> append(mapping[neighbor])

        return mapping[node]

    def getGraphNodes(self, node):
        queue = deque([node]) # use list
        results = [node]
        while queue:
            head = queue.popleft()
            for neighbor in head.neighbors:
                if neighbor not in results:
                    queue.append(neighbor)
                    results.append(neighbor)
        return results

# LINTCODE NO.137
"""
Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []
"""

from collections import deque
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None

        # use bfs algorithm to traverse the graph and get all nodes.
        nodes = self.getGraphNodes(node)

        # copy nodes, store the old->new mapping information in a hash map
        mapping = {}
        for n in nodes:
            mapping[n] = UndirectedGraphNode(n.label)
                
        # copy neighbors(edges)
        for n in nodes:
            for neighbor in n.neighbors:
                mapping[n].neighbors.append(mapping[neighbor]) # link to the mapping dict's nodes mapping[neighbor]
                    
        return mapping[node]

    def getGraphNodes(self, node):
        queue = deque([node]) # use list
        results = [node]
        while queue:
            head = queue.popleft()
            for neighbor in head.neighbors:
                if neighbor not in results:
                    queue.append(neighbor)
                    results.append(neighbor)
        return results
