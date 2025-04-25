# Problem: Strange Printer II - https://leetcode.com/problems/strange-printer-ii/

class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        n, m = len(targetGrid), len(targetGrid[0])
        boundaries = defaultdict(lambda : [float('inf'), -1, float('inf'), -1])

        for r in range(n):
            for c in range(m):
                color = targetGrid[r][c]
                boundaries[color][0] = min(boundaries[color][0] , c)
                boundaries[color][1] = max(boundaries[color][1] , c)
                boundaries[color][2] = min(boundaries[color][2] , r)
                boundaries[color][3] = max(boundaries[color][3] , r)
        
        graph = defaultdict(set)
        indeg = defaultdict(int)

        for color in boundaries:
            l,r ,t ,b = boundaries[color]
            for sr in range(t,b+1):
                for sc in range(l, r+1):
                    if targetGrid[sr][sc] != color:
                        if  targetGrid[sr][sc] not in graph[color]:
                            graph[color].add(targetGrid[sr][sc])
                            indeg[targetGrid[sr][sc]] += 1
        
        queue = deque()
        for node in boundaries:
            if not indeg[node]:
                queue.append(node)
        prossessed = 0
        while queue:
            node = queue.popleft()
            prossessed += 1
            for nei in graph[node]:
                indeg[nei] -= 1
                if not indeg[nei]:
                    queue.append(nei)
        return prossessed == len(boundaries)


