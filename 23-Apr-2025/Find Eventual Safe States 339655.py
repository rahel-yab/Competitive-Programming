# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        res = []
        colors = [0 for _ in range(len(graph))]
        
        def dfs(node):
            if colors[node] == 1:
                return False
            if colors[node] == 2:
                return True
            colors[node] = 1
            for neigh in graph[node]:
                if not dfs(neigh):
                    return False
            colors[node] = 2
            res.append(node)
            return True

        for i in range(len(graph)):
            if colors[i] == 0:
                dfs(i)
        
        return sorted(res)

