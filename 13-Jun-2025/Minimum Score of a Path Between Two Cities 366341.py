# Problem: Minimum Score of a Path Between Two Cities - https://leetcode.com/problems/minimum-score-of-a-path-between-two-cities/description/

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = [[] for i in range(n+1)]
        for u,v ,w in roads:
            graph[u].append((v,w))
            graph[v].append((u,w))
        
        ans = float('inf')
        q = deque()
        q.append(1)
        visited = set()
        while q:
            a = q.popleft()
            for neigh, w in graph[a]:
                if neigh not in visited:
                    q.append(neigh)
                    visited.add(neigh)
                ans = min(ans,w)
        return ans