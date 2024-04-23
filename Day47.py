# 310. Minimum Height Trees

class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1:
            return [0] 
        
        adj = defaultdict(list)
        for edge in edges:
            adj[edge[0]].append(edge[1])
            adj[edge[1]].append(edge[0])

        res = [i for i in adj if len(adj[i]) == 1]
        while n > 2:
            n -= len(res)
            new_leaves = []
            for leaf in res:
                neighbor = adj[leaf].pop()
                adj[neighbor].remove(leaf)
                if len(adj[neighbor]) == 1:
                    new_leaves.append(neighbor)
            res = new_leaves
        return res
        
