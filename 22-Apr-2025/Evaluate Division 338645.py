# Problem: Evaluate Division - https://leetcode.com/problems/evaluate-division/

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)
        for i in range(len(equations)):
            u , v = equations[i]
            val = values[i]
            graph[u].append((v ,val))
            graph[v].append((u ,1/val))
        
        def dfs(start,end,total, visited):
            if start not in graph or end not in graph:
                return -1
            if start == end:
                return total
            visited.add(start)
            
            for neigh, weight in graph[start]:
                if neigh not in visited:
                    res = dfs(neigh,end,total * weight,visited)
                    if res != -1:
                        return res
            return -1
        
        ans = []
        for start,end in queries:
            ans.append(dfs(start,end,1,set()))
        return ans
        
        return res



        