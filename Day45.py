# 1971. Find if Path Exists in Graph

class Solution(object):
    def validPath(self, n, edges, source, destination):
        graph = {k: [] for k in range(n)}
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        
        visited = set()
        
        def dfs(node):
            if node == destination:
                return True
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    if dfs(neighbor):
                        return True
            return False
        
        return dfs(source)
