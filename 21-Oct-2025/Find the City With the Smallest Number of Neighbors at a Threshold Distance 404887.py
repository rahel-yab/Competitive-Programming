# Problem: Find the City With the Smallest Number of Neighbors at a Threshold Distance - https://leetcode.com/problems/find-the-city-with-the-smallest-number-of-neighbors-at-a-threshold-distance/

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = defaultdict(list)
        for u , v , w in edges:
            graph[u].append((v , w))
            graph[v].append((u , w))

        def check(start):
            dist = [float("inf")] * n
            dist[start] = 0
            heap = [start]

            while heap:
                node = heappop(heap)
                for nei, w in graph[node]:
                    if dist[node] +  w < dist[nei]:
                        dist[nei] = dist[node] + w
                        heappush(heap, nei)

            return dist
        
        maxx, ans = float("inf") , 0
        for i in range(n):
            distances = check(i)
            c = 0
            for j in distances:
                if j <= distanceThreshold:
                    c += 1
                    
            if c < maxx:
                maxx = c
                ans = i
            if c == maxx and i > ans:
                ans = i
        return ans
