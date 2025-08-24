# Problem: Detonate the Maximum Bombs - https://leetcode.com/problems/detonate-the-maximum-bombs/description/

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        maxx = float('-inf')
        graph = defaultdict(list)
        n = len(bombs)
        for i in range(n):
            x1, y1, r1 = bombs[i]
            for j in range(n):
                if i == j:
                    continue
                x2, y2, _ = bombs[j]
                dis = math.hypot(x2 - x1, y2 - y1)
                if dis <= r1:
                    graph[i].append(j)



        visited = set()
        def dfs(i):
            visited.add(i)
            for nei in graph[i]:
                if nei not in visited:
                    dfs(nei)

        for i in range(n):
            visited = set()
            dfs(i)
            maxx = max(maxx ,len(visited))

        return maxx
