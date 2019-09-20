from collections import deque
class Solution:
    """
    @param org: a permutation of the integers from 1 to n
    @param seqs: a list of sequences
    @return: true if it can be reconstructed only one or false
    """
    
    """
    Corner case:
    1: [], [[]] True
    2: [1], [1] True
    3: [1], [] False
    3: [5,3,2,4,1], [[5,3,2,4],[4,1],[1],[3],[2,4],[1,1000000000]] False
    1 ~ N (Note: the raange of length "+ 1")
    """
    # need to dissect the problem to steps
    def sequenceReconstruction(self, org, seqs):
        if len(org) == 0:
            return True
        
        if len(org) == 1:
            if len(seqs) > 0:
                return org == seqs[0]
            else:
                return False

        # KEY: Always only one element in the queue
        edges = {i: [] for i in range(len(org) + 1)}
        degrees = [0 for i in range(len(org) + 1)] # no :
        two_pair_seqs = []

        for seq in seqs:
            if len(seq) > 2:
                for idx in range(len(seq) - 1):
                    tmp_seq = [seq[idx], seq[idx + 1]]
                    two_pair_seqs.append(tmp_seq)
            elif len(seq) == 2:
                two_pair_seqs.append(seq)
            elif len(seq) == 1:
                if seq[0] not in org:
                    return False
            else:
                continue

        for i, j in two_pair_seqs:
            if i <= len(org) and j <= len(org):
                edges[i].append(j)
                degrees[j] += 1
            else:
                return False

        start_nodes = [i for i in range(1, len(org) + 1) if degrees[i] == 0]
        queue = deque(start_nodes)
        order = []

        while queue:
            if len(queue) > 1:
                return False
            head = queue.popleft()
            order.append(head) 
            for neighbor in edges[head]:
                degrees[neighbor] -= 1
                if degrees[neighbor] == 0:
                    queue.append(neighbor)

        return order == org

# 九章解法
class Solution:
    """
    @param org: a permutation of the integers from 1 to n
    @param seqs: a list of sequences
    @return: true if it can be reconstructed only one or false
    """
    def sequenceReconstruction(self, org, seqs):
        graph = self.build_graph(seqs)
        topo_order = self.topological_sort(graph)
        return topo_order == org
            
    def build_graph(self, seqs):
        # initialize graph
        graph = {}
        for seq in seqs:
            for node in seq:
                if node not in graph:
                    graph[node] = set()
        
        for seq in seqs:
            for i in range(1, len(seq)):
                graph[seq[i - 1]].add(seq[i])

        return graph
    
    def get_indegrees(self, graph):
        indegrees = {
            node: 0
            for node in graph
        }
        
        for node in graph:
            for neighbor in graph[node]:
                indegrees[neighbor] += 1
                
        return indegrees
        
    def topological_sort(self, graph):
        indegrees = self.get_indegrees(graph)
        
        queue = []
        for node in graph:
            if indegrees[node] == 0:
                queue.append(node)
        
        topo_order = []
        while queue:
            if len(queue) > 1:
                # there must exist more than one topo orders
                return None
                
            node = queue.pop()
            topo_order.append(node)
            for neighbor in graph[node]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)
                    
        if len(topo_order) == len(graph):
            return topo_order
            
        return None