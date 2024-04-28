# 834. Sum of Distances in Tree

class Solution(object):
    def sumOfDistancesInTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        g = [[] for _ in range(n)]
        for i, j in edges:
            g[i].append(j)
            g[j].append(i)
       
        res = [0] * n
        c = [1] * n
        def dfs1(node, parent):
            for child in g[node]:
                if child != parent:
                    dfs1(child, node)
                    c[node] += c[child]
                    res[node] += res[child] + c[child]
        
        dfs1(0, -1)
        
        def dfs2(node, parent):
            for child in g[node]:
                if child != parent:
                    res[child] = res[node] - c[child] + (n - c[child])
                    dfs2(child, node)
        
        dfs2(0, -1)
        
        return res
        
