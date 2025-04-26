# Problem: Loud and Rich - https://leetcode.com/problems/loud-and-rich/description/

class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        graph = [[] for _ in range(n)]
        for u, v in richer:
            graph[v].append(u)

        res = [-1 for _ in range(n)]

        def dfs(node):
            if res[node] != -1:
                return res[node]
            res[node] = node
            for nei in graph[node]:
                minn = dfs(nei)
                if quiet[minn] < quiet[res[node]]:
                    res[node] = minn
            return res[node]
           
        for i in range(n):
            dfs(i)
        return res
